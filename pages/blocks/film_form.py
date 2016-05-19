from pages.page import Page
from selenium.webdriver.support.select import Select


class FilmForm(Page):

    @property
    def name_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def submit_button(self):
        return self.driver.find_element_by_id("submit")