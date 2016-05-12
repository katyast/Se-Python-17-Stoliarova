from selenium.webdriver.common.by import By


class PageAuthorizationLocators(object):
    """ Локаторы главной страницы неавторизованного пользователя"""

    find_login_form_username = (By.ID, "username")
    find_login_form_password = (By.NAME, "password")
    find_login_form_button = (By.NAME, "submit")


class PageDashboardLocators(object):
    """ Локаторы главной страницы авторизованного пользователя"""

    find_search = (By.ID, "search")
