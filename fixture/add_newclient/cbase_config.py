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

    def client_branch_activate(self):
        wd = self.app.wd
        active = wd.find_element(By.XPATH, "//*[@class='btn-default btn active']/input").get.attribute("class value")
        not_active = wd.find_element(By.XPATH, "//*[@class='btn-default btn']/input").get.attribute("class value")
        print(active, not_active)


