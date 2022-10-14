# -*- coding: utf-8 -*-
import testit


@testit.displayName('edit_city_phone')
@testit.externalId('048')
def test_edit_city_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_city_phone(phone="123456")


@testit.displayName('edit_city_phone_none')
@testit.externalId('049')
def test_edit_city_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_city_phone_none()


@testit.displayName('edit_email')
@testit.externalId('050')
def test_edit_email(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_email(mail="TEST@TEST.COM")


@testit.displayName('edit_email_none')
@testit.externalId('051')
def test_edit_email_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_email_none()


@testit.displayName('edit_mobile_phone')
@testit.externalId('052')
def test_edit_mobile_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_mobile_phone(mobile="79051501245")


@testit.displayName('edit_mobile_phone_none')
@testit.externalId('053')
def test_edit_mobile_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_mobile_phone_none()


@testit.displayName('edit_phone')
@testit.externalId('054')
def test_edit_phone(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_phone(phone="79051504578")


@testit.displayName('edit_phone_none')
@testit.externalId('055')
def test_edit_phone_none(app):
    app.contact.search_patient(search_name="SURNAME")
    app.contact.edit_phone_none()
