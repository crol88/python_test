import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
from model.info import Info


class InformationHelper:

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

    def open_additional_info(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, "Дополнительная информация").click()

    def edit_comments(self, comments):
        wd = self.app.wd
        self.open_additional_info()
        wd.find_element(By.XPATH, "//*[@data-key='comments'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='comments']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='comments']//input").send_keys(comments)
        wd.find_element(By.XPATH, "//*[@id='comments']//span[@class='input-group-btn']").click()
        comments_edit = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        print("comments =", comments, ";", "comments_edit =", comments_edit)
        assert comments == comments_edit

    def edit_comments_none(self):
        wd = self.app.wd
        self.open_additional_info()
        comments = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='comments'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='comments']//span[@class='input-group-btn']").click()
        comments_edit = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        print("comments =", comments, ";", "comments_edit =", comments_edit)
        assert comments == comments_edit

    def edit_first_record_date(self, date):
        wd = self.app.wd
        self.open_additional_info()
        wd.find_element(By.XPATH, "//*[@data-key='first_record_date'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='first_record_date']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='first_record_date']//input").send_keys(date)
        wd.find_element(By.XPATH, "//*[@id='first_record_date']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        print("date =", date, ";", "date_edit =", date_edit)
        assert date == date_edit

    def edit_first_record_date_none(self):
        wd = self.app.wd
        self.open_additional_info()
        date = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='first_record_date'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='first_record_date']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        print("date =", date, ";", "date_edit =", date_edit)
        assert date == date_edit

    def edit_id1c(self, id1c):
        wd = self.app.wd
        self.open_additional_info()
        wd.find_element(By.XPATH, "//*[@data-key='id1c'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='id1c']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='id1c']//input").send_keys(id1c)
        wd.find_element(By.XPATH, "//*[@id='id1c']//span[@class='input-group-btn']").click()
        id1c_edit = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        print("id1c =", id1c, ";", "id1c_edit =", id1c_edit)
        assert id1c == id1c_edit

    def edit_id1c_none(self):
        wd = self.app.wd
        self.open_additional_info()
        id1c = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='id1c'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='id1c']//span[@class='input-group-btn']").click()
        id1c_edit = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        print("id1c =", id1c, ";", "id1c_edit =", id1c_edit)
        assert id1c == id1c_edit

    def edit_fromwhere(self):
        # wd = self.app.wd
        # self.open_additional_info()
        self.get_fromwhere_value()

    def get_fromwhere_value(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "id_fromwhere")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='id_fromwhere'][@type='button']").click()
        fromwhere_groups = []
        for element in wd.find_elements(By.XPATH, "//*[@id='id_fromwhere']//select/option"):
            value = element.get_attribute("value")
            fromwhere_groups.append(Info(value=value))
            print(fromwhere_groups)
        return fromwhere_groups

    # def select_random_fromwhere(self):
