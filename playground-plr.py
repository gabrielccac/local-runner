from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launching headless (standard for VPS)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        target_url = "https://example.com"
        print(f"Navigating to {target_url}...")
        
        page.goto(target_url)
        title = page.title()
        
        print(f"--- Success! ---")
        print(f"Page Title: {title}")
        
        browser.close()

if __name__ == "__main__":
    run()