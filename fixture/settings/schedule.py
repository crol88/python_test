import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ScheduleSetHelper:

    def __init__(self, app):
        self.app = app

    def open_doc_schedule(self, group):
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
        if len(wd.find_elements(By.XPATH, "//div[.='График работы врачей']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='График работы врачей']/parent::a").click()
        doc = wd.find_element(By.XPATH, "//strong[contains(text(),'%s')]" % group.surname).text
        print("Врач добавленный в расписание:", doc)

    def open_doc_schedule_new(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//*[@class='breadcrumb']//li[.='График работы врачей (Новый)']")) == 0:
            if len(wd.find_elements(By.XPATH, "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon "
                                              "active']")) == 0:
                wd.find_element(By.XPATH,
                                "//*[@class='btn btn-link js-sidebarSettingsOpen sidebarSpecialIcon']").click()
        b = wd.find_element(By.XPATH,
                            "//span[.='Расписание']/parent::div[@role='button']").get_attribute("aria-expanded")
        if str(b) == "false":
            wd.find_element(By.XPATH, "//span[.='Расписание']/parent::div[@role='button']").click()
        time.sleep(1)
        if len(wd.find_elements(By.XPATH, "//div[.='График работы врачей']/parent::div[@class='headbarLeft']")) == 0:
            wd.find_element(By.XPATH, "//*[.='График работы врачей']/parent::a").click()
