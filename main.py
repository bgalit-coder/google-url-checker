# Import necessary modules
import os
import sys
from url_checker.checker import check_url

# Determine URL precedence: TEST_URL env var > CLI arg > default
env_url = os.getenv("TEST_URL")
cli_url = sys.argv[1] if len(sys.argv) >= 2 else None
url = env_url or cli_url or "https://www.google.com"
if not env_url and not cli_url:
    print("No URL provided. Using default: https://www.google.com")

# Run the URL check logic
current_url, is_valid, input_site_name, final_site_name = check_url(url)

# Validate and exit with proper status code
if not is_valid:
    print(f"Validation failed: site mismatch. input='{input_site_name}', final='{final_site_name}'")
    raise SystemExit(1)
