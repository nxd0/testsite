const puppeteer = require('puppeteer');

async function getPic() {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  await page.goto('https://noahdeutsch.com');
 

  await page.setViewport({width: 1100, height: 600})
  await page.screenshot({path: 'nd-wide.png'});
  await page.setViewport({width: 800, height: 600})
  await page.screenshot({path: 'nd-mid.png'});
  await page.setViewport({width: 320, height: 600})
  await page.screenshot({path: 'nd-mobile.png'});

  await browser.close();
}

getPic()