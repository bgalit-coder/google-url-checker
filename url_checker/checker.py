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
import tldextract

# Function to extract the site name (registrable domain's SLD) from any URL
# Example: https://news.google.co.uk -> "google"
def extract_keyword_from_url(url):
    extracted = tldextract.extract(url)
    # extracted.domain gives the SLD (second-level domain) which is stable across TLDs and subdomains
    return extracted.domain or ""

# Main function to check URL and save results
def check_url(url):
    # Extract site name from input URL
    input_site_name = extract_keyword_from_url(url)

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
    # Extract site name from final URL after redirects
    final_site_name = extract_keyword_from_url(current_url)

    # Close the browser
    driver.quit()

    # Validate that the site names (input vs final) match exactly
    is_valid = (input_site_name.lower() == final_site_name.lower()) if input_site_name and final_site_name else False

    # Determine output file path (defaults to project root)
    output_file_path = os.getenv("OUTPUT_FILE", "final_url.txt")

    # Ensure parent directory exists if a path is provided with directories
    output_dir = os.path.dirname(output_file_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Write only the current URL to the file as per assignment
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(current_url)

    print(f"URL check completed. Current URL saved to {output_file_path}.")

    return current_url, is_valid, input_site_name, final_site_name
