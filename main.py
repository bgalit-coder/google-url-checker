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
check_url(url)
