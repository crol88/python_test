import random
import time
import datetime
from datetime import timedelta

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ScheduleHelper:

    def __init__(self, app):
        self.app = app

    def open_schedule(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[.='Расписание на день']")) == 0:
            wd.find_element(By.XPATH, "//*[@href='/visits/schedule/index']").click()
        # check = wd.find_element(By.XPATH, "//*[@href='/visits/schedule/index']").get_attribute('class')
        # if check != "active":
        #     schedule = wd.find_element(By.XPATH, "//*[@href='/visits/schedule/index']")
        #     time.sleep(2)
        #     schedule.click()
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

    def add_record(self):
        wd = self.app.wd

    def add_test_record(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(10)
        element.click()
        time.sleep(10)

    def open_record_form(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()
        record_form = wd.find_elements(By.XPATH, "//h4[.='Запись пациента']")
        assert record_form != 0

    def open_new_record_form(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[25]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()
        record_form = wd.find_elements(By.XPATH, "//h4[.='Запись пациента']")
        assert record_form != 0

    def open_new_patient_form(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[.='Новый пациент']").click()
        time.sleep(2)
        new = wd.find_element(By.XPATH, "//label[.='Новый пациент']")
        assert new != 0

    def fill_new_patient_form(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@id='client_surname']").send_keys(group.surname)
        wd.find_element(By.XPATH, "//input[@id='client_name']").send_keys("New")
        wd.find_element(By.XPATH, "//input[@id='client_second-name']").send_keys("Patient")
        wd.find_element(By.XPATH, "//input[@id='client_number']").click()
        wd.find_element(By.XPATH, "//input[@id='client_number']").send_keys("79081421617")
        wd.find_element(By.XPATH, "//input[@class='form-control birthday-datepicker']").click()
        wd.find_element(By.XPATH, "//input[@class='form-control birthday-datepicker']").send_keys("10.12.1990")
        wd.find_element(By.XPATH, "//span[.='Мужской']").click()
        from_where = wd.find_elements(By.XPATH, "//select[@id='client_id-fromWhere']/option")
        name = [e.text for e in from_where]
        del name[0]
        r = random.choice(name)
        select = Select(wd.find_element(By.XPATH, "//select[@id='client_id-fromWhere']"))
        select.select_by_visible_text(r)
        wd.find_element(By.XPATH, "//button[.='Сохранить пациента']").click()

    def fill_new_patient_record(self):
        wd = self.app.wd
        priem_list = wd.find_elements(By.XPATH, "//div[@class='doctor-form-body']/div[2]/select/option")
        priem = [e.text for e in priem_list]
        del priem[0]
        # print(priem)
        r = random.choice(priem)
        select = Select(wd.find_element(By.XPATH, "//div[@class='doctor-form-body']/div[2]/select"))
        select.select_by_visible_text(r)
        select_time = Select(wd.find_element(By.XPATH, "//div[@class='doctor-form-body']/div[3]/select"))
        select_time.select_by_value('60')
        element = wd.find_element(By.XPATH, "//div[.='Second N.S.']/parent::div/following-sibling::div//div[17]")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()

    def check_task_dnd(self, locator):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[contains(text(),'%s')]" % locator)) != 0:
            element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
        print("//div[contains(text(),'%s')]" % locator)
        return len(wd.find_elements(By.XPATH, "//div[contains(text(),'%s')]" % locator))

    def check_fill_schedule(self, group):
        wd = self.app.wd
        sys_date = str(datetime.date.today().strftime('%d.%m.%y'))
        locator = f"{sys_date} / {group.surname}"
        if len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)) != 0:
            print("//div[contains(@data-original-title,'%s')]/small" % locator)
            element = wd.find_element(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator)
            wd.execute_script("arguments[0].scrollIntoView();", element)
        return len(wd.find_elements(By.XPATH, "//div[contains(@data-original-title,'%s')]/small" % locator))

    def hold_record(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Удалить или отложить запись']").click()
        del_rec = wd.find_element(By.XPATH, "//h4[.='Вы действительно хотите удалить запись?']")
        assert del_rec != 0
        select = Select(wd.find_element(By.XPATH, "//select[@name='reason']"))
        select.select_by_visible_text('Отложенная запись')
        time.sleep(2)
        wd.find_element(By.XPATH, "//button[@type='submit']").click()

    def task_panel_navigation(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(2)
        nav = wd.find_elements(By.XPATH, "//li[@role='presentation']")
        name = [e.text for e in nav]
        print(name)
        assert name == ['Информация о пациенте', 'Копировать', 'Амбулаторная карта', 'План лечения', 'Заполнить анкету',
                        'Пациент пришёл', 'Отметить результат посещения', 'Перенести запись',
                        'Удалить или отложить запись', 'Запланировать посещение', 'Отправить СМС', 'Оплатить']
        element.click()

    def tp_patient_information(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(2)
        wd.find_element(By.XPATH, "//li[.='Информация о пациенте']").click()
        client_info = wd.find_element(By.XPATH, "//a[@id='client_info-tab']/parent::li").get_attribute('class')
        assert client_info == "active"

    def tp_paticard(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Амбулаторная карта']").click()
        time.sleep(2)
        paticard = wd.find_element(By.XPATH, "//div[contains(text(),'Амбулаторные записи пациента')]").text
        print(paticard[:28])
        paticard_page = paticard[:28]
        assert paticard_page == "Амбулаторные записи пациента"

    def mark_visit_result(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Отметить результат посещения']").click()
        modal_header = wd.find_element(By.XPATH, "//h4[.='Отметить результат посещения']").text
        assert modal_header == "Отметить результат посещения"
        self.modal_close()

    def modal_close(self):
        wd = self.app.wd
        modal_close = wd.find_element(By.XPATH, "//button[@class='modalClose']")
        if modal_close != 0:
            modal_close.click()

    def tp_delete_record(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Удалить или отложить запись']").click()
        del_rec = wd.find_element(By.XPATH, "//h4[.='Вы действительно хотите удалить запись?']")
        assert del_rec != 0
        self.modal_close()

    def tp_send_sms(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Отправить СМС']").click()
        sms = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
        assert sms == "Отправить смс"
        self.modal_close()

    def tp_copy_form(self, locator):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[contains(text(),'%s')]/ancestor:: div[@class='taskDnD']" % locator)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wd.find_element(By.XPATH, "//li[.='Копировать']").click()
        copy_form = wd.find_element(By.XPATH, "//h4[@class='modalHeading']").text
        assert copy_form == "Копировать запись"
        self.modal_close()
