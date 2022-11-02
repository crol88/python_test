import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random


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
        if wd.find_element(By.XPATH, "//*[@class='sweet-content']"):
            error = wd.find_element(By.XPATH, "//*[@class='sweet-content']")
            print("Ошибка:", error.text)
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
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
        time.sleep(1)
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
        time.sleep(1)
        id1c = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='id1c'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='id1c']//span[@class='input-group-btn']").click()
        id1c_edit = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        print("id1c =", id1c, ";", "id1c_edit =", id1c_edit)
        assert id1c == id1c_edit

    def edit_fromwhere(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "id_fromwhere")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='id_fromwhere'][@type='button']").click()

    def select_random_fromwhere(self):
        wd = self.app.wd
        from_where = wd.find_elements(By.XPATH, "//*[@id='id_fromwhere']//select/option")
        names = [e.text for e in from_where]
        random_name = random.choice(names)
        select = Select(wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//select"))
        select.select_by_visible_text(random_name)
        wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()
        from_where_edit = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        print("random_name =", random_name, ";", "from_where_edit =", from_where_edit)
        assert random_name == from_where_edit

    def select_random(self):
        wd = self.app.wd
        from_where = wd.find_elements(By.XPATH, "//*[@id='id_fromwhere']//select/option")
        names = [e.text for e in from_where]
        random_name = random.choice(names)
        select = Select(wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//select"))
        select.select_by_visible_text(random_name)
        wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()

    def change_filial(self, selected_filial):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(1)
        filial = wd.find_element(By.XPATH, "//*[@title='Филиал']//span[1]").text
        if filial != selected_filial:
            wd.find_element(By.XPATH, "//*[@title='Филиал']").click()
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(selected_filial)
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(1)

    def edit_fromwhere_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "id_fromwhere")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        from_where = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='id_fromwhere'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()
        from_where_edit = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        print("from_where =", from_where, ";", "from_where_edit =", from_where_edit)
        assert from_where == from_where_edit

    def edit_sms_status_no(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "nosms")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='nosms'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='nosms']/div[1]/label").text
        wd.find_element(By.XPATH, "//*[@id='nosms']//input[@value=1]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='nosms']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def edit_sms_status_yes(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "nosms")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='nosms'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='nosms']/div[2]/label").text
        wd.find_element(By.XPATH, "//*[@id='nosms']//input[@value=0]").click()
        time.sleep(2)
        if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='nosms']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        assert selected_value == new_value

    def edit_points_field(self, points):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "points")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='points'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='points']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='points']//input").send_keys(points)
        wd.find_element(By.XPATH, "//*[@id='points']//span[@class='input-group-btn']").click()
        points_edit = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        print("points =", points, ";", "points_edit =", points_edit)
        assert points == points_edit

    def edit_points_field_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "points")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        points = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='points'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='points']//span[@class='input-group-btn']").click()
        points_edit = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        print("points =", points, ";", "points_edit =", points_edit)
        assert points == points_edit

    def edit_total_summ(self, summ):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "total_summ")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        wd.find_element(By.XPATH, "//*[@data-key='total_summ'][@type='button']").click()
        wd.find_element(By.XPATH, "//*[@id='total_summ']//input").clear()
        wd.find_element(By.XPATH, "//*[@id='total_summ']//input").send_keys(summ)
        wd.find_element(By.XPATH, "//*[@id='total_summ']//span[@class='input-group-btn']").click()
        summ_edit = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        print("summ =", summ, ";", "summ_edit =", summ_edit)
        assert summ == summ_edit

    def edit_total_summ_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "total_summ")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        summ = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        wd.find_element(By.XPATH, "//*[@data-key='total_summ'][@type='button']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@id='total_summ']//span[@class='input-group-btn']").click()
        summ_edit = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        print("summ =", summ, ";", "summ_edit =", summ_edit)
        assert summ == summ_edit
