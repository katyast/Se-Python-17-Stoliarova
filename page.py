from locators import PageAuthorizationLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class AuthorizationPage(BasePage):
    """Триггеры страницы неавторизованного пользователя"""
    def send_keys_username(self, login_username):
        """Ввод логина"""
        element = self.driver.find_element(*PageAuthorizationLocators.find_login_form_username)
        element.send_keys(login_username)

    def send_keys_password(self, login_password):
        """Ввод пароля"""
        element = self.driver.find_element(*PageAuthorizationLocators.find_login_form_password)
        element.send_keys(login_password)

    def click_go_button(self):
        """Нажатие кнопки входа"""
        element = self.driver.find_element(*PageAuthorizationLocators.find_login_form_button)
        element.click()