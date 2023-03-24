# -*- coding: utf-8 -*-
# def test_open_parent_info(app):
#     app.parent.search_patient(search_name="SURNAME")
#     app.parent.open_parent_info()


def test_edit_parent_birthday(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_birthday(enter_value="05.05.1995")


def test_edit_parent_birthday_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_birthday_none()


def test_edit_parent_name(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_name(enter_value="PARENT-NAME")


def test_edit_parent_name_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_name_none()


def test_edit_parent_passport_number(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_passport_number(enter_value="7301 690033")


def test_edit_parent_passport_number_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_passport_number_none()


def test_parent_passport_unit_code(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_unit_code(enter_value="730-001")


def test_parent_passport_unit_code_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_unit_code_none()


def test_parent_passport_when(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_when(enter_value="10.05.2005")


def test_parent_passport_when_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_when_none()


def test_parent_passport_who(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_who(enter_value="УФМС")


def test_parent_passport_who_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_who_none()


def test_parent_secondname(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_secondname(enter_value="PARENT-SECONDNAME")


def test_parent_secondname_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_secondname_none()


def test_parent_surname(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_surname(enter_value="PARENT-SURNAME")


def test_parent_surname_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_surname_none()


def test_parent_sex_female(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_sex_female()


def test_parent_sex_male(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_sex_male()


def test_passport_unit_code(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.passport_unit_code(enter_value="730-002")


def test_passport_unit_code_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.passport_unit_code_none()
