# -*- coding: utf-8 -*-
from model.group import Group


def test_login_logout(app):
    app.session.login()
    app.session.logout()


def test_add_new_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.change_filial(filial="Филиал 2")
    # app.group.open_form_newclient()
    app.group.fill_newclient_form(
        Group(surname="ФамилияАвтоТест", name="Имя", secondname="Отчество", birthday="10102010", phone="79278889966",
              fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.session.logout()


def test_empty_clientdata(app):
    app.session.login(username="Директор1", password="123456")
    app.group.open_form_newclient()
    app.group.empty_newclient_form(Group(surname="", name="", secondname="", birthday="", phone="", fromwhere=""))
    # app.submit_newpatient_creation()
    app.session.logout()


def test_add_and_delete_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.change_filial(filial="Филиал 1")
    app.group.fill_newclient_form(
        Group(surname="Атест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient()
