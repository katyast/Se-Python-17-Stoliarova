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

base_url = cp.parser.get('url', 'base_url')
username = cp.parser.get('login', 'username')
password = cp.parser.get('login', 'password')

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_new_film(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("unic_title")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2012")
        driver.find_element_by_id("submit").click()
        self.assertEqual("unic_title (2012)", driver.find_element_by_css_selector("h2").text)

    def test_field_form_created_new_film_is_required(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("h1").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("002")
        driver.find_element_by_id("submit").click()
        self.assertEqual("This field is required", driver.find_element_by_css_selector("label.error").text)
        self.assertEqual("This field is required", driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label").text)

    def test_detele_film(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver = mainFunctions.Authorization.login(self, username, password)
        driver.find_element_by_css_selector("h1").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"title\"]"))
        driver.find_element_by_css_selector("img[alt=\"title\"]").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        self.assertEqual("No movies where found.", driver.find_element_by_css_selector("div.content").text)

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
