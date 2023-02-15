import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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

    @allure.step("Открыть контактную информацию")
    def open_contact_info(self):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'Основная информация'"):
            wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        with allure.step("Нажать кнопку 'Контактная информация'"):
            wd.find_element(By.LINK_TEXT, "Контактная информация").click()

    @allure.step("Редактировать и сохранить городской телефон")
    def edit_city_phone(self, phone):
        wd = self.app.wd
        self.open_contact_info()
        with allure.step("Нажать кнопку редактировать поле 'городской телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='city_phone'][@type='button']").click()
        with allure.step(f"Ввести значение: {phone}"):
            wd.find_element(By.XPATH, "//*[@id='city_phone']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='city_phone']//input").send_keys(phone)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='city_phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        phone_edit = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        print("phone =", phone, ";", "phone_edit =", phone_edit)
        with allure.step(f"Проверка. Вводимое значение: {phone}. Сохраненное значение: {phone_edit}"):
            assert phone == phone_edit

    @allure.step("Сохранить городской телефон без изменений")
    def edit_city_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        phone_before = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        with allure.step("Нажать кнопку редактировать поле 'городской телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='city_phone'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='city_phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        phone_after = wd.find_element(By.XPATH, "//*[@id='city_phone']/p").text
        print("phone_before =", phone_before, ";", "phone_after =", phone_after)
        with allure.step(f"Проверка. Значение до редактирования: {phone_before}."
                         f" Значение после сохранения: {phone_after}"):
            assert phone_before == phone_after

    @allure.step("Редактировать и сохранить E-mail")
    def edit_email(self, mail):
        wd = self.app.wd
        self.open_contact_info()
        with allure.step("Нажать кнопку редактировать поле 'E-mail'"):
            wd.find_element(By.XPATH, "//*[@data-key='email'][@type='button']").click()
        with allure.step(f"Ввести значение: {mail}"):
            wd.find_element(By.XPATH, "//*[@id='email']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='email']//input").send_keys(mail)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='email']//span[@class='input-group-btn']").click()
            self.check_alert()
        mail_edit = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        print("mail =", mail, ";", "mail_edit =", mail_edit)
        with allure.step(f"Проверка. Вводимое значение: {mail}. Сохраненное значение: {mail_edit}"):
            assert mail == mail_edit

    def check_alert(self):
        wd = self.app.wd
        try:
            alert = wd.find_element(By.XPATH, "//*[@role='alert']").text
            print(alert)
            assert alert == 0
        except NoSuchElementException:
            print("Нет ошибок")

    @allure.step("Сохранить E-mail пациента")
    def edit_email_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        old_email = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        with allure.step("Нажать кнопку редактировать поле 'E-mail'"):
            wd.find_element(By.XPATH, "//*[@data-key='email'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='email']//span[@class='input-group-btn']").click()
            self.check_alert()
        time.sleep(1)
        new_email = wd.find_element(By.XPATH, "//*[@id='email']/p").text
        print("old_email =", old_email, ";", "new_email =", new_email)
        with allure.step(f"Проверка. Значение до редактирования: {old_email}. Значение после сохранения: {new_email}"):
            assert old_email == new_email

    @allure.step("Редактировать и сохранить мобильный телефон")
    def edit_mobile_phone(self, mobile):
        wd = self.app.wd
        self.open_contact_info()
        with allure.step("Нажать кнопку редактировать поле 'мобильный телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='mobile_phone'][@type='button']").click()
        with allure.step(f"Ввести значение: {mobile}"):
            wd.find_element(By.XPATH, "//*[@id='mobile_phone']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='mobile_phone']//input").send_keys(mobile)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='mobile_phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        mobile_edit = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        print("mobile =", mobile, ";", "mobile_edit =", mobile_edit)
        with allure.step(f"Проверка. Вводимое значение: {mobile}. Сохраненное значение: {mobile_edit}"):
            assert mobile == mobile_edit

    @allure.step("Сохранить мобильный телефон пациента")
    def edit_mobile_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        mobile_before = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        with allure.step("Нажать кнопку редактировать поле 'мобильный телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='mobile_phone'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='mobile_phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        mobile_after = wd.find_element(By.XPATH, "//*[@id='mobile_phone']/p").text
        print("mobile_before =", mobile_before, ";", "mobile_after =", mobile_after)
        with allure.step(f"Проверка. Значение до редактирования: {mobile_before}."
                         f" Значение после сохранения: {mobile_after}"):
            assert mobile_before == mobile_after

    @allure.step("Редактировать и сохранить другой телефон")
    def edit_phone(self, phone):
        wd = self.app.wd
        self.open_contact_info()
        with allure.step("Нажать кнопку редактировать поле 'другой телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='phone'][@type='button']").click()
        with allure.step(f"Ввести значение: {phone}"):
            wd.find_element(By.XPATH, "//*[@id='phone']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='phone']//input").send_keys(phone)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        phone_edit = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        print("phone =", phone, ";", "phone_edit =", phone_edit)
        with allure.step(f"Проверка. Вводимое значение: {phone}. Сохраненное значение: {phone_edit}"):
            assert phone == phone_edit

    @allure.step("Сохранить другой телефон")
    def edit_phone_none(self):
        wd = self.app.wd
        self.open_contact_info()
        time.sleep(1)
        phone_old = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        with allure.step("Нажать кнопку редактировать поле 'другой телефон'"):
            wd.find_element(By.XPATH, "//*[@data-key='phone'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='phone']//span[@class='input-group-btn']").click()
            self.check_alert()
        time.sleep(1)
        phone_new = wd.find_element(By.XPATH, "//*[@id='phone']/p").text
        print("phone_old =", phone_old, ";", "phone_new =", phone_new)
        with allure.step(f"Проверка. Значение до редактирования: {phone_old}. Значение после сохранения: {phone_new}"):
            assert phone_old == phone_new
