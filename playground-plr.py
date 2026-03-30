import sys
from playwright.sync_api import sync_playwright

def get_title(url):
    # The function now assumes it has a valid-ish string
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url)
            print(f"Title of {url}: {page.title()}")
        except Exception as e:
            print(f"Failed to load {url}: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    # Handle ALL default logic here
    # 1. Check if argument exists
    # 2. Check if argument is an empty string (GitHub 'push' event quirk)
    target = "https://www.google.com" # Define the default once
    
    if len(sys.argv) > 1 and sys.argv[1].strip():
        target = sys.argv[1]
    else:
        print(f"No valid URL provided. Using default: {target}")

    get_title(target)