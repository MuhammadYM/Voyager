from pyppeteer import launch

import asyncio

import config

url = "https://www.google.com"


async def scrape_reviews(url):
    browser = await launch({"headless": False, "args": ["--window-size=800,3200"]})

    page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 3200})
    await page.goto(url)


# Run the function
asyncio.get_event_loop().run_until_complete(scrape_reviews(url))