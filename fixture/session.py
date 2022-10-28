# -*- coding: utf-8 -*-
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element(By.ID, "form_user_loginhtml_input_0_login").send_keys(username)
        wd.find_element(By.ID, "form_user_loginhtml_password_0_password").send_keys(password)
        wd.find_element(By.ID, "form_user_loginhtml_button_1_button").click()

    def logout(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//*[@class='modalClose']")) != 0:
            wd.find_element(By.XPATH, "//*[@class='modalClose']").click()
        # wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        # wd.find_element(By.XPATH, "//*[@class='sidebar-content-container']").send_keys(Keys.HOME)
        # element = wd.find_element(By.XPATH, "//*[@class='userHeading']")
        # wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='userHeading']").click()
        wd.find_element(By.XPATH, "//*[@onclick='user.logout();']").click()
