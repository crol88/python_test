# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fixture.session import SessionHelper
from fixture.client_infocard.basic_info import BasicInfoHelper
from fixture.client_infocard.contact import ContactHelper
from fixture.client_infocard.passport import PassportHelper
from fixture.client_infocard.parent import ParentHelper
from fixture.client_infocard.address import AddressHelper
from fixture.client_infocard.information import InformationHelper
from fixture.add_newclient.cbase import CbaseHelper
from fixture.cbase_filter.cbase_filter import CbaseFilterHelper
from fixture.client_infocard.infocard_mainpage import InfoCardHelper
from fixture.add_newclient.cbase_config import CbaseConfigHelper


class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.basic_info = BasicInfoHelper(self)
        self.contact = ContactHelper(self)
        self.passport = PassportHelper(self)
        self.parent = ParentHelper(self)
        self.address = AddressHelper(self)
        self.information = InformationHelper(self)
        self.cbase = CbaseHelper(self)
        self.cbase_filter = CbaseFilterHelper(self)
        self.infocard_mainpage = InfoCardHelper(self)
        self.cbase_config = CbaseConfigHelper(self)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        # wd.get("https://stablev10.dm.dental-pro.online/")
        # wd.get("https://betav10.dm.dental-pro.online/")
        # wd.get("https://regress.dm.dental-pro.online/")
        # wd.get("https://betav11.dm.dental-pro.online/")
        wd.get(self.base_url)
        wd.maximize_window()
        # wd.set_window_size(1920, 1080)

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
