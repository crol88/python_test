import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CbaseConfigHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase_config(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        wd.find_element(By.XPATH, "//*[.='Настройка системы']/ancestor:: div[1]").click()
        wd.find_element(By.XPATH, "//*[@href='/upgrade/config.html']").click()
        select = Select(wd.find_element(By.XPATH, "//*[@id='js-upgrade-plugin-select']"))
        select.select_by_visible_text("cbase: База пациентов")

    def client_branch_status(self, status):
        # status = 'Отключено' or 'Включено'
        wd = self.app.wd
        plugin_off = wd.find_element(By.XPATH,
                                     "//*[@name='settings[cbase.client.branches.branchAll]'][@value='0']/parent::label")
        plugin_on = wd.find_element(By.XPATH,
                                    "//*[@name='settings[cbase.client.branches.branchAll]'][@value='1']/parent::label")
        if status == "Отключено":
            plugin_off.click()
        if status == "Включено":
            plugin_on.click()
        active = wd.find_element(By.CSS_SELECTOR,
                                 "#form_upgrade_confightml_switcher_1__parent > label.btn-default.btn.active")
        print("Прикреплять пациента ко всем филиалам автоматически:", active.text)
        assert active.text == status
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-success btn']").click()

    def search_criteria_set(self, status):
        # status can be 'Отключено' or 'Включено'
        wd = self.app.wd
        set_off = wd.find_element(By.XPATH,
                                  "//*[@name='settings[cbase.index.showSearchedOnly]'][@value='0']/parent::label")
        set_on = wd.find_element(By.XPATH,
                                 "//*[@name='settings[cbase.index.showSearchedOnly]'][@value='1']/parent::label")
        if status == "Отключено":
            set_off.click()
        if status == "Включено":
            set_on.click()
        active = wd.find_element(By.CSS_SELECTOR,
                                 "#form_upgrade_confightml_switcher_2__parent > label.btn-default.btn.active")
        print("Отображать список пациентов только если заданы критерии поиска:", active.text)
        assert active.text == status
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-success btn']").click()
        time.sleep(2)
