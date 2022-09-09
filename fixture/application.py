from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.basic import BasicHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.basic = BasicHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://stablev10.ci.dental-pro.online/")
        # wd.get("https://betav10.ci.dental-pro.online/")
        wd.set_window_size(1920, 1080)

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

