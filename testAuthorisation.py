# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import config as cp
import mainFunctions
from locators import PageAuthorizationLocators
from locators import PageDashboardLocators


base_url = cp.parser.get('url', 'base_url')
username = cp.parser.get('login', 'username')
password = cp.parser.get('login', 'password')


class SuccessAuthorisation(unittest.TestCase):
    """"Проверка успешной авторизации"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.get(base_url)

    def test_success_authorization(self):
        main_page = mainFunctions.Authorization.login(self, username, password)
        find_search = main_page.find_element(*PageDashboardLocators.find_search)
        assert find_search.is_displayed()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
