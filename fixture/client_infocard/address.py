import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AddressHelper:

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

    @allure.step("Открыть вкладку 'Фактический адрес'")
    def open_address_info(self):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'Основная информация'"):
            wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        with allure.step("Нажать кнопку 'Фактический адрес'"):
            wd.find_element(By.LINK_TEXT, "Фактический адрес").click()

    @allure.step("Редактировать и сохранить квартиру")
    def edit_apartment(self, apt):
        wd = self.app.wd
        self.open_address_info()
        with allure.step("Нажать кнопку редактировать поле 'квартира'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_apt'][@type='button']").click()
        with allure.step(f"Ввести значение: {apt}"):
            wd.find_element(By.XPATH, "//*[@id='fact_apt']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_apt']//input").send_keys(apt)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_apt']//span[@class='input-group-btn']").click()
            self.check_alert()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        print("apt =", apt, ";", "apt_edit =", apt_edit)
        with allure.step(f"Проверка. Вводимое значение: {apt}. Сохраненное значение: {apt_edit}"):
            assert apt == apt_edit

    def check_alert(self):
        wd = self.app.wd
        try:
            alert = wd.find_element(By.XPATH, "//*[@role='alert']").text
            print(alert)
            assert alert == 0
        except NoSuchElementException:
            print("Нет ошибок")

    @allure.step("Сохранить 'Дом' без изменений")
    def edit_apartment_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        apt = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        with allure.step("Нажать кнопку редактировать поле 'дом'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_apt'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_apt']//span[@class='input-group-btn']").click()
            self.check_alert()
        time.sleep(1)
        apt_edit = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        print("apt =", apt, ";", "apt_edit =", apt_edit)
        with allure.step(f"Проверка. Значение до редактирования: {apt}. Значение после сохранения: {apt_edit}"):
            assert apt == apt_edit

    @allure.step("Редактировать и сохранить дом")
    def edit_house(self, building):
        wd = self.app.wd
        self.open_address_info()
        with allure.step("Нажать кнопку редактировать поле 'дом'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_building'][@type='button']").click()
        with allure.step(f"Ввести значение: {building}"):
            wd.find_element(By.XPATH, "//*[@id='fact_building']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_building']//input").send_keys(building)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_building']//span[@class='input-group-btn']").click()
            self.check_alert()
        building_edit = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        print("building =", building, ";", "building_edit =", building_edit)
        with allure.step(f"Проверка. Введенное значение: {building}. Сохраненное значение: {building_edit}"):
            assert building == building_edit

    @allure.step("Сохранить значение поля 'дом' без изменений")
    def edit_house_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        building = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        with allure.step("Нажать кнопку редактировать поле 'дом'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_building'][@type='button']").click()
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='fact_building']//span[@class='input-group-btn']").click()
            self.check_alert()
        building_edit = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        print("building =", building, ";", "building_edit =", building_edit)
        with allure.step(f"Проверка. Значение до редактирования: {building}. "
                         f"Значение после сохранения: {building_edit}"):
            assert building == building_edit

    @allure.step("Редактировать и сохранить населенный пункт")
    def edit_fact_city(self, city):
        wd = self.app.wd
        self.open_address_info()
        with allure.step("Нажать кнопку редактировать поле населенный пункт"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_city'][@type='button']").click()
        with allure.step(f"Ввести значение: {city}"):
            wd.find_element(By.XPATH, "//*[@id='fact_city']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_city']//input").send_keys(city)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_city']//span[@class='input-group-btn']").click()
            self.check_alert()
        city_edit = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        print("city =", city, ";", "city_edit =", city_edit)
        with allure.step(f"Проверка. Вводимое значение: {city}. Сохраненное значение: {city_edit}"):
            assert city == city_edit

    @allure.step("Сохранить населенный пункт без изменений")
    def edit_fact_city_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        city = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        with allure.step("Нажать кнопку редактировать поле населенный пункт"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_city'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_city']//span[@class='input-group-btn']").click()
        self.check_alert()
        city_edit = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        print("city =", city, ";", "city_edit =", city_edit)
        with allure.step(f"Проверка. Значение до редактирования: {city}. Значение после редактирования: {city_edit}"):
            assert city == city_edit

    @allure.step("Редактировать и сохранить поле 'Страна'")
    def edit_fact_country(self, country):
        wd = self.app.wd
        self.open_address_info()
        with allure.step("Нажать кнопку редактировать поле Страна"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_country'][@type='button']").click()
        with allure.step(f"Ввести значение: {country}"):
            wd.find_element(By.XPATH, "//*[@id='fact_country']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_country']//input").send_keys(country)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_country']//span[@class='input-group-btn']").click()
            self.check_alert()
        country_edit = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        print("country =", country, ";", "country_edit =", country_edit)
        with allure.step(f"Проверка. Вводимое значение: {country}. Сохранное значение: {country_edit}"):
            assert country == country_edit

    @allure.step("Сохранить значение поля 'Страна'")
    def edit_fact_country_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        country = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        with allure.step("Нажать кнопку редактировать поле 'Страна'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_country'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_country']//span[@class='input-group-btn']").click()
            self.check_alert()
        country_edit = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        print("country =", country, ";", "country_edit =", country_edit)
        with allure.step(f"Проверка. Значение до редактирования: {country}. Значение после сохранения: {country_edit}"):
            assert country == country_edit

    @allure.step("Редактировать и сохранить почтовый индекс")
    def edit_fact_postcode(self, postcode):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_postcode")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать поле почтовый индекс"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_postcode'][@type='button']").click()
        with allure.step(f"Ввести значение: {postcode}"):
            wd.find_element(By.XPATH, "//*[@id='fact_postcode']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_postcode']//input").send_keys(postcode)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_postcode']//span[@class='input-group-btn']").click()
            self.check_alert()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        print("postcode =", postcode, ";", "postcode_edit =", postcode_edit)
        with allure.step(f"Проверка. Вводимое значение: {postcode}. Сохраненное значение: {postcode_edit}"):
            assert postcode == postcode_edit

    @allure.step("Сохранить почтовый индекс без изменения")
    def edit_fact_postcode_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_postcode")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        postcode = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        with allure.step("Нажать кнопку редактировать поле 'почтовый индекс'"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_postcode'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_postcode']//span[@class='input-group-btn']").click()
            self.check_alert()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        print("postcode =", postcode, ";", "postcode_edit =", postcode_edit)
        with allure.step(f"Проверка. Значение до редактирования: {postcode}. "
                         f"Значение после сохранения: {postcode_edit}"):
            assert postcode == postcode_edit

    @allure.step("Редактировать и сохранить регион")
    def edit_fact_state(self, state):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_state")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать поле регион"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_state'][@type='button']").click()
        with allure.step(f"Ввести значение: {state}"):
            wd.find_element(By.XPATH, "//*[@id='fact_state']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_state']//input").send_keys(state)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_state']//span[@class='input-group-btn']").click()
            self.check_alert()
        state_edit = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        print("state =", state, ";", "state_edit =", state_edit)
        with allure.step(f"Проверка. Вводимое значение: {state}. Сохраненное значение: {state_edit}"):
            assert state == state_edit

    @allure.step("Сохранить регион без изменений")
    def edit_fact_state_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_state")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        state = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        with allure.step("Нажать кнопку редактировать поле регион"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_state'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_state']//span[@class='input-group-btn']").click()
            self.check_alert()
        state_edit = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        print("state =", state, ";", "state_edit =", state_edit)
        with allure.step(f"Проверка. Значение до редактирования: {state}. Значение после сохранения: {state_edit}"):
            assert state == state_edit

    @allure.step("Редактировать и сохранить улицу")
    def edit_fact_street(self, street):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_street")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать поле улица"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_street'][@type='button']").click()
        with allure.step(f"Ввести значение: {street}"):
            wd.find_element(By.XPATH, "//*[@id='fact_street']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='fact_street']//input").send_keys(street)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_street']//span[@class='input-group-btn']").click()
            self.check_alert()
        street_edit = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        print("street =", street, ";", "street_edit =", street_edit)
        with allure.step(f"Проверка. Вводимое значение: {street}. Сохраненное значение: {street_edit}"):
            assert street == street_edit

    @allure.step("Сохранить улицу без изменений")
    def edit_fact_street_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_street")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        street = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        with allure.step("Нажать кнопку редактировать поле улица"):
            wd.find_element(By.XPATH, "//*[@data-key='fact_street'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='fact_street']//span[@class='input-group-btn']").click()
            self.check_alert()
        street_edit = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        print("street =", street, ";", "street_edit =", street_edit)
        with allure.step(f"Проверка. Значение до редактирования: {street}. Значение после сохранения: {street_edit}"):
            assert street == street_edit
