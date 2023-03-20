import time
import random

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasicInfoHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Открыть список пациентов')
    def count(self, check_patient):
        wd = self.app.wd
        with allure.step('Проверить присутствие пациента'):
            if len(wd.find_elements(By.LINK_TEXT, "Список пациентов")) == 0:
                wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
                wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
            return len(wd.find_elements(By.LINK_TEXT, check_patient))

    @allure.step("Поиск по пациентам")
    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        with allure.step("Нажать 'Поиск по пациентам'"):
            wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        with allure.step(f"Ввести данные пациента: {search_name}"):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        with allure.step("Нажать ENTER"):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    def open_cbase(self):
        wd = self.app.wd
        if len(wd.find_elements(By.LINK_TEXT, "Добавить")) == 0:
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()

    @allure.step("Генерация тестовых данных")
    def add_patient_for(self, group):
        wd = self.app.wd
        if group.filial is not None:
            with allure.step("Если указан филиал"):
                with allure.step("Нажать на окно выбора филиала"):
                    wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
                with allure.step("Выбрать филиал"):
                    wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.filial)
                    wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(3)
        # Добавить нового пациента
        with allure.step("Добавить нового пациента"):
            self.push_button_newclient()
            self.fill_newclient_form(group)
            self.submit_newpatient_creation()

    @allure.step("Нажать кнопку 'Добавить'")
    def push_button_newclient(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/cbase/admin/newClient']").click()

    @allure.step("Заполнить форму добавления нового пациента")
    def fill_newclient_form(self, group):
        wd = self.app.wd
        # Заполнить обязательные поля ввода валидными данными
        with allure.step(f"Ввести фамилию: {group.surname}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-surname']").send_keys(group.surname)
        with allure.step(f"Ввести имя: {group.name}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-name']").send_keys(group.name)
        with allure.step(f"Ввести отчество: {group.secondname}"):
            wd.find_element(By.XPATH,
                            "//*[@id='form_cbase_admin_newClient_input_0_wizard[data][second_name]']").send_keys(
                group.secondname)
        with allure.step(f"Ввести дату рождения: {group.birthday}"):
            wd.find_element(By.XPATH, "//*[@id='form_cbase_admin_newClient_date_0__visible']").send_keys(
                group.birthday)
        with allure.step(f"Ввести телефон: {group.phone}"):
            wd.find_element(By.XPATH, "//*[@id='js-newrec-phone']").send_keys(group.phone)
        with allure.step(f"Выбрать 'Откуда о нас узнали' - {group.fromwhere}"):
            wd.find_element(By.XPATH, "//*[text()='Откуда о нас узнали']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.fromwhere)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)

    @allure.step("Подтвердить ввод данных")
    def submit_newpatient_creation(self):
        wd = self.app.wd
        # Подтвердить ввод данных
        if wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']") == 0:
            wd.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//*[@class='btn-default btn js-jump-step']").click()
        with allure.step("Нажать 'Готово'"):
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

    @allure.step("Редактировать фамилию пациента и сохранить")
    def edit_patient_surname(self, group):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'редактировать фамилию'"):
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        with allure.step(f"Ввести фамилию: {group.surname}"):
            wd.find_element(By.XPATH, "//*[@id='surname']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='surname']//input").send_keys(group.surname)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='surname']//span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p").text
        with allure.step(f"Проверка. Вводимое значение: {group.surname}. Сохраненное значение: {surname}"):
            assert group.surname == surname

    @allure.step("Сохранить фамилию пациента без изменений")
    def edit_patient_surname_fill(self, text):
        wd = self.app.wd
        with allure.step("Нажать 'редактировать' поле фамилия"):
            wd.find_element(By.XPATH, "//*[@data-key='surname'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='surname']//span[@class='input-group-btn']").click()
        surname = wd.find_element(By.XPATH, "//*[@id='surname']/p").text
        print("enter_data =", text, ";", "save_data =", surname)
        with allure.step(f"Проверка. Значение до редактирования: {text}. Значение после сохранения: {surname}"):
            assert text == surname

    @allure.step("Сохранить имя пациента без изменений")
    def edit_patient_name_fill(self):
        wd = self.app.wd
        name = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        with allure.step("Нажать кнопку редактировать поле имя"):
            wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        name_after = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        print("enter_data =", name, ";", "save_data =", name_after)
        with allure.step(f"Проверка. Значение до редактирования: {name}. Значение после сохранения: {name_after}"):
            assert name == name_after

    @allure.step("Сохранить отчество пациента без изменений")
    def edit_patient_secondname_fill(self):
        wd = self.app.wd
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p").text
        with allure.step("Нажать кнопку редактировать поле отчество"):
            wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname_aft = wd.find_element(By.XPATH, "//*[@id='second_name']/p").text
        print("enter_data =", secondname, ";", "save_data =", secondname_aft)
        with allure.step(f"Проверка. Значение до редактирования: {secondname}. "
                         f"Значение после сохранения: {secondname_aft}"):
            assert secondname == secondname_aft

    @allure.step("Редактировать и сохранить имя пациента")
    def edit_patient_name(self, group):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле имя"):
            wd.find_element(By.XPATH, "//*[@data-key='name'][@type='button']").click()
        with allure.step(f"Ввести имя: {group.name}"):
            wd.find_element(By.XPATH, "//*[@id='name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='name']//input").send_keys(group.name)
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='name']//span[@class='input-group-btn']").click()
        name = wd.find_element(By.XPATH, "//*[@id='name']/p").text
        print("enter_data =", group.name, ";", "save_data =", name)
        with allure.step(f"Проверка. Вводимое значение: {group.name}. Сохраненное значение: {name}"):
            assert group.name == name

    @allure.step("Редактировать и сохранить отчество пациента")
    def edit_patient_secondname(self, group):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле отчество"):
            wd.find_element(By.XPATH, "//*[@data-key='second_name'][@type='button']").click()
        with allure.step(f"Ввести значение: {group.secondname}"):
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='second_name']//input").send_keys(group.secondname)
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='second_name']//span[@class='input-group-btn']").click()
        secondname = wd.find_element(By.XPATH, "//*[@id='second_name']/p").text
        print("enter_data =", group.secondname, ";", "save_data =", secondname)
        with allure.step(f"Проверка. Вводимое значение: {group.secondname}. Сохраненное значение: {secondname}"):
            assert group.secondname == secondname

    @allure.step("Редактировать и сохранить дату рождения")
    def edit_patient_birthday(self, group):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле дата рождения"):
            wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        with allure.step(f"Ввести значение: {group.birthday}"):
            wd.find_element(By.XPATH, "//*[@id='birthday']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='birthday']//input").send_keys(group.birthday)
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        bd = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        birthday = bd[:10]
        print("enter_data =", group.birthday, ";", "save_data =", birthday)
        with allure.step(f"Проверка. Вводимое значение: {group.birthday}. Сохраненное значение: {birthday}"):
            assert group.birthday == birthday

    @allure.step("Сохранить дату рождения без изменений")
    def edit_patient_birthday_fill(self):
        wd = self.app.wd
        birthday = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        with allure.step("Нажать кнопку редактировать поле дата рождения"):
            wd.find_element(By.XPATH, "//*[@data-key='birthday'][@type='button']").click()
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='birthday']//span[@class='input-group-btn']").click()
        birthday_after = wd.find_element(By.XPATH, "//*[@id='birthday']/p").text
        print("enter_data =", birthday_after, ";", "save_data =", birthday)
        with allure.step(f"Проверка. Значение до редактирования: {birthday}. Значение после сохранения: {birthday}"):
            assert birthday_after in birthday

    @allure.step("Редактировать пол пациента и сохранить")
    def edit_patient_sex(self, sex):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать пол пациента"):
            wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        with allure.step(f"В выпадающем списке выбрать пол: {sex}"):
            select = Select(wd.find_element(By.XPATH, "//*[@id='sex']/div/select"))
            select.select_by_visible_text(sex)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_edit = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        print("enter_data =", sex_edit, ";", "save_data =", sex)
        with allure.step(f"Проверка. Выбранное значение: {sex}. Сохраненное значение: {sex_edit}"):
            assert sex_edit == sex

    @allure.step("Сохранить пол пациента без изменений")
    def edit_patient_sex_male_fill(self):
        wd = self.app.wd
        sex = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        with allure.step("Нажать кнопку редактировать пол"):
            wd.find_element(By.XPATH, "//*[@data-key='sex'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='sex']//span[@class='input-group-btn']").click()
        sex_after = wd.find_element(By.XPATH, "//*[@id='sex']/p[@data-key='sex']").text
        print("enter_data =", sex, ";", "save_data =", sex_after)
        with allure.step(f"Проверка. Значение до редактирования: {sex}. Значение после сохранения: {sex_after}"):
            assert sex == sex_after

    @allure.step("Редактировать инн и сохранить")
    def edit_patient_inn(self, inn):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле инн"):
            wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        with allure.step(f"Ввести значение: {inn}"):
            wd.find_element(By.XPATH, "//*[@id='inn']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='inn']//input").send_keys(inn)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        print("enter_data =", inn_edit, ";", "save_data =", inn)
        with allure.step(f"Проверка. Вводимое значение: {inn}. Сохраненное значение: {inn_edit}"):
            assert inn_edit == inn

    @allure.step("Сохранить инн без изменений")
    def edit_patient_inn_fill(self):
        wd = self.app.wd
        inn = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        with allure.step("Нажать кнопку редактировать поле инн"):
            wd.find_element(By.XPATH, "//*[@data-key='inn'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='inn']//span[@class='input-group-btn']").click()
        inn_edit = wd.find_element(By.XPATH, "//*[@id='inn']/p").text
        print("enter_data =", inn, ";", "save_data =", inn_edit)
        with allure.step(f"Проверка. Значение до редактирования: {inn}. Значение после сохранения: {inn_edit}"):
            assert inn == inn_edit

    @allure.step("Редактировать страну и сохранить значение")
    def edit_patient_country(self, country):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле 'Страна'"):
            wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        with allure.step(f"Ввести значение: {country}"):
            wd.find_element(By.XPATH, "//*[@id='country']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='country']//input").send_keys(country)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_edit = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        print("enter_data =", country_edit, ";", "save_data =", country)
        with allure.step(f"Проверка. Вводимое значение: {country}. Сохраненное значение: {country_edit}"):
            assert country_edit == country

    @allure.step("Сохранить поле 'Страна' без изменений")
    def edit_patient_country_fill(self):
        wd = self.app.wd
        country = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        with allure.step("Нажать кнопку редактировать поле страна"):
            wd.find_element(By.XPATH, "//*[@data-key='country'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='country']//span[@class='input-group-btn']").click()
        country_aft = wd.find_element(By.XPATH, "//*[@id='country']/p").text
        print("enter_data =", country, ";", "save_data =", country_aft)
        with allure.step(f"Проверка. Значение до редактирования: {country}. Значение после сохранения: {country_aft}"):
            assert country == country_aft

    @allure.step("Редактировать и сохранить почтовый индекс")
    def edit_patient_postcode(self, postcode):
        wd = self.app.wd
        with allure.step("Нажать кнопку редактировать поле почтовый индекс"):
            self.go_to_element_by_id(id_locator="postcode")
            self.id_double_click(click_id="postcode")
        # wd.find_element(By.XPATH, "//*[@data-key='postcode'][@type='button']").click()
        with allure.step(f"Ввести значение: {postcode}"):
            wd.find_element(By.XPATH, "//*[@id='postcode']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='postcode']//input").send_keys(postcode)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        print("enter_data =", postcode, ";", "save_data =", postcode_edit)
        with allure.step(f"Проверка. Вводимое значение: {postcode}. Сохраненное значение: {postcode_edit}"):
            assert postcode == postcode_edit

    def id_double_click(self, click_id):
        wd = self.app.wd
        button = wd.find_element(By.ID, click_id)
        ActionChains(wd).double_click(button).perform()

    @allure.step("Сохранить почтовый индекс без изменения")
    def edit_patient_postcode_none(self):
        wd = self.app.wd
        self.go_to_element_by_id(id_locator="postcode")
        postcode = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        with allure.step("Нажать кнопку редактировать почтовый индекс"):
            self.id_double_click(click_id="postcode")
        with allure.step("Нажать 'С'охранить'"):
            wd.find_element(By.XPATH, "//*[@id='postcode']//span[@class='input-group-btn']").click()
        postcode_edit = wd.find_element(By.XPATH, "//*[@id='postcode']/p").text
        print("enter_data =", postcode, ";", "save_data =", postcode_edit)
        with allure.step(f"Проверка. Значение до редактирования: {postcode}. "
                         f"Значение после сохранения: {postcode_edit}"):
            assert postcode == postcode_edit

    def scroll_to_element(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, 1000);")
        time.sleep(1)

    @allure.step("Редактировать и сохранить 'Область'")
    def edit_patient_state(self, state):
        wd = self.app.wd
        element = wd.find_element(By.ID, "state")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        with allure.step("Нажать кнопку редактировать поле 'Область'"):
            wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        with allure.step(f"Ввести значение: {state}"):
            wd.find_element(By.XPATH, "//*[@id='state']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='state']//input").send_keys(state)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        print("enter_data =", state, ";", "save_data =", state_edit)
        with allure.step(f"Проверка. Вводимое значение: {state}. Сохраненное значение: {state_edit}"):
            assert state == state_edit

    @allure.step("Сохранить 'Область' без редактирования")
    def edit_patient_state_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="state")
        # wd.execute_script("window.scrollTo(0,1600)")
        element = wd.find_element(By.ID, "state")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        state = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        with allure.step("Нажать кнопку редактировать поле 'Область'"):
            wd.find_element(By.XPATH, "//*[@data-key='state'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='state']//span[@class='input-group-btn']").click()
        state_edit = wd.find_element(By.XPATH, "//*[@id='state']/p").text
        print("enter_data =", state, ";", "save_data =", state_edit)
        with allure.step(f"Проверка. Значение до редактирования: {state}. Значение после сохранения: {state_edit}"):
            assert state == state_edit

    @allure.step("Редактировать и сохранить значение поля 'Город'")
    def edit_patient_city(self, city):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="city")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        with allure.step("Нажать кнопку редактировать поле 'Город'"):
            wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        with allure.step(f"Ввести значение: {city}"):
            wd.find_element(By.XPATH, "//*[@id='city']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='city']//input").send_keys(city)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        print("enter_data =", city_edit, ";", "save_data =", city)
        with allure.step(f"Проверка. Вводимое значение: {city}. Сохраненное значение: {city_edit}"):
            assert city_edit == city

    @allure.step("Сохранить значение поля 'Город'")
    def edit_patient_city_without_changes(self):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="city")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        city = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        with allure.step("Нажать редактировать поле 'Город'"):
            wd.find_element(By.XPATH, "//*[@data-key='city'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='city']//span[@class='input-group-btn']").click()
        city_edit = wd.find_element(By.XPATH, "//*[@id='city']/p").text
        print("enter_data =", city, ";", "save_data =", city_edit)
        with allure.step(f"Проверка. Значение до редактирования: {city}. Значение после сохранения: {city_edit}"):
            assert city == city_edit

    @allure.step("Редактировать и сохранить улицу")
    def edit_patient_street(self, street):
        wd = self.app.wd
        # self.scroll_to_element()
        # self.go_to_element_by_id(id_locator="street")
        element = wd.find_element(By.ID, "city")
        wd.execute_script("arguments[0].scrollIntoView(false);", element)
        time.sleep(1)
        with allure.step("Нажать кнопку редактировать поле улица"):
            wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        with allure.step(f"Ввести значение: {street}"):
            wd.find_element(By.XPATH, "//*[@id='street']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='street']//input").send_keys(street)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        print("enter_data =", street, ";", "save_data =", street_edit)
        with allure.step(f"Проверка. Вводимое значение: {street}. Сохраненное значение: {street_edit}"):
            assert street == street_edit

    @allure.step("Сохранить улицу без изменений")
    def edit_patient_street_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="street")
        street = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        with allure.step("Нажать кнопку редактировать улицу"):
            wd.find_element(By.XPATH, "//*[@data-key='street'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='street']//span[@class='input-group-btn']").click()
        street_edit = wd.find_element(By.XPATH, "//*[@id='street']/p").text
        print("enter_data =", street, ";", "save_data =", street_edit)
        with allure.step(f"Проверка. Значение до редактирования: {street}. Значение после сохранения: {street_edit}"):
            assert street == street_edit

    @allure.step("Редактировать и сохранить 'дом'")
    def edit_patient_building(self, building):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="building")
        with allure.step("Нажать кнопку редактировать поле дом"):
            wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        with allure.step(f"Ввести значение: {building}"):
            wd.find_element(By.XPATH, "//*[@id='building']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='building']//input").send_keys(building)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        print("enter_data =", building, ";", "save_data =", building_edit)
        with allure.step(f"Проверка. Вводимое значение: {building}. Сохраненное значение: {building_edit}"):
            assert building == building_edit

    @allure.step("Сохранить 'дом' без изменений")
    def edit_patient_building_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="building")
        building = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        with allure.step("Нажать кнопку редактировать поле 'дом'"):
            wd.find_element(By.XPATH, "//*[@data-key='building'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='building']//span[@class='input-group-btn']").click()
        building_edit = wd.find_element(By.XPATH, "//*[@id='building']/p").text
        print("enter_data =", building, ";", "save_data =", building_edit)
        with allure.step(f"Проверка. Значение до редактирования: {building}. "
                         f"Значение после сохранения: {building_edit}"):
            assert building == building_edit

    @allure.step("Редактировать и сохранить поле 'квартира'")
    def edit_patient_apartment(self, apt):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="apt")
        with allure.step("Нажать кнопку редактировать поле 'квартира'"):
            wd.find_element(By.XPATH, "//*[@data-key='apt'][@type='button']").click()
        with allure.step(f"Ввести значение: {apt}"):
            wd.find_element(By.XPATH, "//*[@id='apt']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='apt']//input").send_keys(apt)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='apt']//span[@class='input-group-btn']").click()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        print("enter_data =", apt, ";", "save_data =", apt_edit)
        with allure.step(f"Проверка. Вводимое значение: {apt}. Сохраненное значение: {apt_edit}"):
            assert apt == apt_edit

    @allure.step("Сохранить поле 'квартира' без изменений")
    def edit_patient_apartment_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="apt")
        apt = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        with allure.step("Нажать кнопку редактировать поле 'квартира'"):
            wd.find_element(By.XPATH, "//*[@data-key='apt'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='apt']//span[@class='input-group-btn']").click()
        apt_edit = wd.find_element(By.XPATH, "//*[@id='apt']/p").text
        print("enter_data =", apt, ";", "save_data =", apt_edit)
        with allure.step(f"Проверка. Значение до редактирования: {apt}. Значение после сохранения: {apt_edit}"):
            assert apt == apt_edit

    @allure.step("Редактировать и сохранить адрес пациента")
    def edit_patient_address(self, address):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="address")
        with allure.step("Нажать кнопку редактировать поле 'адрес'"):
            wd.find_element(By.XPATH, "//*[@data-key='address'][@type='button']").click()
        with allure.step(f"Ввести значение: {address}"):
            wd.find_element(By.XPATH, "//*[@id='address']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='address']//input").send_keys(address)
        with allure.step("Нажать Сохранить"):
            wd.find_element(By.XPATH, "//*[@id='address']//span[@class='input-group-btn']").click()
            assert wd.find_elements(By.XPATH, "//div[@class='input-group has-error']") == 0
        address_edit = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        with allure.step(f"Проверка. Вводимое значение: {address}. Сохраненное значение: {address_edit}"):
            assert address == address_edit

    @allure.step("Сохранить адрес без изменений")
    def edit_patient_address_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="address")
        address = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        with allure.step("Нажать кнопку редактировать поле 'адрес'"):
            wd.find_element(By.XPATH, "//*[@data-key='address'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='address']//span[@class='input-group-btn']").click()
        address_edit = wd.find_element(By.XPATH, "//*[@id='address']/p").text
        print("enter_data =", address, ";", "save_data =", address_edit)
        with allure.step(f"Проверка. Значение до редактирования: {address}. Значение после сохранения: {address_edit}"):
            assert address == address_edit

    @allure.step("Редактировать и сохранить дату первого приема")
    def edit_patient_first_data(self, date):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_first_appointment")
        with allure.step("Нажать кнопку редактировать поле 'дата первого приема'"):
            wd.find_element(By.XPATH, "//*[@data-key='date_of_first_appointment'][@type='button']").click()
        with allure.step(f"Ввести значение: {date}"):
            wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//input").send_keys(date)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        print("enter_data =", date, ";", "save_data =", date_edit)
        with allure.step(f"Проверка. Вводимое значение: {date}. Сохраненное значение: {date_edit}"):
            assert date == date_edit

    @allure.step("Сохранить дату первого приема без изменений")
    def edit_patient_first_data_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_first_appointment")
        date = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        with allure.step("Нажать кнопку редактировать поле 'дата первой записи'"):
            wd.find_element(By.XPATH, "//*[@data-key='date_of_first_appointment'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='date_of_first_appointment']/p").text
        print("enter_data =", date, ";", "save_data =", date_edit)
        with allure.step(f"Проверка. Значение до редактирования: {date}. Значение после сохранения: {date_edit}"):
            assert date == date_edit

    @allure.step("Редактировать и сохранить дату последнего приема")
    def edit_patient_last_data(self, date):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_last_appointment")
        with allure.step("Нажать кнопку редактировать поле 'дата последней записи'"):
            wd.find_element(By.XPATH, "//*[@data-key='date_of_last_appointment'][@type='button']").click()
        with allure.step(f"Ввести значение: {date}"):
            wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//input").send_keys(date)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        print("enter_data =", date, ";", "save_data =", date_edit)
        with allure.step(f"Проверка. Вводимое значение: {date}. Сохраненное значение: {date_edit}"):
            assert date_edit == date

    @allure.step("Сохранить дату последнего посещения без изменений")
    def edit_patient_last_data_none(self):
        wd = self.app.wd
        # self.scroll_to_element()
        self.go_to_element_by_id(id_locator="date_of_last_appointment")
        data = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        with allure.step("Нажать кнопку редактировать поле 'дата последнего посещения'"):
            wd.find_element(By.XPATH, "//*[@data-key='date_of_last_appointment'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='date_of_last_appointment']/p").text
        print("enter_data =", data, ";", "save_data =", date_edit)
        with allure.step(f"Проверка. Значение до редактирования: {data}. Значение после сохранения: {date_edit}"):
            assert date_edit == data

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
        wd.find_element(By.XPATH, "//*[@class='mb-10']"
                                  "//text()[contains(.,'VIP')]/preceding-sibling::span//*[@type='button']").click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        if len(wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")) != 0:
            marks = wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")
            names = [e.text for e in marks]
            print(f"Список отметок пациента: {names}")
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
