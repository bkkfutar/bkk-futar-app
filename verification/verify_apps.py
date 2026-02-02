from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # 1. Verify Root Dashboard
        print("Verifying Dashboard...")
        page.goto("http://localhost:8000/index.html")
        page.wait_for_selector("h1") # Wait for title
        page.screenshot(path="verification/dashboard.png")
        print("Dashboard screenshot saved.")

        # 2. Verify Planner App
        print("Verifying Planner App...")
        page.goto("http://localhost:8000/planner/index.html")
        page.wait_for_load_state("networkidle") # Wait for map and resources
        # Check title
        if "BKK Tervező" not in page.title():
            print(f"Error: Planner title mismatch. Got: {page.title()}")
        page.screenshot(path="verification/planner.png")
        print("Planner screenshot saved.")

        # 3. Verify Driver App
        print("Verifying Driver App...")
        page.goto("http://localhost:8000/driver/index.html")
        page.wait_for_load_state("networkidle")
        if "BKK Vezető" not in page.title():
             print(f"Error: Driver title mismatch. Got: {page.title()}")

        # In Driver app, we expect the map initially (selection screen)
        # Let's try to simulate clicking a vehicle if any exist (might be empty if no API key or mock data)
        # But for now just screenshot the initial state
        page.screenshot(path="verification/driver_initial.png")
        print("Driver initial screenshot saved.")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    run()
