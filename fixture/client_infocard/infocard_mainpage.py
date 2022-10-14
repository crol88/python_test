import time
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

    def check_filial(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        filial = wd.find_element(By.XPATH, "//*[@class='col-md-3']/div[3]/*[@class='panel-body']").text
        print(filial)
        assert "Филиал" not in filial
