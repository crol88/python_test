import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import pathlib


class ParentHelper:

    def __init__(self, app):
        self.app = app

    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def open_parent_info(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, "Родитель").click()

    def edit_parent_birthday(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        wd.find_element(By.XPATH, "//*[@data-key='parent_birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_birthday']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_birthday']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_birthday']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_birthday']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def edit_parent_birthday_none(self):
        wd = self.app.wd
        self.open_parent_info()
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_birthday']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_birthday']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_birthday']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def edit_parent_name(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        wd.find_element(By.XPATH, "//*[@data-key='parent_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_name']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_name']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_name']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_name']/p").text
        print("enter_name =", enter_value, ";", "save_name =", save_value)
        assert enter_value == save_value

    def edit_parent_name_none(self):
        wd = self.app.wd
        self.open_parent_info()
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_name']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_name']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_name']/p").text
        print("enter_name =", enter_value, ";", "save_name =", save_value)
        assert enter_value == save_value

    def edit_parent_passport_number(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_number'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_number']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_number']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_passport_number']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_number']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def edit_parent_passport_number_none(self):
        wd = self.app.wd
        self.open_parent_info()
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_number']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_number'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_number']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_number']/p").text
        print("save_value =", save_value, ";", "enter_value =", enter_value)
        assert save_value == enter_value

    def parent_passport_unit_code(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        edit = wd.find_element(By.XPATH, "//*[@data-key='passport_unit_code'][@type='button']")
        time.sleep(1)
        wd.execute_script("arguments[0].scrollIntoView();", edit)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='passport_unit_code'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//input").send_keys(enter_value)
        save = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//span[@class='input-group-btn']")
        time.sleep(1)
        wd.execute_script("arguments[0].scrollIntoView();", save)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_passport_unit_code_none(self):
        wd = self.app.wd
        self.open_parent_info()
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_unit_code'][@type='button']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//div[@id='passport_unit_code']//button").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_passport_when(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_when'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_when']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_when']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_passport_when']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_when']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_passport_when_none(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_passport_when")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_when']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_when'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_when']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_when']/p").text
        print("save_value =", save_value, ";", "enter_value =", enter_value)
        assert enter_value == save_value

    def parent_passport_who(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_who'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_who']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_who']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_passport_who']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_who']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_passport_who_none(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_passport_who")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_who']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_passport_who'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_passport_who']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_passport_who']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_secondname(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_secondname")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.XPATH, "//*[@data-key='parent_secondname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_secondname']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_secondname']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_secondname']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_secondname']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_secondname_none(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_secondname")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_secondname']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_secondname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_secondname']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_secondname']/p").text
        print("before =", save_value, ";", "after =", enter_value)
        assert save_value == enter_value

    def parent_surname(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_surname")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='parent_surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_surname']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='parent_surname']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='parent_surname']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_surname']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def parent_surname_none(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "parent_surname")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='parent_surname']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='parent_surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='parent_surname']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='parent_surname']/p").text
        print("before =", save_value, ";", "after =", enter_value)
        assert save_value == enter_value

    def parent_sex_female(self):
        wd = self.app.wd
        self.open_parent_info()
        # element = wd.find_element(By.ID, "passport_sex")
        # element = wd.find_element(By.XPATH, "//*[@id='passport_sex']")
        # wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
        wd.find_element(By.XPATH, "//*[@data-key='passport_sex'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='passport_sex']/div[2]/label").text
        wd.find_element(By.XPATH, "//*[@id='passport_sex']//input[@value=0]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='passport_sex']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def parent_sex_male(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "passport_sex")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='passport_sex'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='passport_sex']/div[1]/label").text
        wd.find_element(By.XPATH, "//*[@id='passport_sex']//input[@value=1]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
            name = str('parent_sex_male_' + datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + '.png')
            capture_path = str(pathlib.Path.cwd() / 'screenshots' / name)
            wd.save_screenshot(capture_path)
        new_value = wd.find_element(By.XPATH, "//*[@id='passport_sex']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def passport_unit_code(self, enter_value):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "passport_unit_code")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='passport_unit_code'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//input").send_keys(enter_value)
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//span[@class='input-group-btn']").click()
        save_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        print("enter_value =", enter_value, ";", "save_value =", save_value)
        assert enter_value == save_value

    def passport_unit_code_none(self):
        wd = self.app.wd
        self.open_parent_info()
        element = wd.find_element(By.ID, "passport_unit_code")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        save_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_unit_code'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_unit_code']//span[@class='input-group-btn']").click()
        enter_value = wd.find_element(By.XPATH, "//*[@id='passport_unit_code']/p").text
        print("save_value =", save_value, ";", "enter_value =", enter_value)
        assert save_value == enter_value
