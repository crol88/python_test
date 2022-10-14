# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CbaseFilterHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase_filter(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='headingOne']//div[@role='button']").click()

    def check_filter_status(self):
        wd = self.app.wd
        filter_status = wd.find_element(By.XPATH, "//*[@role='tabpanel']").get_attribute("aria-expanded")
        print("filter_status =", filter_status)
        assert filter_status == "true"

    def fill_surname_filter(self, surname):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
            .send_keys(surname)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        filter_result = wd.find_element(By.XPATH, "//*[@class='table table-clients-list']//td[2]").text
        print("surname=", surname, ";", "filter_result=", filter_result)
        assert surname == filter_result

    def fill_name_filter(self, name):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
            .send_keys(name)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        filter_result = wd.find_element(By.XPATH, "//*[@class='table table-clients-list']//td[3]").text
        print("name=", name, ";", "filter_result=", filter_result)
        assert name == filter_result

    def fill_secondname_filter(self, secondname):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_input_0_display_name']") \
            .send_keys(secondname)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        filter_result = wd.find_element(By.XPATH, "//*[@class='table table-clients-list']//td[4]").text
        print("secondname=", secondname, ";", "filter_result=", filter_result)
        assert secondname == filter_result

    def fill_birthday_filter(self, birthday):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_date_0__visible']") \
            .send_keys(birthday)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()
        time.sleep(2)
        filter_result = wd.find_element(By.XPATH, "//*[@class='table table-clients-list']//td[5]").text
        print("birthday=", birthday, ";", "filter_result=", filter_result)
        assert birthday in filter_result

    def select_sex_filter(self, sex):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='s2id_form_cbase_indexhtml_select_0_']").click()
        select = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_select_0_']"))
        select.select_by_visible_text(sex)
        wd.find_element(By.XPATH, "//*[@class='panel-footer']/button[@type='submit']").click()

    def get_sex_filter_result_female(self):
        wd = self.app.wd
        patient_list = []
        for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody"):
            sex_list = element.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[6]")
            sex = [e.text for e in sex_list]
            print(sex)
            assert "мужской" not in sex
        return list(patient_list)

    def get_sex_filter_result_male(self):
        wd = self.app.wd
        patient_list = []
        for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody"):
            sex_list = element.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[6]")
            sex = [e.text for e in sex_list]
            print(sex)
            assert "женский" not in sex
        return list(patient_list)

    def add_sex_filter(self):
        wd = self.app.wd
        select = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_indexhtml_select_2_']"))
        select.select_by_visible_text("Пол")

