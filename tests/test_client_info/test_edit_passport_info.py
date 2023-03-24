# -*- coding: utf-8 -*-
# def test(app):
#     app.passport.search_patient(search_name="SURNAME")
#     app.passport.open_passport_info()


def test_edit_copy_passport_value_yes(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_copy_passport_value_yes()


def test_edit_copy_passport_value_no(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_copy_passport_value_no()


def test_edit_passport_address(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address(registration="PASS-ADDRESS")


def test_edit_passport_address_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_none()


def test_edit_passport_address_live(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_live(address="ADDRESS-LIVE")


def test_edit_passport_address_live_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_live_none()


def test_edit_passport_number(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_number(passport="7300 690000")


def test_edit_passport_number_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_number_none()


def test_edit_passport_issue_date(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_issue_date(data="10.12.2016")


def test_edit_passport_issue_date_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_issue_date_none()


def test_edit_passport_who(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_who(who="UFMS")


def test_edit_passport_who_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_who_none()
