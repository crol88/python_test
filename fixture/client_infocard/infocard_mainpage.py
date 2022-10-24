import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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

    def delete_mark(self, mark, status):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        wd.find_element(By.XPATH,
                        "//*[@class='mb-10']//text()[contains(.,'%s')]/preceding-sibling::span//*["
                        "@type='button']" % mark).click()
        wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        marks = wd.find_elements(By.XPATH, "//*[@class='list-group-item_flex']")
        names = [e.text for e in marks]
        assert status not in names
        print(names)

    def mark(self, mark, check_mark):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,600)")
        if len(wd.find_elements(By.XPATH,
                                "//*[@class='mb-10']//text()[contains(.,'%s')]/preceding-sibling::span//*["
                                "@type='button']" % check_mark)) == 0:
            time.sleep(1)
            wd.find_element(By.XPATH, "//*[@class='btn btn-sm btn-default dropdown-toggle btn-block']").click()
            wd.find_element(By.XPATH, "//*[@class='dropdown-menu']/li/a[text()='%s']" % mark).click()
            wd.find_element(By.XPATH, "//*[@class='sweet-confirm styled']").click()
        return len(wd.find_elements(By.XPATH,
                                    "//*[@class='mb-10']//text()[contains(.,'%s')]/preceding-sibling::span//*["
                                    "@type='button']" % check_mark))

    def upload_photo(self):
        wd = self.app.wd
        old_photo = wd.find_element(By.XPATH, "//*[@class='thumbnail photo_sub_wrapper']/img").get_attribute("src")
        wd.find_element(By.XPATH, "//*[@class='btn btn-info js-tooltip photo_sub_upload']").click()
        upload = wd.find_element(By.XPATH, "//input[@type='file']")
        upload.send_keys("C:/Devel/python_test/files/patient_photo.JPG")
        success = wd.find_element(By.XPATH, "//*[@class='text-success form_cbase_photo_upload_0__toShowAfterSuccess']")
        assert success is not None
        wd.find_element(By.XPATH, "//*[@class='btn-success btn']").click()
        new_photo = wd.find_element(By.XPATH, "//*[@class='thumbnail photo_sub_wrapper']/img").get_attribute("src")
        assert old_photo != new_photo

    def choice_coordinator(self, filial, manager):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0,1000)")
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[@class='btn-group btn-block']/a").click()
        select_filial = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_addManager_select_0_']"))
        select_filial.select_by_visible_text(filial)
        select_manager = Select(wd.find_element(By.XPATH, "//*[@id='form_cbase_addManager_select_1_']"))
        select_manager.select_by_visible_text(manager)
        wd.find_element(By.XPATH, "//*[@class='btn-success btn']").click()
        check_m = wd.find_element(By.XPATH, "//*[ @class ='list-group']")
        print(check_m.text)
        assert manager == check_m.text