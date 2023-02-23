import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import time
import random

CHROME_DRIVER_PATH = os.environ.get('PATH')
SIMILAR_ACCOUNT = os.environ.get('SIMILAR_ACCOUNT')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


class InstaFollower:

    def __init__(self, path):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(path), options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(6)
        modal = self.driver.find_element(By.CSS_SELECTOR, "._aano div div button")
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

        for _ in range(100):
            modal.send_keys(Keys.PAGE_DOWN)
            time.sleep(random.randint(3,9)/10)

    def follow(self):
        # all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano div div button")
        # print(all_buttons)
        time.sleep(2)
        for button in all_buttons:
            try:
                button.click()
                time.sleep(random.randint(1, 8))
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[text()='Cancel']")
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

input("Press Enter to close the driver window...")

