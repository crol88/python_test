import time
import random
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import testit


class BasicInfoHelper:

    def __init__(self, app):
        self.app = app

    @testit.step('Открыть список пациентов')
    def count(self, check_patient):
        wd = self.app.wd
        with testit.step('Проверить присутствие пациента, если пациент присутствует, вернуться к списку'):
            if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
                wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
                wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
            return len(wd.find_elements(By.LINK_TEXT, check_patient))

    @testit.step('Найти пациента через глобальный поиск')
    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        with testit.step('Нажать Поиск по пациентам'):
            wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        with testit.step('Ввести фамилию пациента'):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        with testit.step('Подтвердить результат поиска'):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def open_cbase(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    @testit.step('Если пациент отсутствует, добавляем')
    def add_patient_for(self, group):
        wd = self.app.wd
        if group.filial is not None:
            wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        with testit.step('Нажать Добавить'):
            self.push_button_newclient()
        with testit.step('Заполнить форму добавления нового пациента'):
            self.fill_newclient_form(group)
        with testit.step('Подтвердить ввод данных'):
            self.submit_newpatient_creation()

    def push_button_newclient(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    def fill_newclient_form(self, group):
        wd = self.app.wd
        # Заполнить обязательные поля ввода валидными данными
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

    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        if wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']") == 0:
            wd.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()
        time.sleep(2)

    def open_random_patient(self):
        wd = self.app.wd
        self.open_cbase()
        random_p = wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[2]")
        names = [e.text for e in random_p]
        random_name = random.choice(names)
        element = wd.find_element(By.LINK_TEXT, random_name)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, random_name).click()

    def get_basic_patient_birthday(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='birthday']//input").get_attribute("value")

    def open_field_basic_patient_info(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()

    def get_basic_patient_secondname(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='second_name']//input").get_attribute("value")

    def get_basic_patient_name(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='name']//input").get_attribute("value")

    def get_basic_patient_surname(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='surname']//input").get_attribute("value")

    @testit.step('Редактирование фамилии и проверка результата')
    def edit_patient_surname(self, group, text):
        wd = self.app.wd
        with testit.step('Активировать поле Фамилия'):
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        with testit.step('Очистить поле ввода и ввести новую Фамилию'):
            wd.find_element(By.XPATH, "//*[@id='surname']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='surname']//input").send_keys(group.surname)
        with testit.step('Сохранить данные'):
            wd.find_element(By.XPATH, "//*[@id='surname']//span[@class='input-group-btn']").click()
        with testit.step('Проверить ожидаемый и фактический результат'):
            surname = wd.find_element(By.XPATH, "//*[@id='surname']/p").text
            print("enter_data =", text, ";", "save_data =", surname)
            assert text == surname

    def edit_patient_surname_fill(self, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='surname']//span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p").text
        print("enter_data =", text, ";", "save_data =", surname)
        assert text == surname

    def edit_patient_name_fill(self):
        wd = self.app.wd
        name = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        name_after = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        print("enter_data =", name, ";", "save_data =", name_after)
        assert name == name_after

    def edit_patient_secondname_fill(self, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p").text
        print("enter_data =", text, ";", "save_data =", secondname)
        assert text == secondname

    def edit_patient_name(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
        wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        print("enter_data =", text, ";", "save_data =", surname)
        assert text == surname

    def edit_patient_secondname(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
        wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p").text
        print("enter_data =", text, ";", "save_data =", secondname)
        assert text == secondname

    def edit_patient_birthday(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='birthday']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='birthday']//input").send_keys(group.birthday)
        wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        print("enter_data =", text, ";", "save_data =", birthday)
        assert text in birthday

    def edit_patient_birthday_fill(self):
        wd = self.app.wd
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        birthday_after = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        print("enter_data =", birthday_after, ";", "save_data =", birthday)
        assert birthday_after in birthday

    def edit_patient_sex(self, sex):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        select = Select(wd.find_element(By.XPATH, "//*[@id='sex']/div/select"))
        select.select_by_visible_text(sex)
        wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_edit = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        print("enter_data =", sex_edit, ";", "save_data =", sex)
        assert sex_edit == sex

    def edit_patient_sex_male_fill(self):
        wd = self.app.wd
        sex = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_after = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        print("enter_data =", sex, ";", "save_data =", sex_after)
        assert sex == sex_after

    def edit_patient_inn(self, inn):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='inn']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='inn']//input").send_keys(inn)
        wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        print("enter_data =", inn_edit, ";", "save_data =", inn)
        assert inn_edit == inn

    def edit_patient_inn_fill(self):
        wd = self.app.wd
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit_after = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        print("enter_data =", inn_edit, ";", "save_data =", inn_edit_after)
        assert inn_edit == inn_edit_after

    def edit_patient_country(self, country):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='country']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='country']//input").send_keys(country)
        wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_edit = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        print("enter_data =", country_edit, ";", "save_data =", country)
        assert country_edit == country

    def edit_patient_country_fill(self):
        wd = self.app.wd
        country = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_after = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        print("enter_data =", country, ";", "save_data =", country_after)
        assert country == country_after

    def edit_patient_postcode(self, postcode):
        wd = self.app.wd
        self.go_to_element_by_id(id_locator="postcode")
        self.id_double_click(click_id="postcode")
        # wd.find_element(By.XPATH, "//*[@data-key='postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='postcode']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='postcode']//input").send_keys(postcode)
        wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        print("enter_data =", postcode, ";", "save_data =", postcode_edit)
        assert postcode == postcode_edit

    def id_double_click(self, click_id):
        wd = self.app.wd
        button = wd.find_element(By.ID, click_id)
        ActionChains(wd).double_click(button).perform()

    def edit_patient_postcode_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="postcode")
        postcode = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        self.id_double_click(click_id="postcode")
        # wd.find_element(By.XPATH, "//*[@data-key='postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        print("enter_data =", postcode, ";", "save_data =", postcode_edit)
        assert postcode == postcode_edit

    def scroll_to_element(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, 1000);")
        time.sleep(1)

    def edit_patient_state(self, state):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="state")
        element = wd.find_element(By.ID, "state")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='state']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='state']//input").send_keys(state)
        wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        print("enter_data =", state, ";", "save_data =", state_edit)
        assert state == state_edit

    def edit_patient_state_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="state")
        # wd.execute_script("window.scrollTo(0,1600)")
        element = wd.find_element(By.ID, "state")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        state = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        print("enter_data =", state, ";", "save_data =", state_edit)
        assert state == state_edit

    def edit_patient_city(self, city):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="city")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='city']//input").send_keys(city)
        wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        print("enter_data =", city_edit, ";", "save_data =", city)
        assert city_edit == city

    def edit_patient_city_without_changes(self):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="city")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        city = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        print("enter_data =", city, ";", "save_data =", city_edit)
        assert city == city_edit

    def edit_patient_street(self, street):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="street")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='street']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='street']//input").send_keys(street)
        wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        print("enter_data =", street, ";", "save_data =", street_edit)
        assert street == street_edit

    def edit_patient_street_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="street")
        street = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        print("enter_data =", street, ";", "save_data =", street_edit)
        assert street == street_edit

    def edit_patient_building(self, building):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="building")
        wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='building']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='building']//input").send_keys(building)
        wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        print("enter_data =", building, ";", "save_data =", building_edit)
        assert building == building_edit

    def edit_patient_building_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="building")
        building = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        print("enter_data =", building, ";", "save_data =", building_edit)
        assert building == building_edit

    def edit_patient_apartment(self, apt):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="apt")
        wd.find_element(By.XPATH, "//*[@data-key='apt'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='apt']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='apt']//input").send_keys(apt)
        wd.find_element(By.XPATH, "//*[@id='apt']//span[@class='input-group-btn']").click()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        print("enter_data =", apt, ";", "save_data =", apt_edit)
        assert apt == apt_edit

    def edit_patient_apartment_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="apt")
        apt = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='apt'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='apt']//span[@class='input-group-btn']").click()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        print("enter_data =", apt, ";", "save_data =", apt_edit)
        assert apt == apt_edit

    def edit_patient_address(self, address):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="address")
        wd.find_element(By.XPATH, "//*[@data-key='address'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='address']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='address']//input").send_keys(address)
        wd.find_element(By.XPATH, "//*[@id='address']//span[@class='input-group-btn']").click()
        address_edit = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        assert address == address_edit

    def edit_patient_address_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="address")
        address = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='address'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='address']//span[@class='input-group-btn']").click()
        address_edit = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        assert address == address_edit

    def edit_patient_first_data(self, data):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_first_appointment")
        wd.find_element(By.XPATH, "//*[@data-key='date_of_first_appointment'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//input").send_keys(data)
        wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//span[@class='input-group-btn']").click()
        data_edit = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        print("enter_data =", data, ";", "save_data =", data_edit)
        assert data == data_edit

    def edit_patient_first_data_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_first_appointment")
        data = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='date_of_first_appointment'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//span[@class='input-group-btn']").click()
        data_edit = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        print("enter_data =", data, ";", "save_data =", data_edit)
        assert data == data_edit

    def edit_patient_last_data(self, data):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_last_appointment")
        wd.find_element(By.XPATH, "//*[@data-key='date_of_last_appointment'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").send_keys(data)
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//span[@class='input-group-btn']").click()
        data_edit = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        print("enter_data =", data, ";", "save_data =", data_edit)
        assert data_edit == data

    def edit_patient_last_data_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_last_appointment")
        data = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='date_of_last_appointment'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//span[@class='input-group-btn']").click()
        data_edit = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        print("enter_data =", data, ";", "save_data =", data_edit)
        assert data_edit == data

    def go_to_element_by_id(self, id_locator):
        wd = self.app.wd
        element = wd.find_element(By.ID, id_locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def add_mark(self, mark):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//*[@class='btn btn-sm btn-default dropdown-toggle btn-block']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn btn-sm btn-default dropdown-toggle btn-block']").click()
        wd.find_element(By.XPATH, "//*[@class='dropdown-menu']/li/a[text()='%s']" % mark).click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        time.sleep(1)
        status = wd.find_element(By.XPATH, "//*[@class='list-group-item_flex']").text
        print("status:", status, ";", "mark:", mark)
        assert status == mark

    def delete_vip_mark(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='mb-10']//text()[contains(.,'VIP')]/preceding-sibling::span//*["
                                  "@type='button']").click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        if len(wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")) != 0:
            marks = wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")
            names = [e.text for e in marks]
            print(names)
            assert "VIP" not in names

    def delete_blacklist_mark(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        wd.find_element(By.XPATH, "//text()[contains(.,'Черный список')]/preceding-sibling::span/button").click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        if len(wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")) != 0:
            marks = wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")
            names = [e.text for e in marks]
            print(names)
            assert "Черный список" not in names

    def delete_insurance_mark(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        time.sleep(2)
        wd.find_element(By.XPATH, "//text()[contains(.,'Страховой')]/preceding-sibling::span/button").click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        if len(wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")) != 0:
            marks = wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")
            names = [e.text for e in marks]
            print(names)
            assert "Страховой" not in names

    def delete_some_mark(self, mark):
        # mark can be: "vip", "blacklist" or "insurance"
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        select_mark = mark
        if select_mark == "vip":
            if len(wd.find_elements(By.XPATH, "//*[@class='mb-10']//text()[contains(.,'VIP')]"
                                              "/preceding-sibling::span//*[@type='button']")) == 0:
                self.add_mark(mark="VIP")
            self.delete_vip_mark()
        if select_mark == "blacklist":
            if len(wd.find_elements(By.XPATH, "//*[@class='mb-10']//text()[contains(.,'Черный список')]"
                                              "/preceding-sibling::span//*[@type='button']")) == 0:
                self.add_mark(mark="Черный список")
            self.delete_blacklist_mark()
        if select_mark == "insurance":
            if len(wd.find_elements(By.XPATH, "//*[@class='mb-10']//text()[contains(.,'Страховой')]"
                                              "/preceding-sibling::span//*[@type='button']")) == 0:
                self.add_mark(mark="Страховой")
            self.delete_insurance_mark()
