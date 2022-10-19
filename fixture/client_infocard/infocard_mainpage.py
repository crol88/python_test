import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class InfoCardHelper:

    def __init__(self, app):
        self.app = app

    def open_cbase_vip_no_manager(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
        wd.find_element(By.XPATH, "//*[text()='VIP-пациенты без координатора']").click()

    def check_cbase_vip(self, vip_client):
        wd = self.app.wd
        element = wd.find_element(By.LINK_TEXT, vip_client)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        vip = wd.find_element(By.LINK_TEXT, vip_client).text
        print("vip =", vip, ";", "vip_client =", vip_client)
        assert vip == vip_client

    def check_cbase_vip_list(self, vip_client):
        wd = self.app.wd
        element = wd.find_element(By.LINK_TEXT, vip_client)
        wd.execute_script("arguments[0].scrollIntoView();", element)
        vip = wd.find_element(By.LINK_TEXT, vip_client).text
        print("Пациенту добавлен статус VIP:", vip, ";", "Список VIP пациентов:", vip_client)
        assert vip == vip_client

    def open_cbase_vip_list(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@alt='Пациенты']/ancestor::div[@class='menuLinkLine']").click()
        wd.find_element(By.XPATH, "//*[text()='Список VIP-пациентов']").click()

    def check_without_filial(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        filial = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']").text
        print(filial)
        assert "Филиал" not in filial

    def check_filial(self, enter_filial):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        filial = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']").text
        print(filial)
        assert enter_filial in filial

    def add_note(self, enter_text):
        wd = self.app.wd
        # wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
        wd.execute_script("window.scrollTo(0,200)")
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, ".js-edit-note").click()
        element = wd.find_element(By.CSS_SELECTOR, ".js-edit-note")
        # element = wd.find_element(By.XPATH, "//*[@class='form-control js-tooltip js-edit-note']")
        ActionChains(wd).double_click(element).perform()
        element.clear()
        time.sleep(1)
        element.send_keys(enter_text)
        wd.find_element(By.XPATH, "//*[@id='postcode']").click()
        wd.refresh()
        # wd.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
        wd.execute_script("window.scrollTo(0,200)")
        note_after = wd.find_element(By.XPATH, "//*[@class='form-control js-tooltip js-edit-note']").text
        print("Ввод текста:", enter_text, ";", "Сохраненный текст:", note_after)
        assert note_after == enter_text
