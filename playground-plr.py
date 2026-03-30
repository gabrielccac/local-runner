import sys
from playwright.sync_api import sync_playwright

def get_title(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        print(f"Title of {url}: {page.title()}")
        browser.close()

if __name__ == "__main__":
    # Check if a URL was passed as a command-line argument
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "https://example.com"  # Fallback default
        
    get_title(target)