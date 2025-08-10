# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib.parse

# Function to extract main keyword (domain name part) from URL
def extract_keyword_from_url(url):
    # Parse the URL
    parsed = urllib.parse.urlparse(url)
    hostname = parsed.hostname or ""
    parts = hostname.split(".")
    # Filter out common subdomains and TLDs to get the main domain part
    common = {"www", "com", "org", "net", "co", "il"}
    filtered = [part for part in parts if part not in common]
    # Return the first filtered part or empty string if none found
    return filtered[0] if filtered else ""

# Main function to check URL and save results
def check_url(url):
    # Extract keyword from input URL
    keyword = extract_keyword_from_url(url)

    # Set Chrome options for headless browsing
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the given URL
    driver.get(url)

    # Wait for the page body to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get the current URL after all redirections
    current_url = driver.current_url

    # Close the browser
    driver.quit()

    # Check if the extracted keyword is in the current URL (case-insensitive)
    is_valid = keyword.lower() in current_url.lower()

    # Prepare the result text to write to file
    result = (
        f"Input URL: {url}\n"
        f"Current URL: {current_url}\n"
        f"Extracted keyword: {keyword}\n"
        f"Contains keyword: {is_valid}\n"
    )

    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Write the result to a file
    with open("output/url.txt", "w", encoding="utf-8") as f:
        f.write(result)

    # Print confirmation message
    print("URL check completed. Result saved to output/url.txt.")
