import random
import time
import datetime
from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime
from datetime import timedelta


class ScheduleHelper:

    def __init__(self, app):
        self.app = app

    @allure.step("Открыть расписание на день")
    def open_schedule(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Расписание на день']")) == 0:
            wd.find_element(By.XPATH, "//*[@href='/visits/schedule/index']").click()
        time.sleep(1)
        status = wd.find_element(By.XPATH, "//*[@href='/visits/schedule/index']").get_attribute('class')
        assert status == "active"

    def check_schedule_date(self):
        wd = self.app.wd
        dp_date = wd.find_element(By.XPATH, "//*[@class='datetimepickerWrapper']/input").get_attribute('value')
        time.sleep(1)
        sys_date = str(datetime.date.today().strftime('%d.%m.%Y'))
        print("Дата DP:", dp_date, "*", "Дата системы:", sys_date)
        assert dp_date == sys_date

    def schedule_new_patient(self):
        self.open_schedule()
        self.open_record_form()
        self.open_new_patient_form()

    def schedule_edit_new_patient(self):
        self.open_schedule()
        self.open_record_form_edit()
        self.open_new_patient_form()

    def select_doctor_schedule(self):
        wd = self.app.wd
        doctor = wd.find_elements(By.XPATH, "//*[@class='header-title']")
        names = [e.text for e in doctor]
        random_doctor = random.choice(names)
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(random_doctor)
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(Keys.ENTER)
        time.sleep(1)
        search = wd.find_element(By.XPATH, "//*[@class='css-1rhbuit-multiValue react-select__multi-value']").text
        assert random_doctor == search
        doc_after = wd.find_element(By.XPATH, "//*[@class='header-title']").text
        print("Выбранный доктор:", random_doctor, "*", "Отображается в поле ввода:", search, "*",
              "Отображается расписание врача:", doc_after)
        assert random_doctor == doc_after
        wd.find_element(By.XPATH, "//*[@class='react-select__indicators css-1wy0on6']/div[1]").click()

    def select_multiple_doctors(self):
        wd = self.app.wd
        doctor = wd.find_elements(By.XPATH, "//*[@class='header-title']")
        names = [e.text for e in doctor]
        random_doctor = random.sample(names, 3)
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(random_doctor[0])
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(random_doctor[1])
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(Keys.ENTER)
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(random_doctor[2])
        wd.find_element(By.XPATH, "//*[@class='react-select__input']").send_keys(Keys.ENTER)
        time.sleep(1)
        all_doc = wd.find_elements(By.XPATH, "//*[@class='header-title']")
        doc_names = [e.text for e in all_doc]
        print("Отображается расписание врачей:", doc_names)
        assert random_doctor[0] in doc_names
        assert random_doctor[1] in doc_names
        assert random_doctor[2] in doc_names
        wd.find_element(By.XPATH, "//*[@class='react-select__indicators css-1wy0on6']/div[1]").click()

    def open_setting_departments(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[.='Отделения']/parent::a").click()

    def check_all_departments(self):
        wd = self.app.wd
        all_groups = wd.find_elements(By.XPATH, "//*[@class='filter-groups']/button")
        names = [e.text for e in all_groups]
        names.remove("Все")
        print(names)
        self.open_setting_departments()
        all_dep = wd.find_elements(By.XPATH, "//*[@class='table table-hover']/tbody/tr/td[2]")
        dep = [e.text for e in all_dep]
        print(dep)
        assert names == dep

    def select_random_department(self):
        wd = self.app.wd
        all_groups = wd.find_elements(By.XPATH, "//*[@class='filter-groups']/button")
        del all_groups[0]
        random_dep = random.choice(all_groups)
        random_dep.click()
        print(random_dep.text)
        time.sleep(1)
        random_pick = wd.find_elements(By.XPATH, "//*[@class='column-header js-sticky']/div")
        n = [e.text for e in random_pick]
        print(str(n))
        assert random_dep.text in str(n)
        wd.find_element(By.XPATH, "//*[@class='react-select__indicators css-1wy0on6']/div[1]").click()

    def new_patient_record(self):
        wd = self.app.wd
        all_groups = wd.find_elements(By.XPATH, "//*[@class='filter-groups']/button")
        del all_groups[0]
        random_dep = random.choice(all_groups)
        random_dep.click()
        print(random_dep.text)

    @allure.step("Выбрать пациента")
    def select_patient(self, group):
        wd = self.app.wd
        with allure.step(f"Ввести фамилию пациента: {group.surname}"):
            wd.find_element(By.XPATH, "//div[@class=' css-nsoqb2']/input").send_keys(group.surname)
            time.sleep(6)
        with allure.step(f"В результате поиска выбрать пациента {group.surname}"):
            wd.find_element(By.XPATH, "//*[contains(@id,'option-0')]").click()
            time.sleep(1)
        # wd.find_element(By.ID, "react-select-3-option-0").click()
        # pick = wd.find_elements(By.XPATH, "//div[contains(@id,'option')]")
        # n = [e.get_attribute('id') for e in pick]
        # print(n)

    def add_test_record(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(10)
        element.click()
        time.sleep(10)

    @allure.step("Открыть форму записи пациента")
    def open_record_form(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()
        record_form = wd.find_elements(By.XPATH, "//h4[.='Запись пациента']")
        assert record_form != 0

    def open_record_form_edit(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Suredit S.E.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()
        record_form = wd.find_elements(By.XPATH, "//h4[.='Запись пациента']")
        assert record_form != 0

    @allure.step("Открыть форму записи пациента у ранее выбранного врача")
    def open_new_record_form(self, timehelper):
        wd = self.app.wd
        element = wd.find_element(By.XPATH,
                                  "//div[.='Second N.S.']/parent::div/following-sibling::div//div[%s]" % timehelper)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(8)
        element.click()
        record_form = wd.find_elements(By.XPATH, "//h4[.='Запись пациента']")
        assert record_form != 0

    @allure.step("Нажать 'Новый пациент'")
    def open_new_patient_form(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[.='Новый пациент']").click()
        time.sleep(2)
        new = wd.find_element(By.XPATH, "//label[.='Новый пациент']")
        assert new != 0

    @allure.step("Заполнить форму добавления нового пациента")
    def fill_new_patient_form(self, group):
        wd = self.app.wd
        with allure.step(f"Ввести фамилию: {group.surname}"):
            wd.find_element(By.XPATH, "//input[@id='client_surname']").send_keys(group.surname)
        with allure.step("Ввести имя: New"):
            wd.find_element(By.XPATH, "//input[@id='client_name']").send_keys("New")
        with allure.step("Ввести фамилию: Patient"):
            wd.find_element(By.XPATH, "//input[@id='client_second-name']").send_keys("Patient")
        with allure.step("Ввести телефон: 79081421617"):
            wd.find_element(By.XPATH, "//input[@id='client_number']").click()
            wd.find_element(By.XPATH, "//input[@id='client_number']").send_keys("79081421617")
        with allure.step("Ввести дату рождения: 10.12.1990"):
            wd.find_element(By.XPATH, "//input[@class='form-control birthday-datepicker']").click()
            wd.find_element(By.XPATH, "//input[@class='form-control birthday-datepicker']").send_keys("10.12.1990")
        with allure.step("Выбрать пол"):
            wd.find_element(By.XPATH, "//span[.='Мужской']").click()
        with allure.step(f"Выбрать 'Откуда о нас узнали'"):
            from_where = wd.find_elements(By.XPATH, "//select[@id='client_id-fromWhere']/option")
            name = [e.text for e in from_where]
            del name[0]
            r = random.choice(name)
            select = Select(wd.find_element(By.XPATH, "//select[@id='client_id-fromWhere']"))
            select.select_by_visible_text(r)
            time.sleep(8)
        if len(wd.find_elements(By.XPATH, "//div[@class='row duplicate-search']//button")) > 0:
            wd.find_element(By.XPATH, "//div[@class='row duplicate-search']//button[1]").click()
            time.sleep(8)
        try:
            with allure.step("Нажать 'Сохранить пациента'"):
                save = wd.find_element(By.XPATH, "//button[.='Сохранить пациента']")
                wd.execute_script("arguments[0].scrollIntoView();", save)
                time.sleep(2)
                wd.find_element(By.XPATH, "//button[.='Сохранить пациента']").click()
        except NoSuchElementException:
            print("Найден дубликат пациента")

    @allure.step("Заполнить форму записи пациента")
    def fill_new_patient_record(self):
        wd = self.app.wd
        with allure.step("Выбрать прием"):
            priem_list = wd.find_elements(By.XPATH, "//div[@class='doctor-form-body']/div[2]/select/option")
            time.sleep(2)
            priem = [e.get_attribute('textContent') for e in priem_list]
            time.sleep(2)
            print(priem)
            del priem[0]
            time.sleep(1)
            r = random.choice(priem)
            select = Select(wd.find_element(By.XPATH, "//div[@class='doctor-form-body']/div[2]/select"))
            select.select_by_visible_text(r)
        with allure.step("Выбрать продолжительность приема"):
            select_time = Select(wd.find_element(By.XPATH, "//div[@class='doctor-form-body']/div[3]/select"))
            select_time.select_by_value('60')
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//button[.='Сохранить']").click()

    @allure.step("Проверить наличие записи в расписании")
    def check_task_dnd(self, locator):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[contains(text(),'%s')]" % locator)) != 0:
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
        print("//div[contains(text(),'%s')]" % locator)
        return len(wd.find_elements(By.XPATH, "//div[contains(text(),'%s')]" % locator))

    @allure.step("Проверить график работы врача на текущую дату")
    def check_fill_schedule(self, group):
        wd = self.app.wd
        with allure.step(f"Проверить график работы врача '{group.surname}' на текущую дату"):
            now = datetime.now()
            # sys_date = str(datetime.date.today().strftime('%d.%m.%y'))
            sys_date = now.strftime('%d.%m.%y')
            locator = f"{sys_date} / {group.surname}"
            if len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)) != 0:
                print("//div[contains(@data-original-title,'%s')]/small" % locator)
                element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)
                wd.execute_script("arguments[0].scrollIntoView();", element)
            return len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator))

    @allure.step("Отложенная запись")
    def hold_record(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на запись в расписании пациента {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor::div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В меню выбрать 'Удалить или отложить запись'"):
            wd.find_element(By.XPATH, "//li[.='Удалить или отложить запись']").click()
        del_rec = wd.find_element(By.XPATH, "//h4[.='Вы действительно хотите удалить запись?']")
        assert del_rec != 0
        with allure.step("Выбрать причину выписки: Отложенная запись"):
            select = Select(wd.find_element(By.XPATH, "//select[@name='reason']"))
            select.select_by_visible_text('Отложенная запись')
        time.sleep(2)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//button[@type='submit']").click()

    @allure.step("Проверить навигацию записи в расписании")
    def task_panel_navigation(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на запись в расписании пациента {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        time.sleep(2)
        with allure.step("Проверить список навигации"):
            nav = wd.find_elements(By.XPATH, "//li[@role='presentation']")
            name = [e.text for e in nav]
            print(name)
            # assert name == ['Информация о пациенте', 'Копировать', 'Амбулаторная карта', 'План лечения',
            #                 'Заполнить анкету', 'Пациент пришёл', 'Отметить результат посещения', 'Перенести запись',
            #                 'Удалить или отложить запись', 'Запланировать посещение', 'Отправить СМС', 'Оплатить']
        with allure.step("Закрыть карту приема"):
            element.click()

    @allure.step("Информация о пациенте")
    def tp_patient_information(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor::div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        time.sleep(2)
        with allure.step("В открывшемся окне нажать 'Информация о пациенте'"):
            inf = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor::div[@class='taskDnD']" % locator)
            time.sleep(2)
            wd.execute_script("arguments[0].scrollIntoView();", inf)
            time.sleep(2)
            wd.find_element(By.XPATH, "//li[.='Информация о пациенте']").click()
        with allure.step(f"Переадресация в инфокарту пациента 'Информация о пациенте {locator}'"):
            client_info = wd.find_element(By.XPATH, "//a[@id='client_info-tab']/parent::li").get_attribute('class')
            assert client_info == "active"

    @allure.step("Амбулаторная карта")
    def tp_paticard(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]"
                                                "/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            # element.click()
            time.sleep(2)
            wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator).click()
        with allure.step("В открывшемся окне нажать 'Амбулаторная карта'"):
            wd.find_element(By.XPATH, "//li[.='Амбулаторная карта']").click()
        time.sleep(2)
        with allure.step(f"Переадресация в амбулаторные записи пациента: {locator}"):
            paticard = wd.find_element(By.XPATH, "//div[contains(text(),'Амбулаторные записи пациента')]").text
            print(paticard[:28])
            paticard_page = paticard[:28]
            assert paticard_page == "Амбулаторные записи пациента"

    @allure.step("Отметить результат посещения")
    def mark_visit_result(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Отметить результат посещения'"):
            wd.find_element(By.XPATH, "//li[.='Отметить результат посещения']").click()
        with allure.step(f"Открывается модальное окно с формой для отметки результата посещения пациента: {locator}"):
            modal_header = wd.find_element(By.XPATH, "//h4[.='Отметить результат посещения']").text
            assert modal_header == "Отметить результат посещения"
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    def modal_close(self):
        wd = self.app.wd
        modal_close = wd.find_element(By.XPATH, "//button[@class='modalClose']")
        if modal_close != 0:
            modal_close.click()

    @allure.step("Открыть форму удаления записи")
    def tp_delete_record(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Удалить или отложить запись'"):
            wd.find_element(By.XPATH, "//li[.='Удалить или отложить запись']").click()
        with allure.step(f"Открывается модальное окно c формой удаления записи пациента: {locator}"):
            del_rec = wd.find_element(By.XPATH, "//h4[.='Вы действительно хотите удалить запись?']")
            assert del_rec != 0
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    @allure.step("Открыть форму отправки СМС")
    def tp_send_sms(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor::div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Отправить СМС'"):
            wd.find_element(By.XPATH, "//li[.='Отправить СМС']").click()
        with allure.step(f"Открывается модальное окно с формой отправки СМС пациента: {locator}"):
            sms = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
            assert sms == "Отправить смс"
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    @allure.step("Открыть форму копирования записи")
    def tp_copy_form(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Копировать'"):
            wd.find_element(By.XPATH, "//li[.='Копировать']").click()
        with allure.step(f"Открывается модальное окно с формой копирования записи пациента: {locator}"):
            copy_form = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
            assert copy_form == "Копировать запись"
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    @allure.step("План лечения")
    def tp_open_medblock(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'План лечения'"):
            wd.find_element(By.XPATH, "//li[.='План лечения']").click()
        time.sleep(2)
        with allure.step(f"Переадресация в план лечения пациента: {locator}"):
            medblock = wd.find_element(By.XPATH, "//div[@class='pageTitle js-page-title']").text
            assert medblock == "Зубная формула"

    @allure.step("Пациент пришел")
    def tp_patient_came(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH,
                                      "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Пациент пришел'"):
            wd.find_element(By.XPATH, "//li[.='Пациент пришёл']").click()
        time.sleep(2)
        with allure.step(f"Открывается модальное окно с формой 'Пациент пришел' пациента: {locator}"):
            patient_came = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
            assert patient_came == "Пациент пришёл"
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    @allure.step("")
    def tp_move_record(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Перенести запись'"):
            wd.find_element(By.XPATH, "//li[.='Перенести запись']").click()
        time.sleep(2)
        with allure.step(f"Открывается модальное окно с формой переноса записи для пациента: {locator}"):
            move_rec = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
            assert move_rec == "Перенести запись"
        with allure.step("Закрыть модальное окно"):
            self.modal_close()

    @allure.step("Запланировать посещение через расписание")
    def tp_plan_visit(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Запланировать посещение'"):
            wd.find_element(By.XPATH, "//li[.='Запланировать посещение']").click()
        time.sleep(2)
        with allure.step(f"Переадресация на страницу планирования пациента: {locator}"):
            visit = wd.find_element(By.XPATH, "//div[@class='pageTitle js-page-title']").text
            visit_page = visit[:12]
            print(visit_page)
            assert visit_page == "Планирование"

    @allure.step("Оплатить")
    def pay(self, locator):
        wd = self.app.wd
        with allure.step(f"Нажать на ранее созданную запись в расписании {locator}"):
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        with allure.step("В открывшемся окне нажать 'Оплатить'"):
            wd.find_element(By.XPATH, "//li[.='Оплатить']").click()
        time.sleep(2)
        with allure.step(f"Переадресация в кассу пациента: {locator}"):
            pay = wd.find_element(By.XPATH, "//div[@class='pageTitle js-page-title']").text
            assert pay == "Касса"

    @allure.step("Редактировать график в расписании")
    def edit_mode(self):
        wd = self.app.wd
        with allure.step("Нажать 'Режим редактирования'"):
            wd.find_element(By.XPATH, "//a[@class='btn btn-default js-scheduler-edit']").click()
        with allure.step("Нажать 'Редактировать график' у ранне созданного врача"):
            element = wd.find_element(By.XPATH, "//div[contains(@title,'Suredit S.E. - ')]/following-sibling::div/a")
            wd.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        time.sleep(1)
        with allure.step("Выбрать начало работы"):
            select_start = Select(wd.find_element(By.XPATH, "//select[@name='start']"))
            select_start.select_by_visible_text('14:00')
        time.sleep(1)
        with allure.step("Выбрать окончание работы"):
            select_end = Select(wd.find_element(By.XPATH, "//select[@name='end']"))
            select_end.select_by_visible_text('20:00')
        with allure.step("Сохранить изменения"):
            wd.find_element(By.XPATH, "//button[@type='submit']").click()
        self.open_schedule_set()
        with allure.step("Проверить внесение изменений в графике работы врачей"):
            work_time = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'Suredit S.E.')]/div["
                                                  "@class='text-nowrap text-bold']").text
            start_time = work_time[:5]
            end_time = work_time[-5:]
            assert start_time == "14:00", end_time == "20:00"
        self.open_schedule()
        time.sleep(1)
        with allure.step("Закрыть режим редактирования"):
            wd.find_element(By.XPATH, "//a[@class='btn btn-default js-scheduler-edit active']").click()

    @allure.step("Открыть 'Настройки/Расписание/График работы врачей'")
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

    @allure.step("Добавить служебную запись")
    def open_service_record_form(self, surname):
        wd = self.app.wd
        with allure.step("Нажать 'Служебная запись'"):
            wd.find_element(By.XPATH, "//button[@title='Служебная запись']").click()
        with allure.step(f"Ввести фамилию врача: {surname}"):
            wd.find_element(By.XPATH, "//ul[@class='select2-choices']//input").send_keys(surname)
            wd.find_element(By.XPATH, "//ul[@class='select2-choices']//input").send_keys(Keys.ENTER)
        with allure.step("Выбрать тип записи"):
            select = Select(wd.find_element(By.XPATH, "//select[@name='wizard[data][type_id]']"))
            select.select_by_visible_text("Учеба")
        with allure.step("Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        time.sleep(2)
        empty_field = wd.find_elements(By.XPATH, "//*[.='Поле обязательное для заполнения.']")
        error = wd.find_elements(By.XPATH, "//*[@role='alert']")
        if len(empty_field) or len(error) > 0:
            wd.find_element(By.XPATH, "//button[@class='modalClose']").click()
        with allure.step("Выбор места. Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        # определить время начала
        now = datetime.now()
        time_1 = (now + timedelta(hours=1)).strftime("%H")
        t_start = f"{time_1}:00"
        with allure.step(f"Выбор диапазона. Выбрать время начала: {t_start}"):
            print("время:", t_start)
            time_start = Select(wd.find_element(By.XPATH, "//select[@name='wizard[data][timeStart]']"))
            time_start.select_by_visible_text(t_start)
        # определить время окончания
        time_2 = (now + timedelta(hours=2)).strftime("%H")
        t_end = f"{time_2}:00"
        with allure.step(f"Выбор диапазона. Выбрать время окончания: {t_end}"):
            print("время:", t_end)
            time_end = Select(wd.find_element(By.XPATH, "//select[@name='wizard[data][timeEnd]']"))
            time_end.select_by_visible_text(t_end)
        with allure.step("Выбор диапазона. Нажать 'Далее'"):
            wd.find_element(By.XPATH, "//button[@class='btn-default btn js-jump-step']").click()
        time.sleep(5)
        with allure.step(f"Служебная запись добавлена в расписание врача {surname} "):
            tp = wd.find_elements(By.XPATH, "//span[contains(text(),'%s')]/ancestor::div[@class='columns-col']//div["
                                            ".='Учеба']" % surname)
            print("//span[contains(text(),'%s')]/ancestor::div[@class='columns-col']//div[.='Учеба']" % surname)
            assert tp != 0

    @allure.step("Проверить тестовые данные в расписании")
    def check_schedule_test_data(self, surname):
        wd = self.app.wd
        locator = wd.find_elements(By.XPATH, "//span[contains(text(),'%s')]" % surname)
        print("//span[contains(text(),'%s')]" % surname)
        return len(locator)

    def tp_dnd(self):
        wd = self.app.wd
        # wd.switch_to.frame(wd.find_element(By.XPATH, "(//div[@class='columns-col'])[6]"))
        drag = wd.find_element(By.XPATH, "(//div[@draggable='true'])[10]")
        # print("//span[contains(text(),'%s')]/ancestor::div[@class='columns-col']//div[@class='taskDnD']" % surname)
        # drop = wd.find_element(By.XPATH, "(//div[@role='presentation'])[234]/div")
        ActionChains(wd).drag_and_drop_by_offset(drag, 1400, 785)
        time.sleep(5)
