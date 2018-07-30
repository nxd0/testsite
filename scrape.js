const puppeteer = require('puppeteer');

var fs = require('fs');
const TEST_URLS = [
  {'url': 'https://github.com/login', 'name': 'github'},  
  {'url': 'https://www.gartner.com/login/loginInitAction.do?method=initialize&login=mkhdr&TARGET=https%3A%2F%2Fwww.gartner.com%2Fen', 'name': 'gartner'},
  {'url': 'https://www.walmart.com/account/login?tid=0&returnUrl=%2F', 'name': 'walmart'},
  {'url': 'https://tmisha.com/login.html', 'name': 'tmisha'},
  {'url': 'https://airtable.com/login', 'name': 'airtable'},
  {'url': 'https://www.netflix.com/login', 'name': 'netflix'},
  {'url': 'https://twitter.com/', 'name': 'twitter'},
];

const IDX = 5;

//const IDX = parseInt(process.argv[2]);
const OUT_DIR = 'output/';
//var { testLabelFieldGrouping } = require('./LoginTests.js');

//------------------------------------


var day = new Date();

var timestamp = day.getTime();
//console.log(timestamp)



console.log('\n\n--------------------------------------------------------');
console.log('Starting SCRAPE.JS');
console.log('--------------------------------------------------------');

var emailFormElementPath = 'empty';
var theX = 5;
var theY = 10;


(async () => {
  

//{headless: false, slowMo: 100}
  
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  


  /*
  page.on('console', msg => {
    for (let i = 0; i < msg.args.length; ++i)
      console.log(`${i}: ${msg.args[i]}`);
  });
  */

  const url = TEST_URLS[IDX]['url'];
  const name = TEST_URLS[IDX]['name'];
  console.log('\nScraping:', name, url);
  await page.goto(url);
  page.setViewport({width : 1400 , height : 800})
  // await page.screenshot({path: 'example.png'});

  
  //-------------- IF YOU WANT A SCREENSHOT ----------------!!!!!!!!!!!!!!
  //await page.screenshot({path: 'screenshot.png'});



//
//
// START FIRST SCRAPE
//
//
  
  let it = await page.evaluate(() => {
    // let selection = window.devicePixelRatio; // window.getSelection();
    // console.log(selection);
    // return selection;
 

 //var activeElement = document.activeElement;
 //var activeElementName = activeElement.getAttribute('name')


    
    let forms = [...document.querySelectorAll('form')];

    let output = forms.map(form => {
      const tags = ['input', 'label', 'button', '[type="submit"]', 'a'] // ['input, label', 'label'];
      let details = [];
      for(var i=0; i < tags.length; i++) {
        let tag = tags[i];
        details = details.concat([...form.querySelectorAll(tag)]
          .map(el => {

            // dummy element
            var dummyEl = el;

            // check for focus
            var isFocused = (document.activeElement === dummyEl);

            let offsetLeft = el['offsetLeft'];
            let offsetTop = el['offsetTop'];
            let pos = getComputedStyle(el)['position'];
            let display = getComputedStyle(el)['display'];
            let tmp = el;
            

            //NEED TO WORK ON THIS DETECTION //NEED TO WORK ON THIS DETECTION




function fullPath(el){
  var names = [];
  while (el.parentNode){
    if (el.id){
      names.unshift('#'+el.id);
      break;
    }else{
      if (el==el.ownerDocument.documentElement) names.unshift(el.tagName);
      else{
        for (var c=1,e=el;e.previousElementSibling;e=e.previousElementSibling,c++);
        names.unshift(el.tagName+":nth-child("+c+")");
      }
      el=el.parentNode;
    }
  }
  return names.join(" > ");
}


            if ((String(el.getAttribute('name')) == 'email')) {

            emailFormElementPath = fullPath(el);
            }
            


           



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
              
              'focus' : String(isFocused), 
             'csspath' : fullPath(el),
             'value' : el.value,
              
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

      //need if statement
      //if (String(emailFormElement) != '' ) {
        
         
      //}
  });



await page.click('#email');

await page.type('#email', "asdad");




//
//
// START FIRST SCRAPE
//
//
  
  let it2 = await page.evaluate(() => {
    // let selection = window.devicePixelRatio; // window.getSelection();
    // console.log(selection);
    // return selection;
 

 //var activeElement = document.activeElement;
 //var activeElementName = activeElement.getAttribute('name')


    
    let forms = [...document.querySelectorAll('form')];

    let output = forms.map(form => {
      const tags = ['input', 'label', 'button', '[type="submit"]', 'a'] // ['input, label', 'label'];
      let details = [];
      for(var i=0; i < tags.length; i++) {
        let tag = tags[i];
        details = details.concat([...form.querySelectorAll(tag)]
          .map(el => {

            // dummy element
            var dummyEl = el;

            // check for focus
            var isFocused = (document.activeElement === dummyEl);

            let offsetLeft = el['offsetLeft'];
            let offsetTop = el['offsetTop'];
            let pos = getComputedStyle(el)['position'];
            let display = getComputedStyle(el)['display'];
            let tmp = el;
            

            //NEXT COMP DETECT FOR CLICK GOES HERE
            /*
            
            if ((el.getAttribute('name') == 'email')) {
              
            emailFormElement = el;
            }
            */

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
 
              'focus' : String(isFocused), 
              'value' : el.value,
              
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

      //if (emailFormElement != ''){
        //emailFormElement.click();
      //}
  });

  //await this.page.waitFor(2000);


  // TODO: WRITE FUNCTION TO GET SELECTOR FROM THE RIGHT ELEMENT ___-----_____-----_________----
  // HOW: get the path 
  // use elementHandle.click() function?
  //await page.click('#email')

  //emailFormElement.click();

  // print(it)
  // console.log(it); //JSON.parse(it));
  fs.writeFile([OUT_DIR, name,'-start@',timestamp,'.json'].join(''), JSON.stringify(it, null, 2), 'utf8', () => console.log('Done writing'));
  fs.writeFile([OUT_DIR, name,'-emailclick@',timestamp,'.json'].join(''), JSON.stringify(it2, null, 2), 'utf8', () => console.log('Done writing'));

  // testLabelFieldGrouping(it[0]);
  // testLabelFieldGrouping(it[1]);

  // const loginForm = await findLoginForm(page) 
  // console.log('Test 2', it);


//-------------------------
//RUN PYTHON CODE
//-------------------------


var myPythonScriptPath = 'run.py';

// Use python shell
var PythonShell = require('python-shell');
var pyshell = new PythonShell(myPythonScriptPath);

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('Analysis Complete');
    
});

  

  await browser.close();
})();

