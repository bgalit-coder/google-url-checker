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
- Pytest (with one test case) for scalability and CI-ready execution
- Docker for isolated and portable test execution

📁 Project Structure
google-url-checker/
│
├── url_checker/
│   ├── __init__.py
│   └── checker.py           # Contains logic to check URL, extract site, and write to file
│
├── tests/
│   └── test_url_checker.py  # Pytest test case
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

2. Run the container with optional URL and save output to host (Bonus)
# macOS/Linux
mkdir -p output
docker run --rm -e OUTPUT_FILE=/app/output/final_url.txt -v "${PWD}/output:/app/output" google-url-checker https://www.wikipedia.org

# Windows PowerShell
mkdir output -ea 0
docker run --rm -e OUTPUT_FILE=/app/output/final_url.txt -v ${PWD}\output:/app/output google-url-checker https://www.wikipedia.org

3. View the output
Check output/final_url.txt on your host machine.

📈 Scalability and Future Improvements
- Add page title/content validations and error handling
- Support multiple URLs and parallel execution
- Introduce logging and an HTML report (e.g., pytest-html)
- Add linting (ruff/flake8) and formatting (black) with pre-commit hooks

🧠 Why These Tools?
- Python: readability and strong testing ecosystem
- Selenium: browser automation standard
- WebDriver Manager: auto-manages ChromeDriver
- tldextract: robustly extracts registrable domain across complex TLDs and subdomains
- Pytest: simple structure and scalable for multiple tests
- Docker: consistent environment and easy portability

🏁 Notes
- The output file path is configurable via OUTPUT_FILE env var. By default, the file will be written to final_url.txt in the project root.
