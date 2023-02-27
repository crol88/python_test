import time
import datetime
import allure
from datetime import timedelta
import pathlib
from model.group import Group
from model.group import Chair
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EmployeesHelper:

    def __init__(self, app):
        self.app = app

    @allure.step("Открыть 'Настройки/Сотрудники/Пользователи'")
    def open_employees_users(self):
        wd = self.app.wd
        # Настройки
        if len(wd.find_elements(By.XPATH, "//div[.='Пользователи']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Пользователи']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Пользователи']/parent::a").click()

    @allure.step("Перейти в модуль «Сотрудники», в открывающемся списке выбираем пункт – «Кресла»")
    def open_employees_chair(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Кресла']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen"
                                              " sidebarSpecialIcon active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Кресла']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Кресла']/parent::a").click()

    @allure.step("Перейти в раздел «Настройки» - «Сотрудники» - «Врачи»")
    def open_employees_doctor(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Врачи']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen"
                                              " sidebarSpecialIcon active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Врачи']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Врачи']/parent::a").click()

    @allure.step("Открыть настройки графика врачей")
    def open_schedule_set(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//*[@class='breadcrumb']//li[.='График работы врачей']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
            b = wd.find_element(By.XPATH,
                                "//span[.='Расписание']/parent::div[@role='button']").get_attribute("aria-expanded")
            if str(b) == "false":
                wd.find_element(By.XPATH, "//span[.='Расписание']/parent::div[@role='button']").click()
            time.sleep(1)
            if len(wd.find_elements(By.XPATH,
                                    "//div[.='График работы врачей']/parent::div[@class='headbarLeft']")) == 0:
                wd.find_element(By.XPATH, "//*[.='График работы врачей']/parent::a").click()

    @allure.step("Нажать «Добавить пользователя»")
    def add_user(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/boss/ajax.json?action=newUser']").click()
        assert len(wd.find_elements(By.XPATH, "//*[.='Добавить пользователя']")) > 0

    @allure.step("Добавить кресло")
    def add_chair(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title)) == 0:
            with allure.step("Нажать 'Добавить кресло'"):
                wd.find_element(By.XPATH, "//*[@href='/boss/forms/chair_add']").click()
            with allure.step(f"Ввести название: {group.title}"):
                wd.find_element(By.ID, "form_boss_forms_chair_add_input_0_name").send_keys(group.title)
            with allure.step(f"Ввести сортировку: {group.sorting}"):
                wd.find_element(By.XPATH, "//input[@id='form_boss_forms_chair_add_number_0_']").send_keys(group.sorting)
            with allure.step(f"Ввести отделение: {group.department}"):
                wd.find_element(By.ID, "s2id_form_boss_forms_chair_add_select_0_").click()
                wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.department)
                wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
            with allure.step(f"Ввести филиал: {group.filial}"):
                wd.find_element(By.ID, "s2id_form_boss_forms_chair_add_select_1_").click()
                wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.filial)
                wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
            with allure.step("Сохранить введенные данные"):
                wd.find_element(By.XPATH, "//button[@class='btn-success btn']").click()

    @allure.step("Удалить кресло")
    def delete_chair(self, group):
        wd = self.app.wd
        with allure.step(f"Нажать кнопку удалить на кресле: {group.title}"):
            wd.find_element(By.XPATH, "//td[.='%s']/following-sibling::td//button" % group.title).click()
        time.sleep(1)
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//button[.='Удалить']").click()
        time.sleep(2)
        with allure.step(f"Проверка. Кресло {group.title} отсутствует в системе"):
            assert len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title)) == 0

    def get_chair_list(self):
        wd = self.app.wd
        chair_list = wd.find_elements(By.XPATH, "//table[@class='table table-hover js-table-sort']/tbody/tr")
        print("Кол-во кресел в списке:", len(chair_list))
        return chair_list

    @allure.step("Проверить добавление кресла")
    def check_chair(self, group):
        wd = self.app.wd
        with allure.step(f"В настройках системы добавлено кресло: {group.title}"):
            chair = wd.find_element(By.XPATH, "//td[.='%s']" % group.title).text
            chair_info = wd.find_elements(By.XPATH, "//td[.='%s']/parent::tr/td" % group.title)
            names = [e.text for e in chair_info]
            names.pop(-1)
            print("Данные кресла при добавлении:", names, "*", "Проверка наименования кресла в списке:", chair)
            assert chair in names

    @allure.step("Заполнить форму добавления нового пользователя")
    def fill_new_user_form(self, group):
        wd = self.app.wd
        with allure.step(f"Ввести логин: {group.login}"):
            wd.find_element(By.XPATH, "//*[@name='login']").clear()
            wd.find_element(By.XPATH, "//*[@name='login']").send_keys(group.login)
        with allure.step(f"Ввести фамилию: {group.surname}"):
            wd.find_element(By.XPATH, "//*[@name='surname']").clear()
            wd.find_element(By.XPATH, "//*[@name='surname']").send_keys(group.surname)
        with allure.step(f"Ввести имя: {group.name}"):
            wd.find_element(By.XPATH, "//*[@name='name']").clear()
            wd.find_element(By.XPATH, "//*[@name='name']").send_keys(group.name)
        with allure.step(f"Ввести отчество: {group.secondname}"):
            wd.find_element(By.XPATH, "//*[@name='secondname']").clear()
            wd.find_element(By.XPATH, "//*[@name='secondname']").send_keys(group.secondname)
        with allure.step(f"Ввести пароль"):
            wd.find_element(By.XPATH, "//*[@name='password']").clear()
            wd.find_element(By.XPATH, "//*[@name='password']").send_keys("123456")
        with allure.step(f"Ввести почту: {group.mail}"):
            wd.find_element(By.XPATH, "//*[@name='mail']").clear()
            wd.find_element(By.XPATH, "//*[@name='mail']").send_keys(group.mail)
        with allure.step(f"Ввести телефон: {group.phone}"):
            wd.find_element(By.XPATH, "//*[@name='phone']").clear()
            wd.find_element(By.XPATH, "//*[@name='phone']").send_keys(group.phone)
        time.sleep(1)
        filials = wd.find_elements(By.XPATH, "//select[@name='branches[]']/option")
        filial_list = [e.text for e in filials]
        filial = filial_list[0]
        time.sleep(1)
        with allure.step(f"Выбрать филиал: {filial}"):
            select = Select(wd.find_element(By.XPATH, "//select[@name='branches[]']"))
            select.select_by_visible_text(filial)
        with allure.step(f"Выбрать группу пользователя: {group.user_group}"):
            wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys(group.user_group)
            wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys(Keys.ENTER)
        with allure.step(f"Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(3)
        if len(wd.find_elements(By.ID, "error")) > 0:
            name = str(datetime.datetime.now().strftime('%d-%m-%Y_%H-%M') + '.png')
            capture_path = str(pathlib.Path.cwd() / 'screenshots' / name)
            wd.save_screenshot(capture_path)
            wd.find_element(By.CLASS_NAME, "modalClose").click()
        time.sleep(1)
        with allure.step(f"Проверка. Пользователь {group.login} добавлен в систему"):
            assert len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.login)) > 0

    @allure.step("Удалить пользователя")
    def delete_user(self, group):
        wd = self.app.wd
        with allure.step(f"Нажать на кнопку 'Удалить' у пользователя с логином: {group.login}"):
            user = wd.find_element(By.XPATH, "//*[.='%s']" % group.login).text
            wd.find_element(By.XPATH, "//*[.='%s']/following-sibling::*[@class='text-right']//button[@title='']"
                            % group.login).click()
        time.sleep(1)
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        time.sleep(1)
        with allure.step(f"Проверка. Пользователь {group.login} удален из системы"):
            assert len(wd.find_elements(By.XPATH, "//*[.='%s']" % group.login)) == 0
        print("Пользователь", user, "удален")

    @allure.step("Добавить пользователю группу 'Врач'")
    def add_doctor(self, group):
        wd = self.app.wd
        self.open_employees_doctor()
        with allure.step("Нажать 'Добавить'"):
            wd.find_element(By.XPATH, "//a[.='Добавить']").click()
        with allure.step(f"Выбрать пользователя: {group.surname}"):
            wd.find_element(By.XPATH, "//div[@class='select2-container js-select2']").click()
            wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").clear()
            time.sleep(1)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").send_keys(group.surname)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").send_keys(Keys.ENTER)
        with allure.step(f"Выбрать отделение: {group.department}"):
            wd.find_element(By.XPATH, "//label[contains(text(),'Отделения врача')]/following-sibling::input")\
                .send_keys(group.department)
            wd.find_element(By.XPATH, "//label[contains(text(),'Отделения врача')]/following-sibling::input")\
                .send_keys(Keys.ENTER)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(1)

    @allure.step("Удалить врача")
    def delete_doctor(self, group):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,1000)")
        time.sleep(3)
        with allure.step(f"Нажать 'Удалить' врача {group.surname}"):
            wd.find_element(By.XPATH,
                            "//td[contains(text(),'%s')]/following-sibling::td//button" % group.surname).click()
        time.sleep(1)
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//button[.='Удалить']").click()

    @allure.step("Выбор отделения")
    def add_department(self, department):
        wd = self.app.wd
        with allure.step(f"Выбрать отделение: {department}"):
            wd.find_element(By.XPATH, "//label[contains(text(),'Отделения врача')]/following-sibling::input").send_keys(
                department)
            wd.find_element(By.XPATH, "//label[contains(text(),'Отделения врача')]/following-sibling::input").send_keys(
                Keys.ENTER)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(1)

    @allure.step("Добавить в систему нового пользователя")
    def add_user_step(self, group):
        self.open_employees_users()
        self.add_user()
        self.fill_new_user_form(group)

    def add_doctor_step(self, group, department):
        self.open_employees_doctor()
        self.add_doctor(group)
        # self.add_department(department)

    def add_chair_step(self, group):
        self.open_employees_chair()
        self.add_chair(group)

    @allure.step("Перейти в раздел «Настройки» - «Сотрудники» - «Пользователи»")
    def user_availability(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Пользователи']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Пользователи']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Пользователи']/parent::a").click()
        if len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.login)) > 0:
            with allure.step(f"Пользователь {group.login} уже присутствует в системе"):
                print(f"Пользователь {group.login} уже присутствует в системе")
        return len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.login))

    @allure.step("Перейти в модуль «Сотрудники», в открывающемся списке выбираем пункт – «Кресла»")
    def chair_availability(self, group):
        wd = self.app.wd
        # with allure.step(f"Проверить наличие кресла '{group.title}'"):
        if len(wd.find_elements(By.XPATH, "//div[.='Кресла']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen"
                                              " sidebarSpecialIcon active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Кресла']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Кресла']/parent::a").click()
        if len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title)) > 0:
            with allure.step(f"Кресло {group.title} уже присутствует в системе"):
                print(f"Кресло {group.title} уже присутствует в системе")
            # if len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title)) == 0:
            #     with allure.step(f"Кресло {group.title} отсутствует в системе"):
            #         print(f"Кресло {group.title} отсутствует в системе")
        return len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title))

    @allure.step("Перейти в раздел «Настройки» - «Сотрудники» - «Врачи»")
    def doctor_availability(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Врачи']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen"
                                              " sidebarSpecialIcon active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Сотрудники']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Врачи']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Врачи']/parent::a").click()
        # if len(wd.find_elements(By.XPATH, "//td[contains(text(),'%s')]" % group.surname)) > 0:
        #     with allure.step(f"Пользователь {group.surname} уже присутствует в системе"):
        #         print(f"Пользователь {group.surname} уже присутствует в системе")
        # if len(wd.find_elements(By.XPATH, "//td[contains(text(),'%s')]" % group.surname)) == 0:
        #     with allure.step(f"Пользователь {group.surname} с ролью врача отсутствует в системе"):
        #         print(f"Пользователь {group.surname} с ролью врача отсутствует в системе")
        return len(wd.find_elements(By.XPATH, "//td[contains(text(),'%s')]" % group.surname))

    # @allure.step("Генерация тестовых данных. График работы врачей'")
    def schedule_availability(self, group):
        wd = self.app.wd
        # with allure.step(f"Проверить в графике наличие врача: '{group.surname}'"):
        if len(wd.find_elements(By.XPATH, "//*[@class='breadcrumb']//li[.='График работы врачей']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
            b = wd.find_element(By.XPATH,
                                "//span[.='Расписание']/parent::div[@role='button']").get_attribute("aria-expanded")
            if str(b) == "false":
                wd.find_element(By.XPATH, "//span[.='Расписание']/parent::div[@role='button']").click()
            time.sleep(1)
            if len(wd.find_elements(By.XPATH,
                                    "//div[.='График работы врачей']/parent::div[@class='headbarLeft']")) == 0:
                wd.find_element(By.XPATH, "//*[.='График работы врачей']/parent::a").click()
            if len(wd.find_elements(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname)) > 0:
                with allure.step(f"Врач {group.surname} уже добавлен в график работы"):
                    print(f"Врач {group.surname} уже добавлен в график работы")
                # if len(wd.find_elements(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname)) == 0:
                #     with allure.step(f"Врач {group.surname} отсутствует в графике работы"):
                #         print(f"Врач {group.surname} отсутствует в графике работы")
            return len(wd.find_elements(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname))

    @allure.step("Проверка. Добавление врача в график работы")
    def check_doc_schedule(self, group):
        wd = self.app.wd
        self.open_schedule_set()
        element = wd.find_element(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        with allure.step(f"Врач {group.surname} добавлен в график работы"):
            doc = wd.find_element(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname).text
            print("Врач добавленный в расписание:", doc[:-5])
            assert group.surname == doc[:-5]

    @allure.step("Генерация тестовых данных")
    def add_schedule_step(self):
        if self.schedule_availability(Group(surname="Surname")) == 0:
            if self.chair_availability(Chair(title="test-chair")) == 0:
                self.add_chair(
                    Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
            if self.doctor_availability(Group(surname="Surname")) == 0:
                self.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                         login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))
                self.open_employees_doctor()
                self.add_doctor(Group(surname="Surname"))
                # self.add_department(department="Терапевты")
                self.open_schedule_set()
        # self.check_doc_schedule(Group(surname="Surname"))

    @allure.step("Генерация тестовых данных")
    def add_alt_schedule_step(self):
        if self.schedule_availability(Group(surname="Second")) == 0:
            if self.chair_availability(Chair(title="second-test-chair")) == 0:
                self.add_chair(
                    Chair(title="second-test-chair", sorting="10", department="Терапевты", filial="Филиал 1"))
            if self.doctor_availability(Group(surname="Second")) == 0:
                self.add_user_step(Group(surname="Second", name="Name", secondname="Secondname",
                                         login='Second-user-test', mail='Secondmail@mail.ru', phone='79041871136'))
                self.open_employees_doctor()
                self.add_doctor(Group(surname="Second", department="Терапевты"))
                # self.add_department(department="Терапевты")
                self.open_schedule_set()
        # self.check_doc_schedule(Group(surname="Surname"))

    def alt_schedule_step(self):
        if self.schedule_availability(Group(surname="Surtest")) == 0:
            if self.chair_availability(Chair(title="dnd-test-chair")) == 0:
                self.add_chair(
                    Chair(title="dnd-test-chair", sorting="11", department="Терапевты", filial="Филиал 1"))
            if self.doctor_availability(Group(surname="Surtest")) == 0:
                self.add_user_step(Group(surname="Surtest", name="Name", secondname="Secondname",
                                         login='Surtest-user-test', mail='Surtest@mail.ru', phone='79041874682'))
                self.open_employees_doctor()
                self.add_doctor(Group(surname="Surtest", department="Терапевты"))
                # self.add_department(department="Терапевты")
                self.open_schedule_set()

    @allure.step("Генерация тестовых данных")
    def edit_schedule_step(self):
        if self.schedule_availability(Group(surname="Suredit")) == 0:
            if self.chair_availability(Chair(title="edit_sched-chair")) == 0:
                self.add_chair(
                    Chair(title="edit_sched-chair", sorting="14", department="Терапевты", filial="Филиал 1"))
            if self.doctor_availability(Group(surname="Surtest")) == 0:
                self.add_user_step(Group(surname="Suredit", name="Sur", secondname="Edit",
                                         login='Suredit-test', mail='Suredit@mail.ru', phone='79041871793'))
                self.open_employees_doctor()
                self.add_doctor(Group(surname="Suredit", department="Терапевты"))
                # self.add_department(department="Терапевты")
                self.open_schedule_set()

    @allure.step("Открыть форму установки графика")
    def fill_doc_schedule(self, group):
        wd = self.app.wd
        sys_date = str(datetime.date.today().strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        print("//div[contains(@data-original-title,'%s')]" % locator)
        element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator)
        time.sleep(2)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        doc = element.get_attribute("data-original-title")
        print("Открыто расписание врача:", doc)
        time.sleep(2)
        # wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        element.click()
        assert locator == doc[:-5]
        assert len(wd.find_elements(By.XPATH, "//h4[.='Установить график на день']")) != 0
        # return len(wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator))

    @allure.step("Установить график работы на день")
    def fill_doc_schedule_tomorrow(self, group):
        wd = self.app.wd
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        # print(locator)
        with allure.step(f"Выбрать график врача {group.surname} на дату {sys_date}"):
            element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            doc = element.get_attribute("data-original-title")
            print("Открыто расписание врача:", doc)
            time.sleep(2)
            wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
            assert locator == doc[:-5]
            assert len(wd.find_elements(By.XPATH, "//h4[.='Установить график на день']")) != 0

    @allure.step("Выбор даты")
    def fill_date_picker(self):
        wd = self.app.wd
        with allure.step("Ввести начало периода"):
            # Заполнить начало периода
            start = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_0_']")
            start_value = start.get_attribute("value")
            sys_date = str(datetime.date.today().strftime('%Y-%m-%d'))
            print("Текущая дата:", sys_date, "=", "Начало периода:", start_value)
            assert start_value == sys_date
        with allure.step("Ввести конец периода"):
            # Заполнить конец периода
            end = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_1_']")
            end_value = end.get_attribute("value")
            print("Текущая дата:", sys_date, "=", "Конец периода:", end_value)
            assert end_value == sys_date
        # Выбрать врача
        # select = Select(wd.find_elements(By.XPATH, "//select[@name='wizard[data][doctorID]']//option"))
        # select.select_by_visible_text("Surname N.S.")
        # all_dep = wd.find_elements(By.XPATH, "//select[@name='wizard[data][doctorID]']//option")
        # names = [e.text for e in all_dep]
        # print(names)
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    @allure.step("Выбор даты")
    def fill_date_picker_tomorrow(self):
        wd = self.app.wd
        # Заполнить начало периода
        start = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_0_']")
        start_value = start.get_attribute("value")
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%Y-%m-%d'))
        with allure.step(f"Дата начала периода: {start_value}"):
            print("Текущая дата:", sys_date, "=", "Начало периода:", start_value)
        assert start_value == sys_date
        # Заполнить конец периода
        end = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_1_']")
        end_value = end.get_attribute("value")
        with allure.step(f"Дата конца периода: {end_value}"):
            print("Текущая дата:", sys_date, "=", "Конец периода:", end_value)
        assert end_value == sys_date
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    @allure.step("Выбор кресла")
    def fill_chair_selection(self, group):
        wd = self.app.wd
        with allure.step(f"Выбрать кресло: {group.title}"):
            wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
            time.sleep(1)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.title)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    @allure.step("Выбор интервала")
    def default_interval_selection(self, group):
        wd = self.app.wd
        if group.s_time is not None:
            with allure.step("Если интервал указан, то выбрать значения"):
                wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
                wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.s_time)
                wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        # a = wd.find_elements(By.XPATH, "//select[@id='form_stompro_admin_dayGraphWizard_select_0_']/option")
        # names = [e.get_attribute('textContent') for e in a]

    @allure.step("Корректировка графика")
    def default_schedule_correction(self):
        wd = self.app.wd
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    @allure.step("Сохранить график работы")
    def schedule_confirm(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        time.sleep(1)
        result = wd.find_element(By.XPATH, "//div[.='График работы врача сохранен.']").text
        assert result == "График работы врача сохранен."
        wd.find_element(By.XPATH, "//a[@class='btn-default btn js-done-step']").click()

    @allure.step("Заполнить форму установки графика на день")
    def fill_graph_day_form(self, group):
        self.fill_chair_selection(group)
        self.default_interval_selection(group)
        self.default_schedule_correction()
        self.schedule_confirm()

    @allure.step("Проверить заполнение расписания")
    def day_graph_availability(self, group):
        wd = self.app.wd
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        # print(locator)
        if len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)) != 0:
            element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            # doc = element.get_attribute("data-original-title")
            # print("Открыто расписание врача:", doc)
            # time.sleep(1)
            # wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        return len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator))

    @allure.step("Удаление расписания врача на день")
    def delete_day_doc_schedule(self, group):
        wd = self.app.wd
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        print(locator)
        with allure.step(f"Нажать на расписание врача {locator}"):
            if len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)) != 0:
                wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        with allure.step("Выбрать интервал"):
            wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
            interval = wd.find_elements(By.XPATH, "//ul[@class='select2-results']/li/div")
            names = [e.text for e in interval]
            select_in = Select(wd.find_element(By.XPATH, "//select[@id='form_stompro_admin_dayGraphWizard_select_0_']"))
            select_in.select_by_visible_text(names[1])
            time.sleep(1)
            txt = wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").text
            del_int_time = txt[-17:]
            assert names[1] == txt
        with allure.step("Нажать 'Удалить'"):
            wd.find_element(By.XPATH, "//div[@class='modal-body']//button[.='Удалить']").click()
            t = wd.find_element(By.XPATH, "//div[@class='alert alert-success']").text
            int_time_next = t[-17:]
            # print(del_int_time, "*", int_time_next)
            assert del_int_time == int_time_next
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//button[@data-step='done']").click()
            alert = wd.find_element(By.XPATH, "//div[@class='alert alert-success']").text
            assert alert == "График работы врача сохранен."
        with allure.step("Нажать 'Готово'"):
            wd.find_element(By.XPATH, "//a[@class='btn-default btn js-done-step']").click()

    def fill_first_schedule(self):
        self.alt_schedule_step()
        self.fill_doc_schedule(Group(surname="Surtest"))
        self.fill_date_picker()
        self.fill_chair_selection(Chair(title="dnd-test-chair"))
        self.default_interval_selection(Group(s_time="13:00"))
        self.default_schedule_correction()
        self.schedule_confirm()

    @allure.step("Создать тестовые данные")
    def fill_second_schedule(self):
        self.add_alt_schedule_step()
        self.fill_doc_schedule(Group(surname="Second"))
        self.fill_date_picker()
        self.fill_chair_selection(Chair(title="second-test-chair"))
        self.default_interval_selection(Group(s_time="10:00"))
        self.default_schedule_correction()
        self.schedule_confirm()

    @allure.step("Создать тестовые данные")
    def fill_edit_schedule(self):
        self.edit_schedule_step()
        self.fill_doc_schedule(Group(surname="Suredit"))
        self.fill_date_picker()
        self.fill_chair_selection(Chair(title="edit_sched-chair"))
        self.default_interval_selection(Group(s_time="10:00"))
        self.default_schedule_correction()
        self.schedule_confirm()
