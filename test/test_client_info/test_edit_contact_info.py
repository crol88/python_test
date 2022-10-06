# -*- coding: utf-8 -*-

def test_edit_city_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_city_phone(phone="123456")


def test_edit_city_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_city_phone_none()


def test_edit_email(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_email(mail="TEST@TEST.COM")


def test_edit_email_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_email_none()


def test_edit_mobile_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_mobile_phone(mobile="79051501245")


def test_edit_mobile_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_mobile_phone_none()


def test_edit_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_phone(phone="79051504578")


def test_edit_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_phone_none()
