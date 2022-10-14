# -*- coding: utf-8 -*-
import testit
# def test_open_parent_info(app):
#     app.parent.search_patient(search_name="SURNAME")
#     app.parent.open_parent_info()


@testit.displayName('edit_parent_birthday')
@testit.externalId('070')
def test_edit_parent_birthday(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_birthday(enter_value="05.05.1995")


@testit.displayName('edit_parent_birthday_none')
@testit.externalId('071')
def test_edit_parent_birthday_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_birthday_none()


@testit.displayName('edit_parent_name')
@testit.externalId('072')
def test_edit_parent_name(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_name(enter_value="PARENT-NAME")


@testit.displayName('edit_parent_name_none')
@testit.externalId('073')
def test_edit_parent_name_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_name_none()


@testit.displayName('edit_parent_passport_number')
@testit.externalId('074')
def test_edit_parent_passport_number(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_passport_number(enter_value="7301 690033")


@testit.displayName('edit_parent_passport_number_none')
@testit.externalId('075')
def test_edit_parent_passport_number_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.edit_parent_passport_number_none()


@testit.displayName('parent_passport_unit_code')
@testit.externalId('076')
def test_parent_passport_unit_code(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_unit_code(enter_value="730-001")


@testit.displayName('parent_passport_unit_code_none')
@testit.externalId('077')
def test_parent_passport_unit_code_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_unit_code_none()


@testit.displayName('parent_passport_when')
@testit.externalId('078')
def test_parent_passport_when(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_when(enter_value="10.05.2005")


@testit.displayName('parent_passport_when_none')
@testit.externalId('079')
def test_parent_passport_when_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_when_none()


@testit.displayName('parent_passport_who')
@testit.externalId('080')
def test_parent_passport_who(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_who(enter_value="УФМС")


@testit.displayName('parent_passport_who_none')
@testit.externalId('081')
def test_parent_passport_who_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_passport_who_none()


@testit.displayName('parent_secondname')
@testit.externalId('082')
def test_parent_secondname(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_secondname(enter_value="PARENT-SECONDNAME")


@testit.displayName('parent_secondname_none')
@testit.externalId('083')
def test_parent_secondname_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_secondname_none()


@testit.displayName('parent_surname')
@testit.externalId('084')
def test_parent_surname(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_surname(enter_value="PARENT-SURNAME")


@testit.displayName('parent_surname_none')
@testit.externalId('085')
def test_parent_surname_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_surname_none()


@testit.displayName('parent_sex_female')
@testit.externalId('086')
def test_parent_sex_female(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_sex_female()


@testit.displayName('parent_sex_male')
@testit.externalId('087')
def test_parent_sex_male(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.parent_sex_male()


@testit.displayName('passport_unit_code')
@testit.externalId('088')
def test_passport_unit_code(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.passport_unit_code(enter_value="730-002")


@testit.displayName('passport_unit_code_none')
@testit.externalId('089')
def test_passport_unit_code_none(app):
    app.parent.search_patient(search_name="SURNAME")
    app.parent.passport_unit_code_none()
