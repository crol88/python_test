import time
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TreatmentPlanHelper:

    def __init__(self, app):
        self.app = app

    def open_treatment_plan(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[@title='Пациент']").click()
        time.sleep(1)
        wd.find_element(By.XPATH, "//a[.='План лечения']").click()
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

    def select_all_teeth(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//button[.='Выбрать все зубы']").click()
        all_teeth = wd.find_elements(By.XPATH, "//div[@class='jaws']//div[@class='tooth active']")
        assert len(all_teeth) == 32
        print("Кол-во выбранных зубов:", len(all_teeth))

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

    def check_drafts(self, service):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service)) > 0:
            print("Есть черновик приема")
        return len(wd.find_elements(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service))

    def select_optimal_tplan(self, variants, area, problem, var_next, doctor):
        wd = self.app.wd
        self.select_all_teeth()
        wd.find_element(By.XPATH, "//button[.='%s']" % area).click()
        act = wd.find_element(By.XPATH, "//button[.='%s']" % problem).get_attribute("class")
        if act != "DentalPanel_problem active":
            wd.find_element(By.XPATH, "//button[.='%s']" % problem).click()
        time.sleep(2)
        element = wd.find_element(By.XPATH, "//div[.='%s']/div" % variants)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        element.click()
        wd.find_element(By.XPATH, "//div[.='%s']/following-sibling::button" % var_next).click()
        sel = Select(wd.find_element(By.XPATH, "//select[@name='doctorID']"))
        sel.select_by_visible_text(doctor)
        service = wd.find_element(By.XPATH, "//table[@class='table']//label").text
        print(service)
        wd.find_element(By.XPATH, "//button[.='Создать приёмы']").click()
        time.sleep(2)
        assert wd.find_element(By.XPATH, "//div[@class='Canban_col Canban_col_drafts']//div[.='%s']" % service) != 0


