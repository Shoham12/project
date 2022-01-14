from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import chromedriver_binary
import chromedriver_autoinstaller


class e2e:
    def __init__(self):
        self.difficulty = 7

    def test_scores_service(self, url):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # browser = webdriver.Chrome(executable_path="../../Desktop/chromedriver4", options=options)
        # chromedriver_autoinstaller.install()
        # browser = webdriver.Chrome()
        browser = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        browser.get(url)
        # time.sleep(3)
        a = browser.find_element_by_id("score").text
        browser.quit()
        if 1 <= int(a) <= 1000:
            return True
        else:
            return False

    def main_function(self):
        app_url = "http://127.0.0.1:5000/"
        test_func = self.test_scores_service(app_url)
        if not test_func:
            return -1
        else:
            return 0


if __name__ == "__main__":
    print(e2e().main_function())

