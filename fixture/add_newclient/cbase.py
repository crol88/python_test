# -*- coding: utf-8 -*-
import time
import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from model.group import Group
import random
import pathlib


class CbaseHelper:

    def __init__(self, app):
        self.app = app

    def open_form_newclient(self):
        # Открыть список пациентов
        self.open_cbase()
        self.push_button_newclient()

    def open_cbase(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            # if len(wd.find_elements(By.LINK_TEXT, "Сбросить")) != 0:
            #     wd.find_element(By.LINK_TEXT, "Сбросить").click()
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    def open_cbase_temp(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
        time.sleep(1)
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
        self.push_button_newclient()

    def select_all_filial(self, filial):
        wd = self.app.wd
        select = Select(wd.find_element(By.XPATH, "//*[@class='company-switch-wrapper']/select"))
        select.select_by_visible_text(filial)
        selected = wd.find_element(By.XPATH, "//*[@class='company-switch-wrapper']//*[@class='select2-chosen']").text
        print("Выбранный филиал:", selected)
        assert filial == selected

    # def select_filial(self, group):
    #     wd = self.app.wd
    #     wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
    #     wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
    #     wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
    #     time.sleep(2)

    @allure.step("Нажать 'Добавить пациента'")
    def push_button_newclient(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        element = wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    @allure.step("Заполнить форму создания нового пациента")
    def fill_newclient_form(self, group):
        wd = self.app.wd
        # Заполнить обязательные поля ввода валидными данными
        with allure.step(f"Ввести фамилию: {group.surname}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys(group.surname)
        with allure.step(f"Ввести имя: {group.name}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys(group.name)
        with allure.step(f"Ввести отчество: {group.secondname}"):
            wd.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").\
                send_keys(group.secondname)
        with allure.step(f"Ввести дату рождения: {group.birthday}"):
            wd.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(group.birthday)
        with allure.step(f"Ввести телефон: {group.phone}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        with allure.step(f"Выбрать 'Откуда о нас узнали': {group.fromwhere}"):
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
            group.birthday)
        wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        wd.find_element(By.XPATH, "//*[text()='Откуда о нас узнали']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.fromwhere)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()

    @allure.step("Подтвердить ввод данных")
    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        with allure.step("Нажать 'Далее'"):
            if wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']") == 0:
                wd.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        if len(wd.find_elements(By.XPATH, "//*[@role='alert']")) > 0:
            alert_obj = wd.find_element(By.XPATH, "//*[@role='alert']")
            msg = alert_obj.text
            print(msg)
            name = str(datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + '.png')
            capture_path = str(pathlib.Path.cwd() / 'screenshots' / name)
            wd.save_screenshot(capture_path)
            wd.find_element(By.XPATH, "//*[@class='modalClose']").click()
        with allure.step("Нажать 'Готово'"):
            wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()
            time.sleep(2)

    def delete_new_patient(self, search_name):
        wd = self.app.wd
        self.search_patient(search_name)
        wd.find_element(By.XPATH, "//*[@class='col-md-8 text-right pageActions']/div[2]/div[1]").click()
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

    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def check_basic_info(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Основная информация")) == 0:
            return

    def add_patient(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        self.push_button_newclient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    @allure.step("Открыть список пациентов")
    def count(self, check_patient):
        wd = self.app.wd
        with allure.step(f"Проверить с списке наличие пациента: {check_patient}"):
            if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
                b = wd.find_element(By.XPATH,
                                    "//*[@alt='Пациенты']/parent::div/parent::div/parent::div").get_attribute("class")
                if str(b) == "link subMenuOpen active":
                    wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
                wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
                wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
            return len(wd.find_elements(By.LINK_TEXT, check_patient))

    @allure.step("Если пациент не найден")
    def add_patient_for(self, group):
        # wd = self.app.wd
        # with testit.step('Изменить филиал, если указан'):
        #     if group.filial is not None:
        #         wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
        #         wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
        #         wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newclient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    group_cache = None

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

    def get_patient_list(self):
        wd = self.app.wd
        self.open_cbase()
        # patient_list = []
        # for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr"):
        #     patient = element.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[2]/a").text
        #     print(patient)
        # return list(patient_list)
        patient_list = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//tr/td[2]/a")
        names = [e.text for e in patient_list]
        assert len(patient_list) > 0
        print('Кол-во пациентов:', len(names))
        return names

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
        print("Фактический результат *", filial.text)
        print("Ожидаемый результат *", "Пациент обслуживается: не прикреплен к филиалам")
        assert filial.text == "Пациент обслуживается: не прикреплен к филиалам"

    def check_empty_surname(self):
        wd = self.app.wd
        surname_field = wd.find_element(By.XPATH, "//*[@id='js-newrec-surname']/following-sibling::span").text
        field = wd.find_element(By.XPATH, "//*[@for='js-newrec-surname']").text
        form_error = wd.find_elements(By.XPATH, "//*[@class='form-group has-error']/*[@for='js-newrec-surname']")
        print(field, surname_field)
        assert len(form_error) != 0
        assert surname_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def check_empty_name(self):
        wd = self.app.wd
        name_field = wd.find_element(By.XPATH, "//*[@id='js-newrec-name']/following-sibling::span").text
        field = wd.find_element(By.XPATH, "//*[@for='js-newrec-name']").text
        form_error = wd.find_elements(By.XPATH, "//*[@class='form-group has-error']/*[@for='js-newrec-name']")
        print(field, name_field)
        assert len(form_error) != 0
        assert name_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def check_empty_secondname(self):
        wd = self.app.wd
        name_field = wd.find_element(By.XPATH, "//*[@name='wizard[data][second_name]']/following-sibling::span").text
        field = wd.find_element(By.XPATH,
                                "//*[@for='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").text
        form_error = wd.find_elements(By.XPATH,
                                      "//*[@for='form_cbase_admin_newClient_input_0_wizard[data][second_name]']")
        print(field, name_field)
        assert len(form_error) != 0
        assert name_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def check_empty_birthday(self):
        wd = self.app.wd
        name_field = wd.find_element(By.XPATH, "//*[@class='datepicker-group']/following-sibling::span").text
        field = wd.find_element(By.XPATH, "//*[@for='form_cbase_admin_newClient_date_0_']/parent::div").text
        form_error = wd.find_elements(By.XPATH, "//*[@class='form-group has-error']"
                                                "/*[@for='form_cbase_admin_newClient_date_0_']")
        print(field)
        assert len(form_error) != 0
        assert name_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def check_empty_phone(self):
        wd = self.app.wd
        name_field = wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']/following-sibling::span").text
        field = wd.find_element(By.XPATH, "//*[@for='js-newrec-phone']").text
        form_error = wd.find_elements(By.XPATH, "//*[@class='form-group has-error']/*[@for='js-newrec-phone']")
        print(field, name_field)
        assert len(form_error) != 0
        assert name_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def check_empty_fromwhere(self):
        wd = self.app.wd
        name_field = wd.find_element(By.XPATH, "//*[@name='wizard[data][id_fromwhere]']/following-sibling::span").text
        field = wd.find_element(By.XPATH, "//*[@for='form_cbase_admin_newClient_select_0_']").text
        form_error = wd.find_elements(By.XPATH, "//*[@class='form-group has-error']"
                                                "/*[@for='form_cbase_admin_newClient_select_0_']")
        print(field, name_field)
        assert len(form_error) != 0
        assert name_field == "Поле обязательное для заполнения."
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def empty_patient_list(self):
        wd = self.app.wd
        alert = wd.find_element(By.XPATH, "//*[@class='alert alert-info']").text
        status = wd.find_element(By.XPATH, "//*[@class='info']").text
        print("Результат запроса:", alert)
        print("Список пациентов:", status)
        assert status == "Ничего не найдено"
        assert alert == "По вашему запросу ничего не найдено, попробуйте изменить параметры поиска."
