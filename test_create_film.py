from model.film import Film
from model.user import User

#from selenium_fixture import app


def test_add_film(app):
    new_film = Film.unic_name()
    app.ensure_login_as(User.Admin())
    app.add_film(new_film)
    assert app.is_film_created(new_film)