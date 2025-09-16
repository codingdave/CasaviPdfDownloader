# Howto
# - rename this file to credentials.py
# - add your username and password
# - add the path to your ChromeDriver
# - run the script with `run.py`

login_url = 'https://my.casavi.com/app/login'
documents_url = 'https://my.casavi.com/app/c/213519/info/documents'

# add your username and password here
username = 'xxx'
password = 'yyy'

# download the ChromeDriver from:
# https://developer.chrome.com/docs/chromedriver/downloads
# add the path to your ChromeDriver here
chrome_driver_path = '${HOME}/Downloads/chromedriver-mac-arm64/chromedriver'

download_dir = './DownloadedFiles'  # Directory to save downloaded PDFs