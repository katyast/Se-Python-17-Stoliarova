from Se-Python-17-Stoliarova.pages.internal_page import InternalPage
from Se-Python-17-Stoliarova.pages.login_page import LoginPage
from Se-Python-17-Stoliarova.pages.user_management_page import UserManagementPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()

    def login(self, user):
        lp = self.login_page
        lp.is_this_page
        lp.username_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def add_user(self, user):
        self.internal_page.user_management_link.click()
        ump = self.user_management_page
        ump.is_this_page
        ump.username_field.send_keys(user.username)
        ump.email_field.send_keys(user.email)
        ump.password_field.send_keys(user.password)
        ump.password1_field.send_keys(user.password)
        #ump.role_select.select_by_visible_text(user.role)
        ump.submit_button.click()