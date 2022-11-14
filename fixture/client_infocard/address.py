import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    def open_address_info(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, "Фактический адрес").click()

    def edit_apartment(self, apt):
        wd = self.app.wd
        self.open_address_info()
        wd.find_element(By.XPATH, "//*[@data-key='fact_apt'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_apt']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_apt']//input").send_keys(apt)
        wd.find_element(By.XPATH, "//*[@id='fact_apt']//span[@class='input-group-btn']").click()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        print("apt =", apt, ";", "apt_edit =", apt_edit)
        assert apt == apt_edit

    def edit_apartment_none(self):
        wd = self.app.wd
        self.open_address_info()
        apt = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_apt'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_apt']//span[@class='input-group-btn']").click()
        time.sleep(1)
        apt_edit = wd.find_element(By.XPATH, "//*[@id='fact_apt']/p").text
        print("apt =", apt, ";", "apt_edit =", apt_edit)
        assert apt == apt_edit

    def edit_house(self, building):
        wd = self.app.wd
        self.open_address_info()
        wd.find_element(By.XPATH, "//*[@data-key='fact_building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_building']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_building']//input").send_keys(building)
        wd.find_element(By.XPATH, "//*[@id='fact_building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        print("building =", building, ";", "building_edit =", building_edit)
        assert building == building_edit

    def edit_house_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        building = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='fact_building']/p").text
        print("building =", building, ";", "building_edit =", building_edit)
        assert building == building_edit

    def edit_fact_city(self, city):
        wd = self.app.wd
        self.open_address_info()
        wd.find_element(By.XPATH, "//*[@data-key='fact_city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_city']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_city']//input").send_keys(city)
        wd.find_element(By.XPATH, "//*[@id='fact_city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        print("city =", city, ";", "city_edit =", city_edit)
        assert city == city_edit

    def edit_fact_city_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        city = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='fact_city']/p").text
        print("city =", city, ";", "city_edit =", city_edit)
        assert city == city_edit

    def edit_fact_country(self, country):
        wd = self.app.wd
        self.open_address_info()
        wd.find_element(By.XPATH, "//*[@data-key='fact_country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_country']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_country']//input").send_keys(country)
        wd.find_element(By.XPATH, "//*[@id='fact_country']//span[@class='input-group-btn']").click()
        country_edit = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        print("country =", country, ";", "country_edit =", country_edit)
        assert country == country_edit

    def edit_fact_country_none(self):
        wd = self.app.wd
        self.open_address_info()
        time.sleep(1)
        country = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_country']//span[@class='input-group-btn']").click()
        country_edit = wd.find_element(By.XPATH, "//*[@id='fact_country']/p").text
        print("country =", country, ";", "country_edit =", country_edit)
        assert country == country_edit

    def edit_fact_postcode(self, postcode):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_postcode")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='fact_postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_postcode']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_postcode']//input").send_keys(postcode)
        wd.find_element(By.XPATH, "//*[@id='fact_postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        print("postcode =", postcode, ";", "postcode_edit =", postcode_edit)
        assert postcode == postcode_edit

    def edit_fact_postcode_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_postcode")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        postcode = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='fact_postcode']/p").text
        print("postcode =", postcode, ";", "postcode_edit =", postcode_edit)
        assert postcode == postcode_edit

    def edit_fact_state(self, state):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_state")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='fact_state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_state']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_state']//input").send_keys(state)
        wd.find_element(By.XPATH, "//*[@id='fact_state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        print("state =", state, ";", "state_edit =", state_edit)
        assert state == state_edit

    def edit_fact_state_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_state")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        state = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='fact_state']/p").text
        print("state =", state, ";", "state_edit =", state_edit)
        assert state == state_edit

    def edit_fact_street(self, street):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_street")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='fact_street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_street']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='fact_street']//input").send_keys(street)
        wd.find_element(By.XPATH, "//*[@id='fact_street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        print("street =", street, ";", "street_edit =", street_edit)
        assert street == street_edit

    def edit_fact_street_none(self):
        wd = self.app.wd
        self.open_address_info()
        element = wd.find_element(By.ID, "fact_street")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        street = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='fact_street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='fact_street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='fact_street']/p").text
        print("street =", street, ";", "street_edit =", street_edit)
        assert street == street_edit
