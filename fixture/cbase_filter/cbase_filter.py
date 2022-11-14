# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CbaseFilterHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase_filter(self):
        wd = self.app.wd
        time.sleep(2)
        if len(wd.find_elements(By.LINK_TEXT, "Отфильтровать")) == 0:
            wd.find_element(By.XPATH, "//*[@id='headingOne']//div[@role='button']").click()
        # filter_status = wd.find_element(By.XPATH, "//*[@role='tabpanel']").get_attribute("aria-expanded")
        # time.sleep(2)
        # if filter_status == "false" or "None":
        #     wd.find_element(By.XPATH, "//*[@id='headingOne']//div[@role='button']").click()
        # print(filter_status)

    def check_filter_status(self):
        wd = self.app.wd
        filter_status = wd.find_element(By.XPATH, "//*[@role='tabpanel']").get_attribute("aria-expanded")
        print("filter_status =", filter_status)
        assert filter_status == "true"

    def fill_surname_filter(self, surname):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']").clear()
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
            .send_keys(surname)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        # wd.find_element(By.XPATH, "//*[.='Отфильтровать']").click()
        time.sleep(1)
        filter_result = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//td[2]/a")
        result_list = [e.text for e in filter_result]
        print("Искомый пациент:", surname, ';', 'Результат поиска:', result_list)
        assert surname in result_list

    def fill_name_filter(self, name):
        wd = self.app.wd
        # wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
        #     .send_keys(name)
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']").clear()
        wd.find_element(By.ID, "form_cbase_indexhtml_input_0_display_name").send_keys(name)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        time.sleep(1)
        filter_result = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//td[3]/a")
        result_list = [e.text for e in filter_result]
        print("Искомый пациент:", name, ';', 'Результат поиска:', result_list)
        assert name in result_list

    def fill_secondname_filter(self, secondname):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
            .send_keys(secondname)
        wd.find_element(By.ID, "form_cbase_indexhtml_input_0_display_name").click()
        time.sleep(1)
        # wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        wd.find_element(By.XPATH, "//*[.='Отфильтровать']").click()
        time.sleep(1)
        filter_result = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//td[4]/a")
        result_list = [e.text for e in filter_result]
        print("Искомый пациент:", secondname, ';', 'Результат поиска:', result_list)
        assert secondname in result_list

    def fill_birthday_filter(self, birthday):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_date_0__visible']") \
            .send_keys(birthday)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        time.sleep(2)
        filter_result = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']//td[5]/a")
        result_list = [e.text[0:-9] for e in filter_result]
        print("birthday=", birthday, ";", "filter_result=", result_list)
        assert birthday in result_list

    def select_sex_filter(self, sex):
        wd = self.app.wd
        time.sleep(1)
        # wd.find_element(By.XPATH, "//*[@id='s2id_form_cbase_indexhtml_select_0_']").click()
        wd.find_element(By.ID, "s2id_form_cbase_indexhtml_select_0_").click()
        # select = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_select_0_']"))
        select = Select(wd.find_element(By.ID, "form_cbase_indexhtml_select_0_"))
        select.select_by_visible_text(sex)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()

    def get_sex_filter_result_female(self):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody")
        sex_list = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[6]/a")
        sex = [e.text for e in sex_list]
        print(sex)
        assert "мужской" not in sex
        return list(sex)

    def get_sex_filter_result_male(self):
        wd = self.app.wd
        time.sleep(1)
        sex_list = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[6]/a")
        sex = [e.text for e in sex_list]
        print(sex)
        assert "женский" not in sex
        return list(sex)

    def add_sex_filter(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='s2id_form_cbase_indexhtml_select_2_']").click()
        select = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_select_2_']"))
        select.select_by_value('sex')
