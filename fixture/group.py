from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase(self):
        wd = self.app.wd
        # WebDriverWait(wd, 20).until(
            # EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]")))
        wd.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[1]").click()

    def open_form_newclient(self):
        wd = self.app.wd
        # WebDriverWait(wd, 20).until(
            # EC.element_to_be_clickable((By.LINK_TEXT, "Список пациентов")))
        # wd.find_element(By.XPATH, "//*[@id='menu-content']/div[2]/div/nav/div[5]/div[2]/a[4]").click()
        wd.find_element(By.LINK_TEXT, "Список пациентов").click()

    def push_add_key(self):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]")))
        wd.find_element(By.XPATH, "//*[@id='main-container']/div[1]/div/a[4]").click()

    def change_filial(self, filial):
        wd = self.app.wd
        WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='s2id_autogen2']/a")))
        wd.find_element(By.XPATH, "//*[@id='s2id_autogen2']/a").click()
        wd.find_element(By.XPATH, "//*[@id='s2id_autogen3_search']").send_keys(filial)
        wd.find_element(By.XPATH, "//*[@id='s2id_autogen3_search']").send_keys(Keys.ENTER)

    def fill_newclient_form(self, group):
        wd = self.app.wd
        self.open_cbase()
        self.open_form_newclient()
        self.push_add_key()
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
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/button").click()
        wd.find_element(By.XPATH, "//*[@id='js-wizard-form']/div[2]/div[1]/a").click()
