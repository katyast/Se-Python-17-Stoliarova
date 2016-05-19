from pages.page import Page
from selenium.webdriver.common.by import By


class ViewFilm(Page):

    @property
    def film_delete_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= 'delete']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, ".maininfo_full > h2:nth-child(1)"))

    @property
    def film_name(self):
        return self.driver.find_element_by_css_selector(".maininfo_full > h2:nth-child(1)")
