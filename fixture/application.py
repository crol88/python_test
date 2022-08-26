from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://betav10.ci.dental-pro.online/")
        wd.set_window_size(1920, 1080)

    def destroy(self):
        wd = self.wd
        wd.quit()
