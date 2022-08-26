from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor:: div[@class='menuLinkLine']").click()

    def open_form_newclient(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    def push_add_key(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    def change_filial(self, filial):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(filial)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        self.open_cbase()
        self.open_form_newclient()
        self.push_add_key()

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
        wd.find_element(By.XPATH, "//*[text()='Откуда о нас узнали']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.fromwhere)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)

    def submit_newpatient_creation(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()

    def delete_new_patient(self):
        wd = self.app.wd
        # Поиск пациента
        wd.find_element(By.XPATH, "//*[@id='clientSearchMenu']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys("АТЕСТ")
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        # Опции
        wd.find_element(By.XPATH, "//*[@class='col-md-8 text-right pageActions']/div[2]/div[1]").click()
        # Удалить
        wd.find_element(By.XPATH, "//*[@class='js-client_delete']").click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
