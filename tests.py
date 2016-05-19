# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import config as cp
import datetime
from selenium import webdriver
from selenium.common.exceptions import *
from model.user import User
from selenium_fixture import app
from selenium.webdriver.support import expected_conditions as EC



base_url = cp.parser.get('url', 'base_url')
username = cp.parser.get('login', 'username')
password = cp.parser.get('login', 'password')
now_time = datetime.datetime.now()
now_time = str(now_time)
film_name = "unic_title_" + now_time


def test_login_with_valid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()


def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.random())
    assert app.is_not_logged_in()

# def test_create_new_film(driver):
#     """ Проверка корректного создания фильма.
#     (на странице присутствует уникальное имя фильма)"""
#     driver.get(base_url)
#     driver = mainFunctions.Authorization.login(username, password)
#     driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
#     driver.find_element_by_name("name").clear()
#     driver.find_element_by_name("name").send_keys(film_name)
#     driver.find_element_by_name("year").clear()
#     driver.find_element_by_name("year").send_keys("2012")
#     driver.find_element_by_id("submit").click()
#     body_text = driver.find_element_by_css_selector(".maininfo_full > h2:nth-child(1)").text
#     driver.assertTrue(film_name, body_text)

    # def test_field_form_created_new_film_is_required(self):
    #     """ Проверка обязательности полей на форме создания фильма.
    #     (сообщения об ошибках при незаполненных полях)"""
    #     driver = self.driver
    #     driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
    #     driver = mainFunctions.Authorization.login(self, username, password)
    #     driver.find_element_by_css_selector("h1").click()
    #     driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    #     driver.find_element_by_name("imdbid").clear()
    #     driver.find_element_by_name("imdbid").send_keys("002")
    #     driver.find_element_by_id("submit").click()
    #     self.assertEqual("This field is required", driver.find_element_by_css_selector("label.error").text)
    #     self.assertEqual("This field is required", driver.find_element_by_xpath("//form[@id='updateform']"
    #                                                                             "/table/tbody/tr[4]/td[2]/label").text)
    #
    # def test_detele_film(self):
    #     """ Проверка корректного удаления фильма.
    #     (на странице нет id фильма)"""
    #     driver = self.driver
    #     driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
    #     driver = mainFunctions.Authorization.login(self, username, password)
    #     driver.find_element_by_css_selector("h1").click()
    #     self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".movie_cover"))
    #     id_film = driver.find_element_by_css_selector(".movie_box").get_attribute('id')
    #     driver.find_element_by_css_selector(".movie_cover").click()
    #     driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
    #     self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
    #     self.assertFalse(self.is_element_present(By.ID,  id_film))
    #
    # def test_search_exist_film(self):
    #     """ Поиск успешного поиска фильмов.
    #     Выбираем фильм на главной странице, вводим его название в поле поиска.
    #     Проверяем, что фильм присутствует на странице результатов """
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver = mainFunctions.Authorization.login(self, username, password)
    #     self.film_name = driver.find_element_by_css_selector(".title").text
    #     driver.find_element_by_id("q").clear()
    #     driver.find_element_by_id("q").send_keys(self.film_name)
    #     driver.find_element_by_id("q").send_keys(Keys.ENTER)
    #     self.assertEquals(driver.find_element_by_css_selector(".title").text, self.film_name)
    #
    # def test_search_no_exist_film(self):
    #     """ Проверка вывода сообщения о не найденом фильме."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver = mainFunctions.Authorization.login(self, username, password)
    #     driver.find_element_by_id("q").clear()
    #     driver.find_element_by_id("q").send_keys(u"такого фильма не существует")
    #     driver.find_element_by_id("q").send_keys(Keys.ENTER)
    #     self.assertEqual("No movies where found.", driver.find_element_by_css_selector("div.content").text)
    #
    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    #
    #
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)