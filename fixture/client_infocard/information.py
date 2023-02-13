import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import allure


class InformationHelper:

    def __init__(self, app):
        self.app = app

    @allure.step("Поиск пациента")
    def search_patient(self, search_name):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.HOME)
        time.sleep(2)
        with allure.step("Нажать 'Поиск по пациентам'"):
            wd.find_element(By.XPATH, "//*[@class='headbarUserSearch headbarRightElement']").click()
        with allure.step(f"Ввести фамилию {search_name} в поле ввода"):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(search_name)
        time.sleep(2)
        with allure.step("Нажать 'ENTER'"):
            wd.find_element(By.XPATH, "//*[@id='select2-drop']//input").send_keys(Keys.ENTER)
        time.sleep(2)

    @allure.step("Открыть дополнительную информацию")
    def open_additional_info(self):
        wd = self.app.wd
        with allure.step("Закрыть основную информацию"):
            wd.find_element(By.LINK_TEXT, "Основная информация").click()
        time.sleep(1)
        with allure.step("Открыть дополнительную информацию"):
            wd.find_element(By.LINK_TEXT, "Дополнительная информация").click()

    @allure.step("Редактировать комментарий")
    def edit_comments(self, comments):
        wd = self.app.wd
        self.open_additional_info()
        with allure.step("Нажать кнопку 'Редактировать комментарий'"):
            wd.find_element(By.XPATH, "//*[@data-key='comments'][@type='button']").click()
        with allure.step(f"Ввести текст {comments}"):
            wd.find_element(By.XPATH, "//*[@id='comments']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='comments']//input").send_keys(comments)
        with allure.step("Сохранить комментарий"):
            wd.find_element(By.XPATH, "//*[@id='comments']//span[@class='input-group-btn']").click()
        if wd.find_element(By.XPATH, "//*[@class='sweet-content']"):
            error = wd.find_element(By.XPATH, "//*[@class='sweet-content']")
            print("Ошибка:", error.text)
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        comments_edit = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        print("comments =", comments, ";", "comments_edit =", comments_edit)
        with allure.step(f"Проверка. Вводимые данные: {comments}. Сохраненные данные: {comments_edit}"):
            assert comments == comments_edit

    @allure.step("Сохранить комментарий без изменений")
    def edit_comments_none(self):
        wd = self.app.wd
        self.open_additional_info()
        time.sleep(1)
        comments = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        with allure.step("Нажать кнопку 'Редактировать комментарий'"):
            wd.find_element(By.XPATH, "//*[@data-key='comments'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='comments']//span[@class='input-group-btn']").click()
        comments_edit = wd.find_element(By.XPATH, "//*[@id='comments']/p").text
        print("comments =", comments, ";", "comments_edit =", comments_edit)
        with allure.step(f"Проверка. Значение поля до редактирования:"
                         f" {comments}. Значение поля после сохранения: {comments_edit}"):
            assert comments == comments_edit

    @allure.step("Редактировать дату первой записи")
    def edit_first_record_date(self, date):
        wd = self.app.wd
        self.open_additional_info()
        with allure.step("Нажать кнопку 'Редактировать дату первой записи'"):
            wd.find_element(By.XPATH, "//*[@data-key='first_record_date'][@type='button']").click()
        with allure.step(f"Ввести дату: {date}"):
            wd.find_element(By.XPATH, "//*[@id='first_record_date']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='first_record_date']//input").send_keys(date)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='first_record_date']//span[@class='input-group-btn']").click()
        self.error_trapping()
        date_edit = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        print("date =", date, ";", "date_edit =", date_edit)
        with allure.step(f"Проверка. Вводимое значение: {date}. Сохраненное значение: {date_edit}"):
            assert date == date_edit

    @allure.step("Проверка на ошибки")
    def error_trapping(self):
        wd = self.app.wd
        if wd.find_element(By.XPATH, "//*[@class='sweet-content']"):
            error = wd.find_element(By.XPATH, "//*[@class='sweet-content']")
            print("Ошибка:", error.text)
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
            assert error == 0

    @allure.step("Сохранить дату первой записи без ввода данных")
    def edit_first_record_date_none(self):
        wd = self.app.wd
        self.open_additional_info()
        time.sleep(1)
        date = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        with allure.step("Нажать кнопку 'Редактировать дату первой записи'"):
            wd.find_element(By.XPATH, "//*[@data-key='first_record_date'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='first_record_date']//span[@class='input-group-btn']").click()
        date_edit = wd.find_element(By.XPATH, "//*[@id='first_record_date']/p").text
        print("date =", date, ";", "date_edit =", date_edit)
        with allure.step(f"Проверка. Значение поля до редактирования: {date}. После сохранения: {date_edit}"):
            assert date == date_edit

    @allure.step("Ввести и сохранить 1c id")
    def edit_id1c(self, id1c):
        wd = self.app.wd
        self.open_additional_info()
        with allure.step("Нажать кнопку редактировать '1c id'"):
            wd.find_element(By.XPATH, "//*[@data-key='id1c'][@type='button']").click()
        with allure.step(f"Ввести значение: {id1c}"):
            wd.find_element(By.XPATH, "//*[@id='id1c']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='id1c']//input").send_keys(id1c)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='id1c']//span[@class='input-group-btn']").click()
        self.error_trapping()
        id1c_edit = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        print("id1c =", id1c, ";", "id1c_edit =", id1c_edit)
        with allure.step(f"Проверка. Вводимое значение: {id1c}. Сохранное значение: {id1c_edit}"):
            assert id1c == id1c_edit

    @allure.step("Сохранить 1с id без изменения")
    def edit_id1c_none(self):
        wd = self.app.wd
        self.open_additional_info()
        time.sleep(1)
        id1c = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        with allure.step("Нажать кнопку редактировать '1c id'"):
            wd.find_element(By.XPATH, "//*[@data-key='id1c'][@type='button']").click()
        with allure.step("Нажать кнопку 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='id1c']//span[@class='input-group-btn']").click()
        id1c_edit = wd.find_element(By.XPATH, "//*[@id='id1c']/p").text
        print("id1c =", id1c, ";", "id1c_edit =", id1c_edit)
        with allure.step(f"Проверка. Значение поля до редактирования: {id1c}. После сохранения: {id1c_edit}"):
            assert id1c == id1c_edit

    @allure.step("Редактировать поле 'Откуда узнали'")
    def edit_fromwhere(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "id_fromwhere")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать"):
            wd.find_element(By.XPATH, "//*[@data-key='id_fromwhere'][@type='button']").click()
        from_where = wd.find_elements(By.XPATH, "//*[@id='id_fromwhere']//select/option")
        names = [e.text for e in from_where]
        random_name = random.choice(names)
        with allure.step(f"В выпадающем списке выбрать значение: {random_name}"):
            select = Select(wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//select"))
            select.select_by_visible_text(random_name)
        with allure.step("Нажать кнопку 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()
        self.error_trapping()
        from_where_edit = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        print("random_name =", random_name, ";", "from_where_edit =", from_where_edit)
        with allure.step(f"Проверка. Выбранное значение в селекте: {random_name}."
                         f" Сохраненное в поле значение: {from_where_edit}"):
            assert random_name == from_where_edit

    def select_random_fromwhere(self):
        wd = self.app.wd
        from_where = wd.find_elements(By.XPATH, "//*[@id='id_fromwhere']//select/option")
        names = [e.text for e in from_where]
        random_name = random.choice(names)
        select = Select(wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//select"))
        select.select_by_visible_text(random_name)
        wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()
        self.error_trapping()
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

    @allure.step("Сохранить 'Откуда узнали' без изменений")
    def edit_fromwhere_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "id_fromwhere")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        from_where = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        with allure.step("Нажать кнопку редактировать поле 'Откуда узнали'"):
            wd.find_element(By.XPATH, "//*[@data-key='id_fromwhere'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='id_fromwhere']//span[@class='input-group-btn']").click()
        self.error_trapping()
        from_where_edit = wd.find_element(By.XPATH, "//*[@id='id_fromwhere']/p").text
        print("from_where =", from_where, ";", "from_where_edit =", from_where_edit)
        with allure.step(f"Проверка. Значение поля до редактирования: {from_where}."
                         f" Значение после сохранения: {from_where_edit}"):
            assert from_where == from_where_edit

    @allure.step("Редактировать поле 'Не отправлять SMS'")
    def edit_sms_status_no(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "nosms")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать статус отправки SMS"):
            wd.find_element(By.XPATH, "//*[@data-key='nosms'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='nosms']/div[1]/label").text
        with allure.step("Выбрать значение 'Не отправлять SMS'"):
            wd.find_element(By.XPATH, "//*[@id='nosms']//input[@value=1]").click()
        time.sleep(2)
        self.error_trapping()
        # if len(wd.find_elements(By.XPATH, "//*[@class='sweet-confirm styled']")) > 0:
        #     wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        new_value = wd.find_element(By.XPATH, "//*[@id='nosms']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        with allure.step(f"Проверка. Выбранное значение: {selected_value}. Сохраненное значение: {new_value}"):
            assert selected_value == new_value

    @allure.step("Редактировать поле 'Отправлять SMS'")
    def edit_sms_status_yes(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "nosms")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать статус отправки SMS"):
            wd.find_element(By.XPATH, "//*[@data-key='nosms'][@type='button']").click()
        selected_value = wd.find_element(By.XPATH, "//*[@id='nosms']/div[2]/label").text
        with allure.step("Выбрать значение 'Отправлять SMS'"):
            wd.find_element(By.XPATH, "//*[@id='nosms']//input[@value=0]").click()
        time.sleep(2)
        self.error_trapping()
        new_value = wd.find_element(By.XPATH, "//*[@id='nosms']/p").text
        print("enter_data =", selected_value, ";", "save_data =", new_value)
        with allure.step(f"Проверка. Выбранное значение: {selected_value}. Сохраненное значение: {new_value}"):
            assert selected_value == new_value

    @allure.step("Редактировать поле 'Очки'")
    def edit_field_points(self, points):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "points")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать поле 'Очки'"):
            wd.find_element(By.XPATH, "//*[@data-key='points'][@type='button']").click()
        with allure.step(f"Ввести значение: {points}"):
            wd.find_element(By.XPATH, "//*[@id='points']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='points']//input").send_keys(points)
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='points']//span[@class='input-group-btn']").click()
        self.error_trapping()
        points_edit = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        print("points =", points, ";", "points_edit =", points_edit)
        with allure.step(f"Проверка. Вводимое значение: {points}. Сохраненное значение: {points_edit}"):
            assert points == points_edit

    @allure.step("Редактировать поле 'Очки'")
    def edit_field_points_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "points")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        points = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        with allure.step("Нажать кнопку редактировать поле 'Очки'"):
            wd.find_element(By.XPATH, "//*[@data-key='points'][@type='button']").click()
        with allure.step("Нажать 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='points']//span[@class='input-group-btn']").click()
        points_edit = wd.find_element(By.XPATH, "//*[@id='points']/p").text
        print("points =", points, ";", "points_edit =", points_edit)
        with allure.step(f"Проверка. Вводимое значение: {points}. Сохраненное значение: {points_edit}"):
            assert points == points_edit

    @allure.step("Редактировать сумму за лечение")
    def edit_total_summ(self, summ):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "total_summ")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        with allure.step("Нажать кнопку редактировать сумму за лечение"):
            wd.find_element(By.XPATH, "//*[@data-key='total_summ'][@type='button']").click()
        with allure.step(f"Ввести значение: {summ}"):
            wd.find_element(By.XPATH, "//*[@id='total_summ']//input").clear()
            wd.find_element(By.XPATH, "//*[@id='total_summ']//input").send_keys(summ)
        with allure.step("Нажать кнопку 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='total_summ']//span[@class='input-group-btn']").click()
        self.error_trapping()
        summ_edit = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        print("summ =", summ, ";", "summ_edit =", summ_edit)
        with allure.step(f"Проверка. Вводимое значение: {summ}. Сохраненное значение: {summ_edit}"):
            assert summ == summ_edit

    @allure.step("Редактировать сумму за лечение")
    def edit_total_summ_none(self):
        wd = self.app.wd
        self.open_additional_info()
        element = wd.find_element(By.ID, "total_summ")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        summ = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        with allure.step("Нажать кнопку редактировать сумму за лечение"):
            wd.find_element(By.XPATH, "//*[@data-key='total_summ'][@type='button']").click()
        time.sleep(1)
        with allure.step("Нажать кнопку 'Сохранить'"):
            wd.find_element(By.XPATH, "//*[@id='total_summ']//span[@class='input-group-btn']").click()
        summ_edit = wd.find_element(By.XPATH, "//*[@id='total_summ']/p").text
        print("summ =", summ, ";", "summ_edit =", summ_edit)
        with allure.step(f"Проверка. Вводимое значение: {summ}. Сохраненное значение: {summ_edit}"):
            assert summ == summ_edit
