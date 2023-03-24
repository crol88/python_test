# -*- coding: utf-8 -*-
import allure
from model.group import Group


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить городской телефон")
def test_edit_city_phone(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_city_phone(phone="123456")


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить городской телефон без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_city_phone_none(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_city_phone_none()


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить E-mail пациента")
def test_edit_email(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_email(mail="test@test.com")


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить E-mail пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_email_none(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_email_none()


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить мобильный телефон пациента")
def test_edit_mobile_phone(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_mobile_phone(mobile="79051501245")


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить мобильный телефон пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_mobile_phone_none(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_mobile_phone_none()


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить другой телефон пациента")
def test_edit_phone(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_phone(phone="79051504578")


@allure.epic("Информация о пациенте. Контактная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить другой телефон пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_phone_none(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.contact.edit_phone_none()
