const puppeteer = require('puppeteer');

var fs = require('fs');
const TEST_URLS = [
  {'url': 'https://www.walmart.com/account/login?tid=0&returnUrl=%2F', 'name': 'tmisha'},
  {'url': 'https://tmisha.com/login.html', 'name': 'tmisha'},
  {'url': 'https://airtable.com/login', 'name': 'airtable'},
  {'url': 'https://www.netflix.com/login', 'name': 'netflix'},
  {'url': 'https://twitter.com/', 'name': 'twitter'},
];
const IDX = 0;

//const IDX = parseInt(process.argv[2]);
console.log(IDX);
const OUT_DIR = 'python/';
//var { testLabelFieldGrouping } = require('./LoginTests.js');


(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  page.on('console', msg => {
    for (let i = 0; i < msg.args.length; ++i)
      console.log(`${i}: ${msg.args[i]}`);
  });

  const url = TEST_URLS[IDX]['url'];
  const name = TEST_URLS[IDX]['name'];
  console.log(IDX);
  console.log('Doing:', name, url);
  await page.goto(url);
  page.setViewport({width : 1400 , height : 800})
  // await page.screenshot({path: 'example.png'});
  console.log('Test 1');
  await page.screenshot({path: 'screenshot.png'});

  let it = await page.evaluate(() => {
    // let selection = window.devicePixelRatio; // window.getSelection();
    // console.log(selection);
    // return selection;


    let forms = [...document.querySelectorAll('form')];
    let output = forms.map(form => {
      const tags = ['input', 'label', 'button', '[type="submit"]', 'a'] // ['input, label', 'label'];
      let details = [];
      for(var i=0; i < tags.length; i++) {
        let tag = tags[i];
        details = details.concat([...form.querySelectorAll(tag)]
          .map(el => {
            let offsetLeft = el['offsetLeft'];
            let offsetTop = el['offsetTop'];
            let pos = getComputedStyle(el)['position'];
            let display = getComputedStyle(el)['display'];
            let tmp = el;
            while(tmp = tmp.offSetParent) {
              // tmp = tmp.parentNode;
              if('offsetLeft' in tmp) {
                offsetLeft.push(tmp['offsetLeft']);
                offsetTop.push(tmp['offsetTop']);
                pos.push(getComputedStyle(tmp)['position'])
                display.push(getComputedStyle(tmp)['display'])
              }
            } 
            return {
              'offsetLeft': offsetLeft,
              'offsetTop': offsetTop,
              'pos': pos,
              'top': el.getBoundingClientRect().top,
              'left': el.getBoundingClientRect().left,
              'offsetWidth': el['offsetWidth'],
              'offsetHeight': el['offsetHeight'],
              'id': el.getAttribute('id'),
              'name': el.getAttribute('name'),
              'width': getComputedStyle(el)['width'],
              'height': getComputedStyle(el)['height'],
              'display': display,
              // 'cx': getComputedStyle(el)['cx'],
              // 'cy': getComputedStyle(el)['cy'],
              // 'x': getComputedStyle(el)['x'],
              // 'y': getComputedStyle(el)['y'],
              'tag': tag,
              'outerHTML': el['outerHTML'],
              'innerHTML': el['innerHTML'],
              // 'j': el.jsonValue,
              // 'tag': tag,
              // 'styles': // Object.keys(el).map(obj =>)
                        // .filter(key=>typeof el[this]==='function')
                        // getComputedStyle(el),
                        // el.jsonValue(),
            }
          })
        )
      }
      return details;
    });
    return output;
  });
  // print(it)
  // console.log(it); //JSON.parse(it));
  fs.writeFile([OUT_DIR, name,'-out.json'].join(''), JSON.stringify(it, null, 2), 'utf8', () => console.log('Done writing'));
  // testLabelFieldGrouping(it[0]);
  // testLabelFieldGrouping(it[1]);

  // const loginForm = await findLoginForm(page) 
  // console.log('Test 2', it);
  await browser.close();
})();