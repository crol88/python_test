from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from model.basic import Basic
import time


class BasicHelper:

    def __init__(self, app):
        self.app = app

    basic_cache = None

    def get_basic_patient_info_after_edit(self):
        wd = self.app.wd
        self.search_patient(search_name="ТЕСТ-Добавить")
        self.open_field_basic_patient_info()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']//input").get_attribute("value")
        name = wd.find_element(By.XPATH, "//*[@id='name']//input").get_attribute("value")
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']//input").get_attribute("value")
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']//input").get_attribute("value")
        return Basic(surname=surname, name=name, secondname=secondname, birthday=birthday)

    def get_basic_patient_info(self):
        if self.basic_cache is None:
            wd = self.app.wd
            # self.search_patient(search_name)
            self.open_field_basic_patient_info()
            self.basic_cache = []
            for row in wd.find_elements(By.XPATH, "//*[@id='collapseOne']"):
                cells = row.find_elements(By.TAG_NAME, "p")
                surname = cells[0].text
                name = cells[1].text
                secondname = cells[2].text
                birthday = cells[3].text
                self.basic_cache.append(Basic(surname=surname, name=name, secondname=secondname, birthday=birthday))
        return list(self.basic_cache)

    def search_patient(self, search_name):

        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def open_field_basic_patient_info(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()

    def edit_patient_surname(self, basic, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='surname']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='surname']//input").send_keys(basic.surname)
        wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p")
        assert (text, surname.text)

