const puppeteer = require('puppeteer');

async function getPic() {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  await page.goto('https://noahdeutsch.com');
  await page.screenshot({path: 'nd.png'});

  await browser.close();
}

getPic();