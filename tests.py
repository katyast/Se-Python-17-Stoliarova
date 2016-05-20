# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import datetime


now_time = datetime.datetime.now()
now_time = str(now_time)
film_name = "unic_title_" + now_time


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        # создание фильма с уникальным именем
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(film_name)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2012")
        driver.find_element_by_id("submit").click()
        # переход на главную страницу
        driver.find_element_by_link_text("Home").click()
        # проверка поиска несуществующего фильма
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(film_name+"нет такого")
        driver.find_element_by_id("q").send_keys(Keys.ENTER)
        self.assertEqual("No movies where found.", driver.find_element_by_css_selector("div.content").text)
        # проверка поиска существующего фильма
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(film_name)
        driver.find_element_by_id("q").send_keys(Keys.ENTER)
        self.assertEqual(film_name, driver.find_element_by_css_selector(".title").text)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

