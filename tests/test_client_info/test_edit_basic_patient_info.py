# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести фамилию пациента и сохранить")
def test_edit_patient_surname(app):
    if app.basic_info.count(check_patient="SURNAME") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"))


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить фамилию пациента без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_surname_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME-EDIT", name="name", secondname="secondname", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_surname_fill(text="SURNAME-EDIT")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести имя пациента и сохранить")
def test_edit_patient_name(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname-edit", name="name", secondname="secondname", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="surname-edit")
    app.basic_info.edit_patient_name(Group(name="NAME-EDIT"))


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить имя пациента без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_name_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname-edit", name="name", secondname="secondname", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_name_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести отчество пациента и сохранить")
def test_edit_patient_secondname(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_secondname(Group(secondname="SECONDNAME-EDIT"))


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить отчество пациента без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_secondname_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_secondname_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести дату рождения пациента и сохранить")
def test_edit_patient_birthday(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_birthday(Group(birthday="21.12.1999"))


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить дату рождения без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_birthday_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME-EDIT")
    app.basic_info.edit_patient_birthday_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Выбрать мужской пол пациента и сохранить")
def test_edit_patient_sex_male(app):
    if app.basic_info.count(check_patient="SEX-MALE") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SEX-MALE", name="ПОЛ", secondname="МУЖСКОЙ", birthday="21101984",
                  phone="79051593692",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SEX-MALE")
    app.basic_info.edit_patient_sex(sex="Мужской")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить пол пациента без изменений")
def test_edit_patient_sex_male_without_changes(app):
    if app.basic_info.count(check_patient="SEX-MALE") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SEX-MALE", name="ПОЛ", secondname="МУЖСКОЙ", birthday="21101984",
                  phone="79051593692",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SEX-MALE")
    app.basic_info.edit_patient_sex_male_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Выбрать женский пол пациента и сохранить")
def test_edit_patient_sex_female(app):
    if app.basic_info.count(check_patient="SEX-FEMALE") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SEX-FEMALE", name="ПОЛ", secondname="Женский", birthday="23101985",
                  phone="79051151254",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SEX-FEMALE")
    app.basic_info.edit_patient_sex(sex="Женский")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить инн пациента")
def test_edit_patient_inn(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_inn(inn="736833331215")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить инн пациента без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_inn_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_inn_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поле 'Страна'")
def test_edit_patient_country(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_country(country="country-edit")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поле 'Страна' без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_country_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_country_fill()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить почтовый индекс")
def test_edit_patient_postcode(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_postcode(postcode="432001")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить почтовый индекс без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_postcode_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_postcode_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить 'Область' пациента")
def test_edit_patient_state(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_state(state="State")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить 'Область' пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_state_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_state_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить 'Город' пациента")
def test_edit_patient_city(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_city(city="city")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить 'Город' пациента без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_city_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_city_without_changes()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Улица'")
def test_edit_patient_street(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_street(street="street")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Улица' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_street_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_street_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Дом'")
def test_edit_patient_building(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_building(building="4")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Дом' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_building_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_building_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Квартира'")
def test_edit_patient_apartment(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_apartment(apt="56")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Квартира' без редактирования")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_apartment_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_apartment_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить значение поля 'Адрес'")
def test_edit_patient_address(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_address(address="testaddress")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Адрес' без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_address_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_address_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить дату первого приема")
def test_edit_patient_first_data(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_first_data(date="31.12.2021")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить дату первого приема без изменений")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_first_data_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_first_data_none()


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Редактировать и сохранить дату последнего приема")
def test_edit_patient_last_data(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_last_data(date="10.10.2021")


@allure.epic("Информация о пациенте. Основная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить дату последнего приема без изменения")
@allure.description("Проверить, что после активации поля ввода, сохраняются ранее введенные данные")
def test_edit_patient_last_data_without_changes(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="surname", name="name", secondname="secondname", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_last_data_none()
