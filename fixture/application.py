from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://betav10.ci.dental-pro.online/")
        wd.set_window_size(1920, 1080)

    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        wd.find_element(By.ID, "form_user_loginhtml_input_0_login").send_keys(username)
        wd.find_element(By.ID, "form_user_loginhtml_password_0_password").send_keys(password)
        wd.find_element(By.ID, "form_user_loginhtml_button_1_button").click()

    def open_cbase(self):
        wd = self.wd
        element = WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]")))
        wd.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]").click()

    def open_form_newclient(self):
        wd = self.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]")))
        wd.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]").click()

    def add_key(self):
        wd = self.wd
        element = WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]")))
        wd.find_element(By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]").click()

    def fill_newclient_form(self, group):
        wd = self.wd
        self.open_cbase()
        self.open_form_newclient()
        self.add_key()
        wd.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys(group.surname)
        wd.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys(group.name)
        wd.find_element(By.XPATH,
                        "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").send_keys(
            group.secondname)
        wd.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(
            group.datapicker)
        wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        wd.find_element(By.XPATH, "//*[@id='select2-chosen-9']").click()
        wd.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys(group.fromwhere)
        wd.find_element(By.XPATH, "//*[@id='s2id_autogen9_search']").send_keys(Keys.ENTER)

    def submit_newpatient_creation(self):
        wd = self.wd
        wd.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/button").click()
        wd.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/a").click()

    def destroy(self):
        wd = self.wd
        wd.quit()
