import webbrowser
import time
import os
from selenium import webdriver
import json
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


capabilities = {
                    "browserName": "chrome",
                    "version": "83.0",
                }
options = webdriver.ChromeOptions()
                #options.add_argument('--no-sandbox')
options.headless = True

browser = webdriver.Remote(


                )
