import time
import random
import allure
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TreatmentPlanHelper:

    def __init__(self, app):
        self.app = app

    @allure.step("Открыть план лечения")
    def open_treatment_plan(self):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'Пациент'"):
            wd.find_element(By.XPATH, "//button[@title='Пациент']").click()
        time.sleep(1)
        with allure.step("В выпадающем списке выбрать план лечения"):
            wd.find_element(By.XPATH, "//a[.='План лечения']").click()
        with allure.step("Проверить, что открылась зубная формула"):
            toothsmap = wd.find_element(By.XPATH, "//div[.='Зубная формула']")
            assert toothsmap != 0

    def add_plan(self):
        wd = self.app.wd
        sys_time = str(datetime.now().time().strftime('%H:%M'))
        plan_name = f"План {sys_time}"
        print(plan_name)
        wd.find_element(By.XPATH, "//button[@class='Canban_variants-add']").click()
        wd.find_element(By.XPATH, "//input[@name='name']").clear()
        wd.find_element(By.XPATH, "//input[@name='name']").send_keys(plan_name)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        new_plan = wd.find_element(By.XPATH, "//button[.='%s']" % plan_name)
        assert new_plan != 0

    @allure.step("Выбрать все зубы")
    def select_all_teeth(self):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'Выбрать все зубы'"):
            wd.find_element(By.XPATH, "//button[.='Выбрать все зубы']").click()
        all_teeth = wd.find_elements(By.XPATH, "//div[@class='jaws']//div[@class='tooth active']")
        assert len(all_teeth) == 32
        # print("Кол-во выбранных зубов:", len(all_teeth))

    def open_treatment_chains(self):
        wd = self.app.wd
        # Цепочки лечения
        if len(wd.find_elements(By.XPATH, "//div[.='Цепочки лечений']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Мед. блок']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Мед. блок']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Цепочки лечений']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Цепочки лечений']/parent::a").click()

    def open_medblock_problem(self):
        wd = self.app.wd
        # Проблемы
        if len(wd.find_elements(By.XPATH, "//div[.='Проблемы']/parent::div[@class='headbarLeft']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH, "//span[.='Мед. блок']/parent::div").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//*[.='Мед. блок']/parent::div").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='Проблемы']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='Проблемы']/parent::a").click()

    def search_chains(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@title='Плагин:medblock Таблица:medblock_chains']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//input[@name='filter[Filter][name]']").send_keys("Снятие зубных отложений/ Профессиональная гигиена")
        wd.find_element(By.XPATH, "//input[@name='filter[Filter][name]']").send_keys(Keys.ENTER)
        # wd.find_element(By.XPATH, "//button[.='Отфильтровать']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//a[contains(text(),'Профессиональная гигиена')]").click()
        chain = wd.find_elements(By.XPATH, "//div[.='Настройка этапов']/parent::div[@class='headbarLeft']")
        assert chain != 0

    def search_problem(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='headingOne']").click()
        wd.find_element(By.XPATH, "//input[@name='filter[Filter][name]']").send_keys("Профессиональная гигиена")
        wd.find_element(By.XPATH, "//input[@name='filter[Filter][name]']").send_keys(Keys.ENTER)
        # wd.find_element(By.XPATH, "//button[.='Отфильтровать']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//a[contains(text(),'Профессиональная гигиена')]").click()
        chain = wd.find_elements(By.XPATH, "//div[.='Настройка этапов']/parent::div[@class='headbarLeft']")
        assert chain != 0

    def check_chain_table(self):
        wd = self.app.wd
        # all_chain = wd.find_elements(By.XPATH, "//div[contains(@class,'panel-success')]//span")
        # names = [e.text for e in all_chain]
        # a = wd.find_elements(By.XPATH, "//div[contains(@class,'panel-success')]//span")
        a = wd.find_elements(By.XPATH, "//div[@class='media-body']/a")
        names = [e.get_attribute('textContent') for e in a]
        # print(names)
        return names

    def select_problem(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[.='Шейка зуба']").click()
        act = wd.find_element(By.XPATH, "//button[.='Зубные отложения']").get_attribute("class")
        if act != "DentalPanel_problem active":
            wd.find_element(By.XPATH, "//button[.='Зубные отложения']").click()
        time.sleep(2)
        element = wd.find_element(By.XPATH, "//div[.='Снятие зубных отложений/ Профессиональная гигиена']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        # wd.find_element(By.XPATH, "//div[.='Снятие зубных отложений/ Профессиональная гигиена']").click()
        element.click()
        var = wd.find_elements(By.XPATH, "//div[.='Снятие зубных отложений/ Профессиональная "
                                         "гигиена']/following-sibling::div//div[@class='Canban_variant_heading']")
        names = [e.get_attribute('textContent') for e in var]
        # print(names)
        return names

    def treatment_options(self):
        wd = self.app.wd
        # element = wd.find_element(By.XPATH, "//div[.='Профессиональная гигиена Norma']/button")
        # wd.execute_script("arguments[0].scrollIntoView();", element)
        wd.find_element(By.XPATH, "//div[.='Профессиональная гигиена Norma']/button").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Создать приёмы']").click()
        p = wd.find_elements(By.XPATH, "//div[@class='Canban_element_heading']")
        print("Кол-во созданных приемов:", len(p))
        assert len(p) == 1

    def plan_approved(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[.='Утвердить приём']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Да']").click()
        approved = wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//div[@class='Canban_element_heading']")
        draft = wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[@class='Canban_element_heading']")
        assert len(approved) == 1
        assert len(draft) == 0

    def create_fact(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//button[.='Toggle Dropdown']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Toggle Dropdown']").click()
        wd.find_element(By.XPATH, "//a[.='Создать факт']").click()
        stage_list = wd.find_elements(By.XPATH, "//select[@name='caredoc_stage_id']/option")
        # names = [e.get_attribute('textContent') for e in stage]
        names = [e.text for e in stage_list]
        del names[0]
        random_stage = random.choice(names)
        print(names)
        print(random_stage)
        select_stage = Select(wd.find_element(By.XPATH, "//select[@name='caredoc_stage_id']"))
        select_stage.select_by_visible_text(random_stage)
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[@class='col-xs-6 js-codes']")) > 0:
            all_sel = wd.find_elements(By.XPATH, "//select[@name='caredoc_code_id']/option")
            code_sel = [e.text for e in all_sel]
            del code_sel[0]
            random_code = random.choice(code_sel)
            sel = Select(wd.find_element(By.XPATH, "//select[@name='caredoc_code_id']"))
            sel.select_by_visible_text(random_code)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        fact = wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_fact']//div[@class='Canban_element_heading']")
        approved = wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//div[@class='Canban_element_heading']")
        draft = wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[@class='Canban_element_heading']")
        assert len(fact) == 1
        assert len(approved) == 0
        assert len(draft) == 0

    def check_problem_after_fact(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//button[.='Выбрать все зубы']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Выбрать все зубы']").click()
        wd.find_element(By.XPATH, "//button[.='Шейка зуба']").click()
        act = wd.find_element(By.XPATH, "//button[.='Зубные отложения']").get_attribute("class")
        assert act == "DentalPanel_problem"

    def open_fin_plane(self):
        self.open_treatment_plan()
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//div[@class='Canban_switch-view']//*[@class='glyphicon glyphicon-list-alt']/parent::button")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        a = element.get_attribute("class")
        print(a)
        assert a == "btn btn-default active"

    def add_fin_plane_step(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//a[@href='/medblock/finplan/formAdd?variantID=895']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        element.click()

    @allure.step("Проверить приемы в черновике")
    def check_drafts(self, service):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service)) > 0:
            with allure.step("В черновике присутствует прием"):
                print("В черновике присутствует прием")
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service)) == 0:
            with allure.step("В черновике отсутствуют приемы"):
                print("В черновике отсутствуют приемы")
        return len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service))

    @allure.step("Проверить утвержденные приемы")
    def check_approved(self, service):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//div[.='%s']" % service)) > 0:
            with allure.step("Присутствует утвержденный прием"):
                print("Есть утвержденный прием")
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']"
                                          "//div[.='%s']" % service)) == 0:
            with allure.step("Утвержденные приемы отсутствуют"):
                print("Утвержденные приемы отсутствуют")
        return len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//div[.='%s']" % service))

    def check_planned(self, service):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_planned']//div[.='%s']" % service)) > 0:
            with allure.step("Присутствует утвержденный прием"):
                print("Есть утвержденный прием")
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_planned']"
                                          "//div[.='%s']" % service)) == 0:
            with allure.step("Утвержденные приемы отсутствуют"):
                print("Запланированные приемы отсутствуют")
        return len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_planned']//div[.='%s']" % service))

    @allure.step("Сформировать план лечения из вариантов предложенных системой")
    def select_optimal_tplan(self, variants, area, problem, var_next, doctor):
        wd = self.app.wd
        self.select_all_teeth()
        with allure.step(f"Указать область зуба: {area}"):
            wd.find_element(By.XPATH, "//button[.='%s']" % area).click()
        with allure.step(f"Указать проблему: {problem}"):
            act = wd.find_element(By.XPATH, "//button[.='%s']" % problem).get_attribute("class")
            if act != "DentalPanel_problem active":
                wd.find_element(By.XPATH, "//button[.='%s']" % problem).click()
        time.sleep(2)
        with allure.step(f"Выбрать варианты лечения: {variants}"):
            element = wd.find_element(By.XPATH, "//div[.='%s']/div" % variants)
            wd.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            element.click()
        with allure.step(f"Перенести выбранный прием в черновик: {var_next}"):
            wd.find_element(By.XPATH, "//div[.='%s']/following-sibling::button" % var_next).click()
        with allure.step(f"Выбрать врача, который будет выполнять приемы: {doctor}"):
            sel = Select(wd.find_element(By.XPATH, "//select[@name='doctorID']"))
            sel.select_by_visible_text(doctor)
        service = wd.find_element(By.XPATH, "//table[@class='table']//label").text
        print(service)
        with allure.step("Нажать 'Создать прием'"):
            wd.find_element(By.XPATH, "//button[.='Создать приёмы']").click()
        time.sleep(2)
        with allure.step(f"Проверка. В черновик добавлен прием с выбранным вариантом лечения: {service}"):
            assert wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service) != 0

    @allure.step("Утвердить прием")
    def canban_approved(self, service):
        wd = self.app.wd
        with allure.step(f"Прием в черновике: {service}"):
            draft = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service)
            wd.execute_script("arguments[0].scrollIntoView();", draft)
        time.sleep(5)
        with allure.step(f"Нажать кнопку 'Утвердить прием' {service}"):
            button = wd.find_element(By.XPATH, "//button[.='Утвердить приём']")
            wd.execute_script("arguments[0].scrollIntoView();", button)
            time.sleep(2)
            wd.find_element(By.XPATH, "//button[.='Утвердить приём']").click()
        time.sleep(1)
        with allure.step("Подтвердить действие"):
            wd.find_element(By.XPATH, "//button[@class='sweet-confirm styled']").click()
        with allure.step(f"Проверка. Прием: {service} перенесен из колонки 'Черновик' в колонку 'Утвержденные'"):
            approved = wd.find_element(By.XPATH,
                                       "//div[@class='Canban_col Canban_col_approved']//div[.='%s']" % service)
            assert approved != 0
            try:
                draft
            except NoSuchElementException:
                return False
            print("Запись из черновика перенесена в утвержденные")
            return True

    @allure.step("Согласовать план лечения")
    def approve_tplan(self):
        wd = self.app.wd
        with allure.step("Нажать кнопку 'Согласовать'"):
            approve = wd.find_element(By.XPATH, "//button[.='Согласовать']")
            wd.execute_script("arguments[0].scrollIntoView();", approve)
            time.sleep(4)
            approve.click()
        time.sleep(1)
        with allure.step("Подтвердить действие"):
            wd.find_element(By.XPATH, "//button[@class='sweet-confirm styled']").click()
        time.sleep(1)
        with allure.step("Проверка. План лечения получил соответствующую отметку 'Согласованно'"):
            assert wd.find_element(By.XPATH, "//i[@class='icon glyphicon glyphicon-ok']") != 0
            assert wd.find_element(By.XPATH, "//div[@class='Canban_agreed text-success']") != 0

    @allure.step("Отменить согласование")
    def cancel_approval(self):
        wd = self.app.wd
        try:
            wd.find_element(By.XPATH, "//div[@class='Canban_agreed text-success']")
        except NoSuchElementException:
            self.approve_tplan()
        with allure.step("Нажать кнопку 'Отменить согласование'"):
            cancel = wd.find_element(By.XPATH, "//button[.='Отменить согласование']")
            wd.execute_script("arguments[0].scrollIntoView();", cancel)
            time.sleep(4)
            cancel.click()
        time.sleep(1)
        with allure.step("Подтвердить действие"):
            wd.find_element(By.XPATH, "//button[@class='sweet-confirm styled']").click()
        time.sleep(2)
        with allure.step("Проверка. План лечения лишился соответствующей отметки 'Согласованно'"):
            assert len(wd.find_elements(By.XPATH, "//div[@class='Canban_agreed text-success']")) == 0

    @allure.step("Удалить прием из черновика")
    def delete_canban_draft(self):
        wd = self.app.wd
        num = len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']"
                                             "//div[@class='Canban_element_heading']"))
        with allure.step("Нажать кнопку 'удалить' на приеме в черновике"):
            delete = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//button[4]")
            time.sleep(1)
            wd.execute_script("arguments[0].scrollIntoView();", delete)
            time.sleep(6)
            wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//button[4]").click()
        time.sleep(1)
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//button[@class='sweet-confirm styled']").click()
        time.sleep(1)
        num_d = len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']"
                                               "//div[@class='Canban_element_heading']"))
        with allure.step(f"Проверка. Кол-во приемов в черновике: {num}."
                         f" Кол-во приемов в черновике после удаления: {num - 1}"):
            assert num - 1 == num_d

    @allure.step("Удалить утвержденный прием")
    def delete_canban_approve(self):
        wd = self.app.wd
        num = len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']"
                                             "//div[@class='Canban_element_heading']"))
        with allure.step("Нажать кнопку 'удалить' на утвержденном приеме"):
            delete = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//button[4]")
            time.sleep(1)
            wd.execute_script("arguments[0].scrollIntoView();", delete)
            time.sleep(6)
            wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//button[4]").click()
        time.sleep(1)
        with allure.step("Подтвердить удаление"):
            wd.find_element(By.XPATH, "//button[@class='sweet-confirm styled']").click()
        time.sleep(1)
        num_d = len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_approved']"
                                               "//div[@class='Canban_element_heading']"))
        with allure.step(f"Проверка. Кол-во утвержденных приемов: {num}."
                         f" Кол-во утвержденных приемов после удаления: {num - 1}"):
            print(num, "=", num_d)
            assert num - 1 == num_d

    def edit_approved_tplan(self, group):
        wd = self.app.wd
        edit = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//button[3]")
        time.sleep(1)
        wd.execute_script("arguments[0].scrollIntoView();", edit)
        time.sleep(4)
        wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_approved']//button[3]").click()
        # Выбор врача
        sel = Select(wd.find_element(By.XPATH, "//select[@name='id_doctor']"))
        doc = str(f"{group.surname} {group.name} {group.secondname}")
        time.sleep(1)
        sel.select_by_visible_text(doc)
        time.sleep(1)
        wd.find_element(By.XPATH, "//textarea[@name='comment']").send_keys("Причина смены врача")
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        doc_edit = str(f"{group.surname} {group.name[0]}.{group.secondname[0]}.")
        # print(doc_edit)
        time.sleep(4)
        canban_doc = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_approved']"
                                               "//div[@class='Canban_element_doctor']").text
        # print("text", canban_doc)
        assert doc_edit == canban_doc

    def reg_approved_tplan(self):
        wd = self.app.wd
        reg = wd.find_element(By.XPATH, "//button[.='Записать']")
        time.sleep(1)
        wd.execute_script("arguments[0].scrollIntoView();", reg)
        time.sleep(4)
        wd.find_element(By.XPATH, "//button[.='Записать']").click()
        wd.find_element(By.XPATH, "//button[.='Развернуть']").click()
        sel = Select(wd.find_element(By.XPATH, "//div[4]/select[@class='form-control']"))
        sel.select_by_visible_text("20:00-21:00")
        time.sleep(1)
        wd.find_element(By.XPATH, "//button[.='Сохранить']").click()
        time.sleep(4)

    def create_fact_tplan(self):
        wd = self.app.wd
        fact = wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_planned']//button[.='Создать факт']")
        time.sleep(2)
        wd.execute_script("arguments[0].scrollIntoView();", fact)
        time.sleep(2)
        wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_planned']//button[.='Создать факт']").click()
        sel = Select(wd.find_element(By.XPATH, "//select[@name='caredoc_stage_id']"))
        sel.select_by_visible_text("З - Лечение закончено")
        time.sleep(2)
        code_list = wd.find_elements(By.XPATH, "//select[@name='caredoc_code_id']/option")
        code_id = [e.text for e in code_list]
        time.sleep(1)
        code = Select(wd.find_element(By.XPATH, "//select[@name='caredoc_code_id']"))
        code.select_by_visible_text(code_id[1])
