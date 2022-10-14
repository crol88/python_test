# -*- coding: utf-8 -*-
from model.group import Group
import testit

# def test(app):
# app.basic_info.open_random_patient()


@testit.workItemIds(261)
@testit.displayName('edit_patient_surname')
@testit.externalId('001')
def test_edit_patient_surname(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")


@testit.displayName('edit_patient_surname_without_changes')
@testit.externalId('002')
def test_edit_patient_surname_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_surname_fill(text="SURNAME-EDIT")


@testit.displayName('edit_patient_name')
@testit.externalId('003')
def test_edit_patient_name(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname-edit", name="name", secondname="secondname", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="surname-edit")
    app.basic_info.edit_patient_name(Group(name="NAME-EDIT"), text="NAME-EDIT")


@testit.displayName('edit_patient_name_without_changes')
@testit.externalId('004')
def test_edit_patient_name_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_name_fill()


@testit.displayName('edit_patient_secondname')
@testit.externalId('005')
def test_edit_patient_secondname(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_secondname(Group(secondname="SECONDNAME-EDIT"), text="SECONDNAME-EDIT")


@testit.displayName('edit_patient_secondname_without_changes')
@testit.externalId('006')
def test_edit_patient_secondname_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_secondname_fill(text="SECONDNAME-EDIT")


@testit.displayName('edit_patient_birthday')
@testit.externalId('007')
def test_edit_patient_birthday(app):
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_birthday(Group(birthday="21.12.1999"), text="21.12.1999")


@testit.displayName('edit_patient_birthday_without_changes')
@testit.externalId('008')
def test_edit_patient_birthday_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_birthday_fill()


@testit.displayName('edit_patient_sex_male')
@testit.externalId('009')
def test_edit_patient_sex_male(app):
    if app.basic_info.count(check_patient="SEX-MALE") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SEX-MALE", name="ПОЛ", secondname="МУЖСКОЙ", birthday="21101984",
                  phone="79051593692",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="SEX-MALE")
    app.basic_info.edit_patient_sex(sex="Мужской")


@testit.displayName('edit_patient_sex_male_without_changes')
@testit.externalId('010')
def test_edit_patient_sex_male_without_changes(app):
    app.basic_info.search_patient(search_name="SEX-MALE")
    app.basic_info.edit_patient_sex_male_fill()


@testit.displayName('edit_patient_sex_female')
@testit.externalId('011')
def test_edit_patient_sex_female(app):
    if app.basic_info.count(check_patient="SEX-FEMALE") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SEX-FEMALE", name="ПОЛ", secondname="Женский", birthday="23101985",
                  phone="79051151254",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.basic_info.search_patient(search_name="SEX-FEMALE")
    app.basic_info.edit_patient_sex(sex="Женский")


@testit.displayName('edit_patient_sex_female')
@testit.externalId('012')
def test_edit_patient_sex_female(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_inn(inn="736833331215")


@testit.displayName('edit_patient_inn_without_changes')
@testit.externalId('013')
def test_edit_patient_inn_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_inn_fill()


@testit.displayName('edit_patient_country')
@testit.externalId('014')
def test_edit_patient_country(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_country(country="country-edit")


@testit.displayName('edit_patient_country_without_changes')
@testit.externalId('015')
def test_edit_patient_country_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_country_fill()


@testit.displayName('edit_patient_postcode')
@testit.externalId('016')
def test_edit_patient_postcode(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_postcode(postcode="432001")


@testit.displayName('edit_patient_postcode_without_changes')
@testit.externalId('017')
def test_edit_patient_postcode_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_postcode_none()


@testit.displayName('edit_patient_state')
@testit.externalId('018')
def test_edit_patient_state(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_state(state="State")


@testit.displayName('edit_patient_state_without_changes')
@testit.externalId('019')
def test_edit_patient_state_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_state_none()


@testit.displayName('edit_patient_city')
@testit.externalId('020')
def test_edit_patient_city(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_city(city="city")


@testit.displayName('edit_patient_city_without_changes')
@testit.externalId('021')
def test_edit_patient_city_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_city_without_changes()


@testit.displayName('edit_patient_street')
@testit.externalId('022')
def test_edit_patient_street(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_street(street="street")


@testit.displayName('edit_patient_street_without_changes')
@testit.externalId('023')
def test_edit_patient_street_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_street_none()


@testit.displayName('test_edit_patient_building')
@testit.externalId('024')
def test_edit_patient_building(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_building(building="4")


@testit.displayName('edit_patient_building_without_changes')
@testit.externalId('025')
def test_edit_patient_building_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_building_none()


@testit.displayName('edit_patient_apartment')
@testit.externalId('026')
def test_edit_patient_apartment(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_apartment(apt="56")


@testit.displayName('edit_patient_apartment_without_changes')
@testit.externalId('027')
def test_edit_patient_apartment_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_apartment_none()


@testit.displayName('edit_patient_address')
@testit.externalId('028')
def test_edit_patient_address(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_address(address="testaddress")


@testit.displayName('edit_patient_address_without_changes')
@testit.externalId('029')
def test_edit_patient_address_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_address_none()


@testit.displayName('edit_patient_first_data')
@testit.externalId('030')
def test_edit_patient_first_data(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_first_data(data="31.12.2021")


@testit.displayName('edit_patient_first_data_without_changes')
@testit.externalId('031')
def test_edit_patient_first_data_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_first_data_none()


@testit.displayName('edit_patient_last_data')
@testit.externalId('032')
def test_edit_patient_last_data(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_last_data(data="10.10.2021")


@testit.displayName('edit_patient_last_data_without_changes')
@testit.externalId('033')
def test_edit_patient_last_data_without_changes(app):
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_last_data_none()
