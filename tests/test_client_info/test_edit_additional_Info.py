# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести комментарий и сохранить")
def test_edit_comments(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments(comments="Comment")


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить комментарий без изменений")
def test_edit_comments_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments_none()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести и сохранить дату первой записи")
def test_edit_first_record_date(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date(date="11.09.2001")


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить дату первой записи без изменения")
def test_edit_first_record_date_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date_none()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести и сохранить 1с id")
def test_edit_id1c(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c(id1c="073111")


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить 1с id без изменений")
def test_edit_id1c_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c_none()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Выбрать и сохранить значение поля 'Откуда узнали'")
def test_edit_fromwhere(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere()
    # app.information.select_random_fromwhere()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Откуда узнали' без изменений")
def test_edit_fromwhere_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere_none()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Не отправлять SMS")
def test_sms_status_no(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_sms_status_no()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Отправлять SMS")
def test_sms_status_yes(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_sms_status_yes()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести и сохранить значение поля 'Очки'")
def test_edit_points_field(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_field_points(points="points")


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Очки' без изменений")
def test_edit_points_field_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_field_points_none()


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Ввести и сохранить значение поля 'Сумма за лечение'")
def test_edit_total_summ(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ(summ="100500")


@allure.epic("Информация о пациенте. Дополнительная информация")
@allure.tag("Инфокарта пациента")
@allure.title("Сохранить значение поля 'Сумма за лечение' без изменений")
def test_edit_total_summ_none(app):
    if app.cbase.count("SURNAME") == 0:
        app.cbase.add_patient_for(
            Group(surname="SURNAME", name="name", secondname="secondname", birthday="17071977",
                  phone="79058143656", fromwhere="2ГИС", filial=""))
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ_none()
