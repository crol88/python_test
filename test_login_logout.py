# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from group import Group


class TestAddNewPatient(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_add_new_patient(self):
        self.open_homepage()
        self.login(username="Директор1", password="123456")
        self.open_cbase()
        self.open_form_newclient()
        self.add_key()
        self.fill_newclient_form(Group(surname="ФамилияАвтоТест", name="Имя", secondname="Отчество",
                                 datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
        self.submit_newpatient_creation()

    def test_empty_clientdata(self):
        self.open_homepage()
        self.login(username="Директор1", password="123456")
        self.open_cbase()
        self.open_form_newclient()
        self.add_key()
        self.fill_newclient_form(Group(surname="", name="", secondname="",
                                 datapicker="", phone="", fromwhere=""))
        self.submit_newpatient_creation()

    def open_homepage(self):
        self.driver.get("https://betav10.ci.dental-pro.online/")
        self.driver.set_window_size(1920, 1080)

    def login(self, username, password):
        self.driver.find_element(By.ID, "form_user_loginhtml_input_0_login").send_keys(username)
        self.driver.find_element(By.ID, "form_user_loginhtml_password_0_password").send_keys(password)
        self.driver.find_element(By.ID, "form_user_loginhtml_button_1_button").click()

    def open_cbase(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]")))
        self.driver.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]").click()

    def open_form_newclient(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]")))
        self.driver.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]").click()

    def add_key(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]")))
        self.driver.find_element(By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]").click()

    def fill_newclient_form(self, group):
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys(group.surname)
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys(group.name)
        self.driver.find_element(By.XPATH,
                                 "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").send_keys(
            group.secondname)
        self.driver.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(
            group.datapicker)
        self.driver.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        self.driver.find_element(By.XPATH, "//*[@id='select2-chosen-9']").click()
        self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys(group.fromwhere)
        self.driver.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys(Keys.ENTER)

    def submit_newpatient_creation(self):
        self.driver.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/a").click()

    def teardown_method(self, method):
        self.driver.quit()
