from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element(By.ID, "form_user_loginhtml_input_0_login").send_keys(username)
        wd.find_element(By.ID, "form_user_loginhtml_password_0_password").send_keys(password)
        wd.find_element(By.ID, "form_user_loginhtml_button_1_button").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class='userHeading']").click()
        wd.find_element(By.XPATH, "//*[@onclick='user.logout();']").click()

