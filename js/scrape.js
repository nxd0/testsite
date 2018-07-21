const puppeteer = require('puppeteer');

let scrape = async () => {
    const browser = await puppeteer.launch({headless: true});
    const page = await browser.newPage();

    await page.goto('http://noahdeutsch.com/');
    await page.waitFor(2000);

    const result = await page.evaluate(() => {
        let title = document.querySelector('html').innerHTML;

        return {
            title
        }

    });

    browser.close();
    return result;
};

scrape().then((value) => {
    console.log(value); // Success!
});