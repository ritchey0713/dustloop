// guilty gear urls 

// const URLS = [
//   'https://www.dustloop.com/w/GGST/Testament',
//   'https://www.dustloop.com/w/GGST/Jack-O',

// ]
import axios from 'axios';
import puppeteer from 'puppeteer';

const baseURL = 'https://www.dustloop.com/w/GGST'

const browser = await puppeteer.launch({
  headless: false,
  defaultViewport: null,
});

// open a new page
const page = await browser.newPage();

const run = async () => {
  // what do to do on page?
  await page.goto(baseURL, {
    waitUntil: 'domcontentloaded',
  });

  const urls = await getGGSTURLS();
  console.log(urls);
};

const getGGSTURLS = async () => {
  await page.evaluate(async () => {
    const links = document.querySelector('.add-hover-effect').children[0].children
    for (let ele of links) {
      await page.goto(ele.href, {
        waitUntil: 'domcontentloaded'
      })

    };
  });
};


run();
