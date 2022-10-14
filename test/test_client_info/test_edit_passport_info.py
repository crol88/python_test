# -*- coding: utf-8 -*-
import testit
# def test(app):
#     app.passport.search_patient(search_name="SURNAME")
#     app.passport.open_passport_info()


@testit.displayName('edit_copy_passport_value_yes')
@testit.externalId('090')
def test_edit_copy_passport_value_yes(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_copy_passport_value_yes()


@testit.displayName('edit_copy_passport_value_no')
@testit.externalId('091')
def test_edit_copy_passport_value_no(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_copy_passport_value_no()


@testit.displayName('edit_passport_address')
@testit.externalId('092')
def test_edit_passport_address(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address(registration="PASS-ADDRESS")


@testit.displayName('edit_passport_address_none')
@testit.externalId('093')
def test_edit_passport_address_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_none()


@testit.displayName('edit_passport_address_live')
@testit.externalId('094')
def test_edit_passport_address_live(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_live(address="ADDRESS-LIVE")


@testit.displayName('edit_passport_address_live_none')
@testit.externalId('095')
def test_edit_passport_address_live_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_address_live_none()


@testit.displayName('edit_passport_number')
@testit.externalId('096')
def test_edit_passport_number(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_number(passport="7300 690000")


@testit.displayName('edit_passport_number_none')
@testit.externalId('097')
def test_edit_passport_number_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_number_none()


@testit.displayName('edit_passport_issue_date')
@testit.externalId('098')
def test_edit_passport_issue_date(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_issue_date(data="10.12.2016")


@testit.displayName('edit_passport_issue_date_none')
@testit.externalId('099')
def test_edit_passport_issue_date_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_issue_date_none()


@testit.displayName('edit_passport_who')
@testit.externalId('100')
def test_edit_passport_who(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_who(who="UFMS")


@testit.displayName('passport_unit_code_none')
@testit.externalId('101')
def test_edit_passport_who_none(app):
    app.passport.search_patient(search_name="SURNAME")
    app.passport.edit_passport_who_none()
