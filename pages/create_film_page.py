from pages.internal_page import InternalPage
from pages.blocks.film_form import FilmForm
from selenium.webdriver.support.select import Select


class CreateFilmPage(InternalPage):

    def __init__(self, driver, base_url):
        super(CreateFilmPage, self).__init__(driver, base_url)
        self.film_form = FilmForm(self.driver, self.base_url)