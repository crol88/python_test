# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_login(self):
        # open homepage
        self.driver.get("https://betav10.ci.dental-pro.online/")
        self.driver.set_window_size(1920, 1080)
        # login
        self.driver.find_element(By.ID, "form_user_loginhtml_input_0_login").send_keys("Директор1")
        self.driver.find_element(By.ID, "form_user_loginhtml_password_0_password").send_keys("123456")
        self.driver.find_element(By.ID, "form_user_loginhtml_button_1_button").click()
        # open cbase
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]")))
        self.driver.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]").click()
        # open form newclient
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]")))
        self.driver.find_element(By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]").click()
        # fill newclient form
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys("ФамилияАвтоТест")
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys("Имя")
        self.driver.find_element(By.XPATH,
                                 "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").send_keys(
            "Отчество")
        self.driver.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(
            "10102010")
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys("79278889966")
        self.driver.find_element(By.XPATH, "//*[@id='select2-chosen-9']").click()
        self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys("2ГИС")
        self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys(Keys.ENTER)
        # submit new patient creation
        self.driver.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/a").click()

    def teardown_method(self, method):
        self.driver.quit()
