import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_form_newclient(self):
        wd = self.app.wd
        # Открыть список пациентов
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
        wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        self.push_button_newClient()

    def change_filial(self, filial):
        wd = self.app.wd
        # Открыть список пациентов
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
        wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        # Изменить филиал
        wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(filial)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newClient()

    def push_button_newClient(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    def fill_newclient_form(self, group):
        wd = self.app.wd
        # Заполнить обязательные поля ввода валидными данными
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

    def empty_newclient_form(self, group):
        wd = self.app.wd
        # Оставить поля ввода пустыми
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
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()
        time.sleep(3)

    def delete_new_patient(self, search_name):
        wd = self.app.wd
        # Поиск пациента
        self.search_patient(search_name)
        # Опции
        wd.find_element(By.XPATH, "//*[@class='col-md-8 text-right pageActions']/div[2]/div[1]").click()
        # Удалить пациента
        wd.find_element(By.XPATH, "//*[@class='js-client_delete']").click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()

    def edit_patient_data(self, group):  # create
        wd = self.app.wd
        # Редактировать фамилию
        if group.surname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@class='form-control']").clear()
            wd.find_element(By.XPATH, "//*[@class='form-control']").send_keys(group.surname)
            wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-group-btn']").click()
        # Редактировать имя
        if group.name is not None:
            wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
            wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        # Редактировать отчество
        if group.secondname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
            wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()

    def search_patient(self, search_name):

        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)
