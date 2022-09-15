import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from model.group import Group
from selenium.webdriver.support.ui import Select


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_form_newclient(self):
        # Открыть список пациентов
        self.open_cbase()
        self.push_button_newClient()

    def open_cbase(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    def check_exists_by_xpath(self):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, "//*[@href='/cbase/admin/newClient']")) > 0

    def change_filial(self, group):
        wd = self.app.wd
        # Открыть список пациентов
        self.open_cbase()
        # Изменить филиал
        if group.filial is not None:
            wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newClient()

    def push_button_newClient(self):
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

    def empty_newclient_form(self, group):
        wd = self.app.wd
        # Оставить поля ввода пустыми
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
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='modalClose']").click()

    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        if wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']") == 0:
            wd.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        wd.find_element(By.XPATH, "//*[@class='btn-default btn js-done-step']").click()
        time.sleep(2)
        self.group_cache = None

    def delete_new_patient(self, search_name):
        wd = self.app.wd
        # Поиск пациента
        self.search_patient(search_name)
        # Опции
        wd.find_element(By.XPATH, "//*[@class='col-md-8 text-right pageActions']/div[2]/div[1]").click()
        # Удалить пациента
        wd.find_element(By.XPATH, "//*[@class='js-client_delete']").click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='sweet-spacer']/following-sibling::button[1]").click()
        self.group_cache = None

    def edit_patient_data(self, group):
        wd = self.app.wd
        # Редактировать фамилию
        if group.surname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@class='form-control']").clear()
            wd.find_element(By.XPATH, "//*[@class='form-control']").send_keys(group.surname)
            wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-group-btn']").click()
        # Редактировать имя
        if group.name is not None:
            wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
            wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        # Редактировать отчество
        if group.secondname is not None:
            wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
            wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        self.group_cache = None

    def search_patient(self, search_name):

        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def add_patient(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        self.push_button_newClient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    def count(self, check_patient):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        return len(wd.find_elements(By.LINK_TEXT, check_patient))

    def add_patient_for_del(self, group):
        wd = self.app.wd
        if group.filial is not None:
            wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        self.push_button_newClient()
        self.fill_newclient_form(group)
        self.submit_newpatient_creation()

    group_cache = None

    def get_group_list(self):
        # Проверка списка пациентов
        if self.group_cache is None:
            wd = self.app.wd
            self.open_cbase()
            self.group_cache = []
            for element in wd.find_elements(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr"):
                text = element.find_element(By.XPATH, "//*[@class='table table-clients-list']/tbody/tr/td[2]").text
                cbaseid = element.find_element(By.XPATH, "//*[@class='js-client-checkbox']") \
                    .get_attribute("data-client-id")
                self.group_cache.append(Group(name=text, cbaseid=cbaseid))
        return list(self.group_cache)

    def get_basic_patient_info_after_edit(self):
        wd = self.app.wd
        self.search_patient(search_name="")
        self.open_field_basic_patient_info()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']//input").get_attribute("value")
        name = wd.find_element(By.XPATH, "//*[@id='name']//input").get_attribute("value")
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']//input").get_attribute("value")
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']//input").get_attribute("value")
        return Group(surname=surname, name=name, secondname=secondname, birthday=birthday)

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

    # def get_basic_patient_info(self):
    #     if self.group_cache is None:
    #         wd = self.app.wd
    #         self.search_patient(search_name="")
    #         self.open_field_basic_patient_info()
    #         self.group_cache = []
    #         for row in wd.find_element(By.XPATH, "//*[@id='collapseOne']"):
    #             cells = row.find_element(By.TAG_NAME, "p")
    #             surname = cells[0].text
    #             name = cells[1].text
    #             secondname = cells[2].text
    #             birthday = cells[3].text
    #             self.group_cache.append(Group())

    def edit_patient_surname(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='surname']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='surname']//input").send_keys(group.surname)
        wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p")
        assert text == surname.text

    def edit_patient_surname_fill(self, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='surname']/descendant::span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p")
        assert text == surname.text

    def edit_patient_name_fill(self):
        wd = self.app.wd
        name = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        name_after = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        assert name == name_after

    def edit_patient_secondname_fill(self, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p")
        assert text == secondname.text

    def edit_patient_name(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
        wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='name']/p")
        assert text == surname.text

    def edit_patient_secondname(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
        wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p")
        assert text == secondname.text

    def edit_patient_birthday(self, group, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='birthday']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='birthday']//input").send_keys(group.birthday)
        wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        # assert text == birthday.text
        assert text in birthday

    def edit_patient_birthday_fill(self):
        wd = self.app.wd
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        birthday_after = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        assert birthday_after in birthday

    def edit_patient_sex(self, sex):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        select = Select(wd.find_element(By.XPATH, "//*[@id='sex']/div/select"))
        select.select_by_visible_text(sex)
        wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_edit = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        assert sex_edit == sex

    def edit_patient_sex_male_fill(self):
        wd = self.app.wd
        sex = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_after = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        assert sex == sex_after

    def edit_patient_inn(self, inn):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='inn']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='inn']//input").send_keys(inn)
        wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        assert inn_edit == inn

    def edit_patient_inn_fill(self):
        wd = self.app.wd
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit_after = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        assert inn_edit == inn_edit_after

    def edit_patient_country(self, country):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='country']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='country']//input").send_keys(country)
        wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_edit = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        assert country_edit == country

    # def basic_info(self):
    #     wd = self.app.wd
    #     wd.find_elements(By.XPATH, "//*[contains(text(), 'SURNAME-EDIT')]")

    def edit_patient_country_fill(self):
        wd = self.app.wd
        country = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_after = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        assert country == country_after

    def edit_patient_postcode(self, postcode):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='postcode']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='postcode']//input").send_keys(postcode)
        wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        assert postcode == postcode_edit

    def edit_patient_postcode_none(self):
        wd = self.app.wd
        self.scroll_to_element()
        postcode = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='postcode'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        assert postcode == postcode_edit

    def scroll_to_element(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, 1000);")
        time.sleep(1)

    def edit_patient_last_data(self, data):
        wd = self.app.wd
        self.scroll_to_element()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@data-key='date_of_last_appointment'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").send_keys(data)
        wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//span[@class='input-group-btn']").click()
        data_edit = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        assert data_edit == data

    def edit_patient_state(self, state):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='state']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='state']//input").send_keys(state)
        wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        assert state == state_edit

    def edit_patient_state_none(self):
        wd = self.app.wd
        self.scroll_to_element()
        state = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        assert state == state_edit

    def edit_patient_city(self, city):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='city']//input").send_keys(city)
        wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        assert city_edit == city

    def edit_patient_city_without_changes(self):
        wd = self.app.wd
        self.scroll_to_element()
        city = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        assert city == city_edit

    def edit_patient_street(self, street):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='street']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='street']//input").send_keys(street)
        wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        assert street == street_edit

    def edit_patient_street_none(self):
        wd = self.app.wd
        self.scroll_to_element()
        street = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        assert street == street_edit

    def edit_patient_building(self, building):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='building']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='building']//input").send_keys(building)
        wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        assert building == building_edit

    def edit_patient_building_none(self):
        wd = self.app.wd
        self.scroll_to_element()
        building = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        assert building == building_edit

    def edit_patient_apartment(self, apt):
        wd = self.app.wd
        self.scroll_to_element()
        wd.find_element(By.XPATH, "//*[@data-key='apt'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='apt']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='apt']//input").send_keys(apt)
        wd.find_element(By.XPATH, "")

