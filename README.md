# Google URL Checker
This project is a simple, generic test automation solution that:
- Opens a Chrome browser
- Navigates to a user-provided URL (or defaults to https://www.google.com)
- Captures the current page URL
- Validates that the URL contains a specific substring (extracted from the domain)
- Writes the final URL to a file saved in the project directory (host system if using Docker)

🧰 Tools Used
- Python 3.11
- Selenium for browser automation
- ChromeDriver via webdriver-manager
- Pytest for future test scalability
- Docker for isolated and portable test execution

📁 Project Structure
google-url-checker/
│
├── url_checker/
│   ├── __init__.py
│   └── checker.py           # Contains logic to check URL and write to file
│
├── output/
│   └── final_url.txt        # Output file written after test run
│
├── main.py                  # Entrypoint script to run the test
├── requirements.txt         # Project dependencies
├── Dockerfile               # Docker build instructions
└── README.md                # This file

🚀 Run the project locally

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/google-url-checker.git
cd google-url-checker

2. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the script with a custom URL
python main.py https://www.wikipedia.org
If no URL is provided, it defaults to https://www.google.com.

🐳 Run the project in Docker

1. Build the Docker image
docker build -t google-url-checker .

2. Run the container with optional URL
docker run --rm -v "${PWD}/output:/app/output" google-url-checker https://www.wikipedia.org
💡 On Windows (PowerShell):

docker run --rm -v ${PWD}\output:/app/output google-url-checker https://www.wikipedia.org

3. View the output
After running, check the output/final_url.txt file in your local project folder.

📈 Scalability and Future Improvements
If given more time, I would:
Handle more validations (e.g., page title, content checks)

Add support for multiple URLs and parallel execution

Include logging and HTML reporting and handle errors

🧠 Why These Tools?
- Python: Clear syntax and strong community for testing
- Selenium: Browser automation standard
- WebDriver Manager: Simplifies ChromeDriver management
- Docker: Ensures consistent environment and easy portability
- Project structure: Encourages modularity, maintainability, and scalability

🏁 Bonus – Saving Output to Host
This is done using Docker's volume mounting:

-v "${PWD}/output:/app/output"
It maps the container’s /app/output directory to your local machine’s output directory.
