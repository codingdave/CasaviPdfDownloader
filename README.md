# CasaviPdfDownloader

Download your pdfs from casavi

## Intro

Backing up the documents from Casavi can be frustrating and error prone, as this portal doesn't provide a way to download all the files in an automated fashion. This script is doing the job by emulating a human who clicks on every link one after another and fixes the filename.

## Setup

You need some software installed and some personal information set up, before the script can act.

### Dependencies

- Make sure you have python installed
- Make sure you have a version of ChromeDriver downloaded and unpacked

### Steps

- Copy credentials-example.py to credentials.py
- Insert the url of the login page
- Login with the browser and find out the basedir of your documents. Add this url to documents_url.
- Insert your username and password
- Change chrome_driver_path to the binary of the chrome driver
- Optionally change the target directory of downloaded pdfs

### Run

- Open a commandline and navigate into this directory
- verify that python is installed `python3 --version`
- if that worked flawless, you can run the application by calling `python run.py`