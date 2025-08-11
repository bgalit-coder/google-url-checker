# Import necessary modules
import sys
from url_checker.checker import check_url

# Use default URL if none is provided
if len(sys.argv) < 2:
    print("No URL provided. Using default: https://www.google.com")
    url = "https://www.google.com"
else:
    # Use the user-provided URL
    url = sys.argv[1]

# Run the URL check logic
current_url, is_valid, input_site_name, final_site_name = check_url(url)

# Validate and exit with proper status code
if not is_valid:
    print(f"Validation failed: site mismatch. input='{input_site_name}', final='{final_site_name}'")
    raise SystemExit(1)
