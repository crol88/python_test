import time

from model.group import Group
from model.group import Chair


def test_add_chair(app):
    app.settings.open_employees_chair()
    app.settings.add_chair(Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
    app.settings.check_chair(Chair(title="test-chair"))


def test_delete_chair(app):
    app.settings.open_employees_chair()
    old_list = app.settings.get_chair_list()
    app.settings.add_chair(Chair(title="del-chair", sorting="10", department="Терапевты", filial="Филиал 1"))
    app.settings.delete_chair(Chair(title="del-chair"))
    new_list = app.settings.get_chair_list()
    assert len(old_list) == len(new_list) - 1


def test_manual_add_user(app):
    app.settings.open_employees_users()
    app.settings.add_user()
    app.settings.fill_new_user_form(Group(login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))


def test_delete_user(app):
    app.settings.open_employees_users()
    app.settings.add_user()
    app.settings.fill_new_user_form(Group(login='del-user-test', mail='delmail@mail.ru', phone='79041871535'))
    app.settings.delete_user(Group(login='del-user-test'))


def test_add_doctor(app):
    app.settings.open_employees_doctor()
    app.settings.add_doctor(Group(login="new-user-test"))
    app.settings.add_department(department="Терапевты")
