# -*- coding: utf-8 -*-
from selenium import webdriver
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
from fixture.schedule.schedule import ScheduleHelper
from fixture.settings.employees import EmployeesHelper
from fixture.settings.schedule import ScheduleSetHelper
from fixture.client_infocard.tplan import TreatmentPlanHelper


class Application:

    def __init__(self, base_url):
        # chrome_options = webdriver.ChromeOptions()
        # self.wd = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub',
        #                            desired_capabilities={'browserName': 'chrome',
        #                                                  'version': '110.0'},
        #                            options=chrome_options)
        capabilities = {
            "browserName": "chrome",
            "version": "110.0",
            "platform": "LINUX"
        }
        self.wd = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                   desired_capabilities=capabilities)
        # self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
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
        self.schedule = ScheduleHelper(self)
        self.base_url = base_url
        self.settings = EmployeesHelper(self)
        self.set_schedule = ScheduleSetHelper(self)
        self.tplan = TreatmentPlanHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get(self.base_url)
        wd.maximize_window()
        # wd.set_window_size(1920, 1080)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
