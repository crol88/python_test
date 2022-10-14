# -*- coding: utf-8 -*-
import testit


@testit.displayName('edit_comments')
@testit.externalId('034')
def test_edit_comments(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments(comments="Comment")


@testit.displayName('edit_comments_none')
@testit.externalId('035')
def test_edit_comments_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments_none()


@testit.displayName('edit_first_record_date')
@testit.externalId('036')
def test_edit_first_record_date(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date(date="11.09.2001")


@testit.displayName('edit_first_record_date_none')
@testit.externalId('037')
def test_edit_first_record_date_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date_none()


@testit.displayName('edit_id1c')
@testit.externalId('038')
def test_edit_id1c(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c(id1c="073111")


@testit.displayName('edit_id1c_none')
@testit.externalId('039')
def test_edit_id1c_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c_none()


@testit.displayName('edit_fromwhere')
@testit.externalId('040')
def test_edit_fromwhere(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere()
    app.information.select_random_fromwhere()


@testit.displayName('edit_fromwhere_none')
@testit.externalId('041')
def test_edit_fromwhere_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere_none()


@testit.displayName('sms_status_no')
@testit.externalId('042')
def test_sms_status_no(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.edit_sms_status_no()


@testit.displayName('sms_status_yes(')
@testit.externalId('043')
def test_sms_status_yes(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.edit_sms_status_yes()


@testit.displayName('edit_points_field')
@testit.externalId('044')
def test_edit_points_field(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_points_field(points="points")


@testit.displayName('edit_points_field_none')
@testit.externalId('045')
def test_edit_points_field_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_points_field_none()


@testit.displayName('edit_total_summ')
@testit.externalId('046')
def test_edit_total_summ(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ(summ="100500")


@testit.displayName('edit_total_summ_none')
@testit.externalId('047')
def test_edit_total_summ_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ_none()
