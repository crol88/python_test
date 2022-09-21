import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PassportHelper:

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

    def open_passport_info(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, "Паспортные данные").click()

    def edit_copy_passport_value_yes(self):
        wd = self.app.wd
        self.open_passport_info()
        wd.find_element(By.XPATH, "//*[@data-key='copyPassportYes'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='copyPassportYes']/div[1]/label").text
        wd.find_element(By.XPATH, "//*[@id='copyPassportYes']//input[@value=1]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='copyPassportYes']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def edit_copy_passport_value_no(self):
        wd = self.app.wd
        self.open_passport_info()
        wd.find_element(By.XPATH, "//*[@data-key='copyPassportYes'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='copyPassportYes']/div[2]/label").text
        wd.find_element(By.XPATH, "//*[@id='copyPassportYes']//input[@value=0]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='copyPassportYes']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def edit_passport_address(self, registration):
        wd = self.app.wd
        self.open_passport_info()
        wd.find_element(By.XPATH, "//*[@data-key='passport_address'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_address']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_address']//input").send_keys(registration)
        wd.find_element(By.XPATH, "//*[@id='passport_address']//span[@class='input-group-btn']").click()
        reg_edit = wd.find_element(By.XPATH, "//*[@id='passport_address']/p").text
        print("enter_data =", registration, ";", "save_data =", reg_edit)
        assert registration == reg_edit

    def edit_passport_address_none(self):
        wd = self.app.wd
        self.open_passport_info()
        reg = wd.find_element(By.XPATH, "//*[@id='passport_address']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_address'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_address']//span[@class='input-group-btn']").click()
        reg_edit = wd.find_element(By.XPATH, "//*[@id='passport_address']/p").text
        print("enter_data =", reg, ";", "save_data =", reg_edit)
        assert reg == reg_edit

    def edit_passport_address_live(self, address):
        wd = self.app.wd
        self.open_passport_info()
        wd.find_element(By.XPATH, "//*[@data-key='passport_address_live'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_address_live']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_address_live']//input").send_keys(address)
        wd.find_element(By.XPATH, "//*[@id='passport_address_live']//span[@class='input-group-btn']").click()
        address_edit = wd.find_element(By.XPATH, "//*[@id='passport_address_live']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        assert address == address_edit

    def edit_passport_address_live_none(self):
        wd = self.app.wd
        self.open_passport_info()
        time.sleep(1)
        address = wd.find_element(By.XPATH, "//*[@id='passport_address_live']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_address_live'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_address_live']//span[@class='input-group-btn']").click()
        address_edit = wd.find_element(By.XPATH, "//*[@id='passport_address_live']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        assert address == address_edit

    def edit_passport_number(self, passport):
        wd = self.app.wd
        self.open_passport_info()
        wd.find_element(By.XPATH, "//*[@data-key='passport_number'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_number']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_number']//input").send_keys(passport)
        wd.find_element(By.XPATH, "//*[@id='passport_number']//span[@class='input-group-btn']").click()
        passport_edit = wd.find_element(By.XPATH, "//*[@id='passport_number']/p").text
        print("before =", passport, ";", "after =", passport_edit)
        assert passport == passport_edit

    def edit_passport_number_none(self):
        wd = self.app.wd
        self.open_passport_info()
        time.sleep(1)
        passport = wd.find_element(By.XPATH, "//*[@id='passport_number']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_number'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_number']//span[@class='input-group-btn']").click()
        passport_edit = wd.find_element(By.XPATH, "//*[@id='passport_number']/p").text
        print("before =", passport, ";", "after =", passport_edit)
        assert passport == passport_edit

    def edit_passport_issue_date(self, data):
        wd = self.app.wd
        self.open_passport_info()
        element = wd.find_element(By.ID, "passport_when")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='passport_when'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_when']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_when']//input").send_keys(data)
        wd.find_element(By.XPATH, "//*[@id='passport_when']//span[@class='input-group-btn']").click()
        edit_data = wd.find_element(By.XPATH, "//*[@id='passport_when']/p").text
        print("enter_data =", data, ";", "save_data =", edit_data)
        assert data == edit_data

    def edit_passport_issue_date_none(self):
        wd = self.app.wd
        self.open_passport_info()
        element = wd.find_element(By.ID, "passport_when")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        data = wd.find_element(By.XPATH, "//*[@id='passport_when']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_when'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_when']//span[@class='input-group-btn']").click()
        edit_data = wd.find_element(By.XPATH, "//*[@id='passport_when']/p").text
        print("enter_data =", data, ";", "save_data =", edit_data)
        assert data == edit_data

    def edit_passport_who(self, who):
        wd = self.app.wd
        self.open_passport_info()
        element = wd.find_element(By.ID, "passport_who")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.XPATH, "//*[@data-key='passport_who'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_who']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='passport_who']//input").send_keys(who)
        wd.find_element(By.XPATH, "//*[@id='passport_who']//span[@class='input-group-btn']").click()
        who_edit = wd.find_element(By.XPATH, "//*[@id='passport_who']/p").text
        print("enter_data =", who, ";", "save_data =", who_edit)
        assert who == who_edit

    def edit_passport_who_none(self):
        wd = self.app.wd
        self.open_passport_info()
        element = wd.find_element(By.ID, "passport_who")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        who = wd.find_element(By.XPATH, "//*[@id='passport_who']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='passport_who'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='passport_who']//span[@class='input-group-btn']").click()
        who_edit = wd.find_element(By.XPATH, "//*[@id='passport_who']/p").text
        print("enter_data =", who, ";", "save_data =", who_edit)
        assert who == who_edit

