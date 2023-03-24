# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'квартира'")
def test_edit_fact_apartment(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_apartment(apt="8")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'квартира' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_apartment_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_apartment_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Дом'")
def test_edit_fact_house(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_house(building="12")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Дом' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_house_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_house_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Населенный пункт'")
def test_edit_fact_city(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_city(city="FACT-CITY")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Населенный пункт' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_city_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_city_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Страна'")
def test_edit_fact_country(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_country(country="FACT-COUNTRY")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Страна' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_country_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_country_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить почтовый индекс")
def test_edit_fact_postcode(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode(postcode="432005")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить почтовый индекс без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_postcode_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить регион пациента")
def test_edit_fact_state(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_state(state="FACT-STATE")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить регион пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_state_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_state_none()


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Улица'")
def test_edit_fact_street(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_street(street="FACT-STREET")


@allure.epic("Информация о пациенте. Фактический адрес")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Улица' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_fact_street_none(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.address.edit_fact_street_none()
