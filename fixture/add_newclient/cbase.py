# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from model.group import Group
import testit
import random


class CbaseHelper:

    def __init__(self, app):
        self.app = app

    def open_form_newclient(self):
        # Открыть список пациентов
        self.open_cbase()
        self.push_button_newClient()

    @testit.step('Открыть список пациентов')
    def open_cbase(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    def check_exists_by_xpath(self):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, "//*[@href='/cbase/admin/newClient']")) > 0

    def change_filial(self, group):
        wd = self.app.wd
        # Открыть список пациентов
        self.open_cbase()
        # Изменить филиал
        if group.filial is not None:
            wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newClient()

    def select_all_filial(self, filial):
        wd = self.app.wd
        select = Select(wd.find_element(By.XPATH, "//*[@class='company-switch-wrapper']/select"))
        select.select_by_visible_text(filial)
        selected = wd.find_element(By.XPATH, "//*[@class='company-switch-wrapper']//*[@class='select2-chosen']").text
        print(selected)
        assert filial == selected

    # def select_filial(self, group):
    #     wd = self.app.wd
    #     wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
    #     wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
    #     wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
    #     time.sleep(2)

    @testit.step('Нажать Добавить')
    def push_button_newClient(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    @testit.step('Заполнить форму добавления нового пациента')
    def fill_newclient_form(self, group):
        wd = self.app.wd
        # Заполнить обязательные поля ввода валидными данными
        with testit.step('Заполнить поле Фамилия'):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys(group.surname)
        with testit.step('Заполнить поле Имя'):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys(group.name)
        with testit.step('Заполнить поле Отчество'):
            wd.find_element(By.XPATH,
                            "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").send_keys(
                group.secondname)
        with testit.step('Заполнить поле Дата рождения'):
            wd.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(
                group.birthday)
        with testit.step('Заполнить поле Телефон'):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        with testit.step('Заполнить поле Откуда о нас узнали'):
            wd.find_element(By.XPATH, "//*[text()='Откуда о нас узнали']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.fromwhere)
        with testit.step('Подтвердить ввод данных'):
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
            group.birthday)
        wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        wd.find_element(By.XPATH, "//*[text()='Откуда о нас узнали']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.fromwhere)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    @testit.step('Подтвердить добавление нового пациента')
    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        if wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']") == 0:
            wd.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()
        time.sleep(2)

    @testit.step('Удалить пациента')
    def delete_new_patient(self, search_name):
        wd = self.app.wd
        with testit.step('Найти пациента через глобальный поиск'):
            self.search_patient(search_name)
        with testit.step('Нажать Опции'):
            wd.find_element(By.XPATH, "//*[@class='col-md-8 text-right pageActions']/div[2]/div[1]").click()
        with testit.step('Нажать Удалить'):
            wd.find_element(By.XPATH, "//*[@class='js-client_delete']").click()
            time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()
        self.group_cache = None

    def edit_patient_data(self, group):
        wd = self.app.wd
        # Редактировать фамилию
        if group.surname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@class='form-control']").clear()
            wd.find_element(By.XPATH, "//*[@class='form-control']").send_keys(group.surname)
            wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-basic_info-btn']").click()
        # Редактировать имя
        if group.name is not None:
            wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
            wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-basic_info-btn']").click()
        # Редактировать отчество
        if group.secondname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
            wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-basic_info-btn']").click()
        self.group_cache = None

    @testit.step('Найти пациента через глобальный поиск')
    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        with testit.step('Нажать Поиск по пациентам'):
            wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        with testit.step('Ввести фамилию пациента'):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        with testit.step('Нажать ENTER'):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def check_basic_info(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Основная информация")) == 0:
            return

    @testit.step('Добавить нового пациента')
    def add_patient(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        self.push_button_newClient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    @testit.step('Проверка наличия пациента в cbase')
    def count(self, check_patient):
        wd = self.app.wd
        with testit.step('Открыть список пациентов'):
            if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
                wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
                wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        with testit.step('Если пациент присутствует, вернуться к списку'):
            return len(wd.find_elements(By.LINK_TEXT, check_patient))

    @testit.step('Если пациент отсутствует, добавляем')
    def add_patient_for(self, group):
        wd = self.app.wd
        with testit.step('Изменить филиал, если указан'):
            if group.filial is not None:
                wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
                wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
                wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newClient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    group_cache = None

    @testit.step('Получить список пациентов')
    def get_group_list(self):
        # Проверка списка пациентов
        if self.group_cache is None:
            wd = self.app.wd
            self.open_cbase()
            self.group_cache = []
            for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr"):
                text = element.find_element(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[2]").text
                cbaseid = element.find_element(By.XPATH, "//*[@class='js-client-checkbox']") \
                    .get_attribute("data-client-id")
                self.group_cache.append(Group(name=text, cbaseid=cbaseid))
        return list(self.group_cache)

    @testit.step('Сохранить список пациентов')
    def get_patient_list(self):
        wd = self.app.wd
        self.open_cbase()
        patient_list = []
        for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr"):
            patient_list = element.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[2]")
        return list(patient_list)

    def select_any_patient(self):
        wd = self.app.wd
        patient_list = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//tr/td[2]/a")
        names = [e.text for e in patient_list]
        random_name = random.choice(names)
        element = wd.find_element(By.LINK_TEXT, random_name)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(2)

    def check_filial_info(self):
        wd = self.app.wd
        filial = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']")
        print(filial.text)
        assert filial.text == "Пациент обслуживается: не прикреплен к филиалам"

