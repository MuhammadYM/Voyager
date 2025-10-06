from pyppeteer import launch
import asyncio
import config

url = "https://www.google.com"

async def scrape_reviews(url):
    browser = await launch({
        "headless": False, 
        "args": ["--window-size=800,3200"]
    })
    
    try:
        page = await browser.newPage()
        await page.setViewport({"width": 800, "height": 3200})
        await page.goto(url)
        
        # Add a delay to keep the browser open
        print("Browser opened successfully! Press Ctrl+C to close.")
        await asyncio.sleep(10)  # Keep open for 10 seconds
        
    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_reviews(url))

