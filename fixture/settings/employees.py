import time
import datetime
import random
from model.group import Group

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EmployeesHelper:

    def __init__(self, app):
        self.app = app

    def open_employees_users(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[.='Пользователи']/parent::a").click()

    def open_employees_chair(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[.='Кресла']/parent::a").click()

    def open_employees_doctor(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        wd.find_element(By.XPATH, "//*[.='Сотрудники']/parent::div").click()
        time.sleep(1)
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
            wd.find_element(By.ID, "form_boss_forms_chair_add_input_1_sort").send_keys(group.sorting)
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
        wd.find_element(By.XPATH, "//*[@name='surname']").send_keys("Surname")
        wd.find_element(By.XPATH, "//*[@name='name']").clear()
        wd.find_element(By.XPATH, "//*[@name='name']").send_keys("Name")
        wd.find_element(By.XPATH, "//*[@name='secondname']").clear()
        wd.find_element(By.XPATH, "//*[@name='secondname']").send_keys("Secondname")
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

    def count(self, group):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//*[.='%s']" % group.login)) == 0:
            b = wd.find_element(By.XPATH,
                                "//*[@alt='Пациенты']/parent::div/parent::div/parent::div").get_attribute("class")
            if str(b) == "link subMenuOpen active":
                wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
            wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
            wd.find_element(By.XPATH, "//*[text()='Список пациентов']").click()
        return len(wd.find_elements(By.LINK_TEXT, group.login))






