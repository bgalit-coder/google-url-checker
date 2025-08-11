# Google URL Checker
This project is a simple, generic test automation solution that:
- Opens a Chrome browser
- Navigates to a user-provided URL (or defaults to https://www.google.com)
- Captures the current page URL
- Extracts the site name (registrable domain) from both the input URL and the final URL after redirects
- Validates that both site names match exactly
- Writes the final URL to a file saved in the project directory (host system if using Docker)

🧰 Tools Used
- Python 3.11
- Selenium for browser automation
- ChromeDriver via webdriver-manager
- tldextract for robust domain parsing across TLDs and subdomains
- Docker for isolated and portable test execution

📁 Project Structure
google-url-checker/         # Project's root directory
│
├── url_checker/
│   ├── __init__.py
│   └── checker.py           # Contains logic to check URL, extract site, and write to file
│
├── test_failed\passed_`<keyword>`.txt# File with the final URL saved to root directory    
│
├── main.py                  # Entrypoint script to run the test
├── requirements.txt         # Project dependencies
├── Dockerfile               # Docker build instructions
└── README.md                # This file

🚀 Run locally

1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run the script directly (optional)
python main.py https://www.wikipedia.org
If no URL is provided, it defaults to https://www.google.com.


🐳 Run in Docker

1. Build the Docker image
docker build -t google-url-checker .

2. Run the container with a test URL input and save output to host (Bonus)
# macOS/Linux
docker run --rm -e TEST_URL=https://www.wikipedia.org -v "`<Project root Path>`:/app" google-url-checker

# Windows PowerShell
docker run --rm -e TEST_URL=https://www.wikipedia.org -v `<Project root Path>`:/app google-url-checker

3. View the output
Check test_failed\passed_<keyword>.txt on your host machine.


🏁 Notes
- Provide the test URL via TEST_URL env var, or pass it as a CLI arg: `docker run --rm google-url-checker https://www.wikipedia.org`.
- Optionally override the output filename via OUTPUT_FILE env var. By default, the file will be written in the project root inside the container (mounted to host when volume is used).
