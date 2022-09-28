import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ContactHelper:

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

    def open_contact_info(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, "Контактная информация").click()

    def edit_city_phone(self, phone):
        wd = self.app.wd
        self.open_contact_info()
        wd.find_element(By.XPATH, "//*[@data-key='city_phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city_phone']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='city_phone']//input").send_keys(phone)
        wd.find_element(By.XPATH, "//*[@id='city_phone']//span[@class='input-group-btn']").click()
        phone_edit = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        print("phone =", phone, ";", "phone_edit =", phone_edit)
        assert phone == phone_edit

    def edit_city_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        phone_before = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='city_phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city_phone']//span[@class='input-group-btn']").click()
        phone_after = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        print("phone_before =", phone_before, ";", "phone_after =", phone_after)
        assert phone_before == phone_after

    def edit_email(self, mail):
        wd = self.app.wd
        self.open_contact_info()
        wd.find_element(By.XPATH, "//*[@data-key='email'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='email']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='email']//input").send_keys(mail)
        wd.find_element(By.XPATH, "//*[@id='email']//span[@class='input-group-btn']").click()
        mail_edit = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        print("mail =", mail, ";", "mail_edit =", mail_edit)
        assert mail == mail_edit

    def edit_email_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        old_email = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='email'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='email']//span[@class='input-group-btn']").click()
        time.sleep(1)
        new_email = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        print("old_email =", old_email, ";", "new_email =", new_email)
        assert old_email == new_email

    def edit_mobile_phone(self, mobile):
        wd = self.app.wd
        self.open_contact_info()
        wd.find_element(By.XPATH, "//*[@data-key='mobile_phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='mobile_phone']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='mobile_phone']//input").send_keys(mobile)
        wd.find_element(By.XPATH, "//*[@id='mobile_phone']//span[@class='input-group-btn']").click()
        mobile_edit = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        print("mobile =", mobile, ";", "mobile_edit =", mobile_edit)
        assert mobile == mobile_edit

    def edit_mobile_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        mobile_before = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='mobile_phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='mobile_phone']//span[@class='input-group-btn']").click()
        mobile_after = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        print("mobile_before =", mobile_before, ";", "mobile_after =", mobile_after)
        assert mobile_before == mobile_after

    def edit_phone(self, phone):
        wd = self.app.wd
        self.open_contact_info()
        wd.find_element(By.XPATH, "//*[@data-key='phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='phone']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='phone']//input").send_keys(phone)
        wd.find_element(By.XPATH, "//*[@id='phone']//span[@class='input-group-btn']").click()
        phone_edit = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        print("phone =", phone, ";", "phone_edit =", phone_edit)
        assert phone == phone_edit

    def edit_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        phone_old = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='phone'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='phone']//span[@class='input-group-btn']").click()
        time.sleep(1)
        phone_new = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        print("phone_old =", phone_old, ";", "phone_new =", phone_new)
        assert phone_old == phone_new
