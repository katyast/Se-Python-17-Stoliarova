from model.user import User
from selenium_fixture import app


def test_add_user(app):
    new_user = User.random()
    app.login(User.Admin())
    app.add_user(new_user)
    app.logout()
    app.login(new_user)
    assert app.is_logged_in()
    app.logout()