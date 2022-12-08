import time
import datetime
from datetime import timedelta
import random
import pathlib
from model.group import Group
from model.group import Chair
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EmployeesHelper:

    def __init__(self, app):
        self.app = app

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

    def add_user(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/boss/ajax.json?action=newUser']").click()
        assert len(wd.find_elements(By.XPATH, "//*[.='Добавить пользователя']")) > 0

    def add_chair(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title)) == 0:
            wd.find_element(By.XPATH, "//*[@href='/boss/forms/chair_add']").click()
            wd.find_element(By.ID, "form_boss_forms_chair_add_input_0_name").send_keys(group.title)
            wd.find_element(By.XPATH, "//input[@id='form_boss_forms_chair_add_number_0_']").send_keys(group.sorting)
            wd.find_element(By.ID, "s2id_form_boss_forms_chair_add_select_0_").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(group.department)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
            wd.find_element(By.ID, "s2id_form_boss_forms_chair_add_select_1_").click()
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.filial)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
            wd.find_element(By.XPATH, "//button[@class='btn-success btn']").click()

    def delete_chair(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//td[.='%s']/following-sibling::td//button" % group.title).click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Удалить']").click()

    def get_chair_list(self):
        wd = self.app.wd
        chair_list = wd.find_elements(By.XPATH, "//table[@class='table table-hover js-table-sort']/tbody/tr")
        print("Кол-во кресел в списке:", len(chair_list))
        return chair_list

    def check_chair(self, group):
        wd = self.app.wd
        chair = wd.find_element(By.XPATH, "//td[.='%s']" % group.title).text
        chair_info = wd.find_elements(By.XPATH, "//td[.='%s']/parent::tr/td" % group.title)
        names = [e.text for e in chair_info]
        names.pop(-1)
        print("Данные кресла при добавлении:", names, "*", "Проверка наименования кресла в списке:", chair)
        assert chair in names

    def fill_new_user_form(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@name='login']").clear()
        wd.find_element(By.XPATH, "//*[@name='login']").send_keys(group.login)
        wd.find_element(By.XPATH, "//*[@name='surname']").clear()
        wd.find_element(By.XPATH, "//*[@name='surname']").send_keys(group.surname)
        wd.find_element(By.XPATH, "//*[@name='name']").clear()
        wd.find_element(By.XPATH, "//*[@name='name']").send_keys(group.name)
        wd.find_element(By.XPATH, "//*[@name='secondname']").clear()
        wd.find_element(By.XPATH, "//*[@name='secondname']").send_keys(group.secondname)
        wd.find_element(By.XPATH, "//*[@name='password']").clear()
        wd.find_element(By.XPATH, "//*[@name='password']").send_keys("123456")
        wd.find_element(By.XPATH, "//*[@name='mail']").clear()
        wd.find_element(By.XPATH, "//*[@name='mail']").send_keys(group.mail)
        wd.find_element(By.XPATH, "//*[@name='phone']").clear()
        wd.find_element(By.XPATH, "//*[@name='phone']").send_keys(group.phone)
        wd.find_element(By.CSS_SELECTOR, ".selenium-branches > ul >li >input").clear()
        wd.find_element(By.CSS_SELECTOR, ".selenium-branches > ul >li >input").send_keys("Филиал 1")
        wd.find_element(By.CSS_SELECTOR, ".selenium-branches > ul >li >input").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys("Врач")
        wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(3)
        if len(wd.find_elements(By.ID, "error")) > 0:
            name = str(datetime.datetime.now().strftime('%d-%m-%Y_%H-%M') + '.png')
            capture_path = str(pathlib.Path.cwd() / 'screenshots' / name)
            wd.save_screenshot(capture_path)
            wd.find_element(By.CLASS_NAME, "modalClose").click()
        wd.find_element(By.XPATH, "//*[@class='form-control js-search-text']").clear()
        wd.find_element(By.XPATH, "//*[@class='form-control js-search-text']").send_keys(group.login)
        time.sleep(1)
        new_user_login = wd.find_element(By.XPATH, "//*[.='%s']" % group.login).text
        print("Логин указанный при создании пользователя:", group.login, "*", "Проверка логина в базе:", new_user_login)
        assert group.login == new_user_login

    def delete_user(self, group):
        wd = self.app.wd
        user = wd.find_element(By.XPATH, "//*[.='%s']" % group.login).text
        wd.find_element(By.XPATH, "//*[.='%s']/following-sibling::*[@class='text-right']//button[@title='']"
                        % group.login).click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        time.sleep(1)
        assert len(wd.find_elements(By.XPATH, "//*[.='%s']" % group.login)) == 0
        print("Пользователь", user, "удален")

    def add_doctor(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@href='/boss/ajax.json?action=addDoctor']").click()
        # select = Select(wd.find_element(By.ID, "user"))
        # select.select_by_visible_text(group.login)
        wd.find_element(By.ID, "s2id_user").click()
        wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").clear()
        wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").send_keys(group.login)
        wd.find_element(By.XPATH, "//div[@id='select2-drop']/div/input").send_keys(Keys.ENTER)

    def delete_doctor(self, group):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,1000)")
        time.sleep(3)
        wd.find_element(By.XPATH, "//td[contains(text(),'%s')]/following-sibling::td//button" % group.surname).click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Удалить']").click()

    def add_department(self, department):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@id='s2id_group']").click()
        wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys(department)
        wd.find_element(By.XPATH, "//*[@id='s2id_group']//input").send_keys(Keys.ENTER)
        # all_dep = wd.find_elements(By.XPATH, "//*[@id='group']/option")
        # names = [e.text for e in all_dep]
        # print(names)
        # # select = Select(wd.find_element(By.XPATH, "//*[@id='group']"))
        # # select.select_by_value('2')
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[@class='modalClose']").click()

    def add_user_step(self, group):
        self.open_employees_users()
        self.add_user()
        self.fill_new_user_form(group)

    def add_doctor_step(self, group, department):
        self.open_employees_doctor()
        self.add_doctor(group)
        self.add_department(department)

    def add_chair_step(self, group):
        self.open_employees_chair()
        self.add_chair(group)

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
        return len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.login))

    def chair_availability(self, group):
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
        return len(wd.find_elements(By.XPATH, "//td[.='%s']" % group.title))

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
        return len(wd.find_elements(By.XPATH, "//td[contains(text(),'%s')]" % group.surname))

    def schedule_availability(self, group):
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
            if len(wd.find_elements(By.XPATH, "//div[.='График работы врачей']/parent::div[@class='headbarLeft']")) == 0:
                wd.find_element(By.XPATH, "//*[.='График работы врачей']/parent::a").click()
        return len(wd.find_elements(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname))

    def check_doc_schedule(self, group):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        doc = wd.find_element(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname).text
        print("Врач добавленный в расписание:", doc[:-5])
        assert group.surname == doc[:-5]

    def add_schedule_step(self):
        if self.schedule_availability(Group(surname="Surname")) == 0:
            if self.chair_availability(Chair(title="test-chair")) == 0:
                self.add_chair(
                    Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
            if self.doctor_availability(Group(surname="Surname")) == 0:
                self.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                                 login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))
                self.open_employees_doctor()
                self.add_doctor(Group(login="new-user-test"))
                self.add_department(department="Терапевты")
        # self.check_doc_schedule(Group(surname="Surname"))

    def fill_doc_schedule(self, group):
        wd = self.app.wd
        sys_date = str(datetime.date.today().strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        print(locator)
        element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        doc = element.get_attribute("data-original-title")
        print("Открыто расписание врача:", doc)
        time.sleep(1)
        wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        assert locator == doc[:-5]
        assert len(wd.find_elements(By.XPATH, "//h4[.='Установить график на день']")) != 0

    def fill_doc_schedule_tomorrow(self, group):
        wd = self.app.wd
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        # print(locator)
        element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        doc = element.get_attribute("data-original-title")
        print("Открыто расписание врача:", doc)
        time.sleep(2)
        wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        assert locator == doc[:-5]
        assert len(wd.find_elements(By.XPATH, "//h4[.='Установить график на день']")) != 0

    def fill_date_picker(self):
        wd = self.app.wd
        # Заполнить начало периода
        start = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_0_']")
        start_value = start.get_attribute("value")
        sys_date = str(datetime.date.today().strftime('%Y-%m-%d'))
        print("Текущая дата:", sys_date, "=", "Начало периода:", start_value)
        assert start_value == sys_date
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
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    def fill_date_picker_tomorrow(self):
        wd = self.app.wd
        # Заполнить начало периода
        start = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_0_']")
        start_value = start.get_attribute("value")
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%Y-%m-%d'))
        print("Текущая дата:", sys_date, "=", "Начало периода:", start_value)
        assert start_value == sys_date
        # Заполнить конец периода
        end = wd.find_element(By.XPATH, "//input[@id='form_stompro_admin_dayGraphWizard_date_1_']")
        end_value = end.get_attribute("value")
        print("Текущая дата:", sys_date, "=", "Конец периода:", end_value)
        assert end_value == sys_date
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    def fill_chair_selection(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.title)
        wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
        # # wd.find_element(By.XPATH,
        # #                 "//input[contains(@aria-activedescendant,'select2-result-label')]").send_keys(group.title)
        # wd.find_element(By.XPATH,
        #                 "//input[contains(@aria-activedescendant,'select2-result-label')]").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    def default_interval_selection(self, group):
        wd = self.app.wd
        if group.s_time is not None:
            wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(group.s_time)
            wd.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        # a = wd.find_elements(By.XPATH, "//select[@id='form_stompro_admin_dayGraphWizard_select_0_']/option")
        # names = [e.get_attribute('textContent') for e in a]

    def default_schedule_correction(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()

    def schedule_confirm(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        time.sleep(1)
        result = wd.find_element(By.XPATH, "//div[.='График работы врача сохранен.']").text
        assert result == "График работы врача сохранен."
        wd.find_element(By.XPATH, "//a[@class='btn-default btn js-done-step']").click()

    def fill_graph_day_form(self, group):
        self.fill_chair_selection(group)
        self.default_interval_selection(group)
        self.default_schedule_correction()
        self.schedule_confirm()

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

    def delete_day_doc_schedule(self, group):
        wd = self.app.wd
        sys_date = str((datetime.date.today() + timedelta(days=1)).strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        time.sleep(2)
        print(locator)
        if len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)) != 0:
            wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]" % locator).click()
        wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").click()
        interval = wd.find_elements(By.XPATH, "//ul[@class='select2-results']/li/div")
        names = [e.text for e in interval]
        select_filial = Select(wd.find_element(By.XPATH, "//select[@id='form_stompro_admin_dayGraphWizard_select_0_']"))
        select_filial.select_by_visible_text(names[1])
        time.sleep(1)
        txt = wd.find_element(By.XPATH, "//div[@id='s2id_form_stompro_admin_dayGraphWizard_select_0_']").text
        del_int_time = txt[-17:]
        assert names[1] == txt
        wd.find_element(By.XPATH, "//button[.='Удалить']").click()
        t = wd.find_element(By.XPATH, "//div[@class='alert alert-success']").text
        int_time_next = t[-17:]
        # print(del_int_time, "*", int_time_next)
        assert del_int_time == int_time_next
        wd.find_element(By.XPATH, "//button[@data-step='done']").click()
        alert = wd.find_element(By.XPATH, "//div[@class='alert alert-success']").text
        assert alert == "График работы врача сохранен."

