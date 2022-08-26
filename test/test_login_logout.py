# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.open_form_newclient()
    app.group.fill_newclient_form(Group(surname="ФамилияАвтоТест", name="Имя", secondname="Отчество",
                                        datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()


def test_empty_clientdata(app):
    app.session.login(username="Директор1", password="123456")
    app.group.fill_newclient_form(Group(surname="", name="", secondname="",
                                        datapicker="", phone="", fromwhere=""))
    # app.submit_newpatient_creation()


def test_add_and_delete_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.change_filial(filial="Филиал 1")
    app.group.fill_newclient_form(Group(surname="Атест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient()
