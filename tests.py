# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import config as cp
import mainFunctions
import datetime

base_url = cp.parser.get('url', 'base_url')
username = cp.parser.get('login', 'username')
password = cp.parser.get('login', 'password')
now_time = datetime.datetime.now()
now_time = str(now_time)
film_name = "unic_title_" + now_time

class CreateAndDeleteFilms(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_new_film(self):
        """ Проверка корректного создания фильма.
        (на странице присутствует уникальное имя фильма)"""
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(film_name)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2012")
        driver.find_element_by_id("submit").click()
        body_text = driver.find_element_by_css_selector(".maininfo_full > h2:nth-child(1)").text
        self.assertTrue(film_name, body_text)

    def test_field_form_created_new_film_is_required(self):
        """ Проверка обязательности полей на форме создания фильма.
        (сообщения об ошибках при незаполненных полях)"""
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("h1").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("002")
        driver.find_element_by_id("submit").click()
        self.assertEqual("This field is required", driver.find_element_by_css_selector("label.error").text)
        self.assertEqual("This field is required", driver.find_element_by_xpath("//form[@id='updateform']"
                                                                                "/table/tbody/tr[4]/td[2]/label").text)

    def test_detele_film(self):
        """ Проверка корректного удаления фильма.
        (на странице нет id фильма)"""
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("h1").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".movie_cover"))
        id_film = driver.find_element_by_css_selector(".movie_box").get_attribute('id')
        driver.find_element_by_css_selector(".movie_cover").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        self.assertFalse(self.is_element_present(By.ID,  id_film))

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
