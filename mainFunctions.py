import page

import config as cp

base_url = cp.parser.get('url', 'base_url')
username = cp.parser.get('login', 'username')
password = cp.parser.get('login', 'password')


class Authorization(object):
    """ Вход на главную страницу сайта php4dvd."""

    def login(self, login_username=username, login_password=password):
        """ Ввод логина и пароля на странице авторизации.

        По умолчанию заданы логин и пароль из файла конфигов.
        Метод возвращает страница авторизованного пользователя.
        """
        page.AuthorizationPage.send_keys_username(self, login_username)
        page.AuthorizationPage.send_keys_password(self, login_password)
        page.AuthorizationPage.click_go_button(self)
        return self.driver