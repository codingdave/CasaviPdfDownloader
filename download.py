"""

https://github.com/codingdave/CasaviPdfDownloader

This script automates the process of logging into a website, navigating to a documents page, 
and downloading PDF files using Selenium and Requests libraries.
Modules:
- selenium: Used for browser automation.
- credentials: Contains login credentials and URLs.
- os: Provides functions for interacting with the operating system.
- requests: Used for HTTP requests to download files.
- time: Used for adding delays.
Workflow:
1. Load login credentials and URLs from the `credentials` module.
2. Set up Chrome WebDriver with headless mode (optional).
3. Navigate to the login page and perform login using provided credentials.
4. Navigate to the documents page after successful login.
5. Interact with the page to reveal PDF links.
6. Extract PDF links and download each file using HTTP requests.
7. Save the downloaded PDFs to the specified directory.
Attributes:
- login_url (str): URL of the login page.
- documents_url (str): URL of the documents page.
- username (str): Username for login.
- password (str): Password for login.
- chrome_driver_path (str): Path to the ChromeDriver executable.
- download_dir (str): Directory where downloaded PDFs will be saved.
Functions:
- None explicitly defined; the script executes sequentially.
Notes:
- Ensure that the `credentials` module contains the required attributes: `login_url`, `documents_url`, `username`, and `password`.
- The script uses cookies from Selenium's WebDriver to authenticate HTTP requests for downloading files.
- The ChromeDriver path must be correctly set to match your system configuration.
- The script assumes that the PDF links are revealed after interacting with specific elements on the page.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import credentials
import os
import requests
import time

username = credentials.username
password = credentials.password
login_url = credentials.login_url
documents_url = credentials.documents_url
chrome_driver_path = os.path.expandvars(credentials.chrome_driver_path)
download_dir = credentials.download_dir

# create download directory if it does not exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create WebDriver instance
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Retrieve the login page
driver.get(login_url)

# Wait for the page to fully load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

# Find and fill in the login credentials
username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-in"]')

username_field.send_keys(username)
password_field.send_keys(password)

# Click on the submit button
submit_button.click()

# Wait for the login to complete
time.sleep(1)

# Navigate to the documents page
driver.get(documents_url)

# Wait for the page to fully load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.clickable.box-subhead--title.dashboard-tile-company-background')))

# Interact with the page to reveal the PDF links
folders = driver.find_elements(By.CSS_SELECTOR, 'div.clickable.box-subhead--title.dashboard-tile-company-background')
for folder in folders:
    folder.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/api/v1/communities/213519/documents/"]')))

# Extract PDF links
pdf_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/api/v1/communities/213519/documents/"]')

# Download and save the PDFs
for link in pdf_links:
    pdf_url = link.get_attribute('href')
    pdf_name = os.path.join(download_dir, link.text.strip().replace(' ', '_'))
    
    # Ensure that the file extension .pdf is present
    if not pdf_name.endswith('.pdf'):
        pdf_name += '.pdf'
    
    # Download the PDF file
    cookies = driver.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    
    response = session.get(pdf_url, stream=True)
    if response.status_code == 401:
        print("Not authenticated")
        continue
    
    with open(pdf_name, 'wb') as pdf_file:
        for chunk in response.iter_content(chunk_size=8192):
            pdf_file.write(chunk)
    
    print(f"Downloaded {pdf_name}")

# Close the browser
driver.quit()

print("All PDFs downloaded successfully.")