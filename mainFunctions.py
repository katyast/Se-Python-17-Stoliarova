import page

import config as cp

base_url = cp.parser.get('url', 'base_url')
operator_pl_username = cp.parser.get('login', 'username')
operator_pl_password = cp.parser.get('login', 'password')


class Authorization(object):
    """ Вход на главную страницу сайта тестовой площадки."""

    def login(self, login_username, login_password):
        """ Ввод логина и пароля на странице авторизации.

        По умолчанию заданы логин и пароль оператора из файла конфигов.
        Метод возвращает страница авторизованного пользователя.
        """
        page.AuthorizationPage.send_keys_username(self, login_username)  # вынести локаторы и элеиенты отдельно
        page.AuthorizationPage.send_keys_password(self, login_password)
        page.AuthorizationPage.click_go_button(self)
        return self.driver