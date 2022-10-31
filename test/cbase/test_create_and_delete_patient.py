# -*- coding: utf-8 -*-
import testit
from model.group import Group


@testit.workItemIds(5)
@testit.displayName('Добавление нового пациента')
@testit.externalId('1-001')
def test_add_patient(app):
    with testit.step('Сохранить список пациентов до действий пользователя'):
        old_list = app.cbase.get_patient_list()
    group = Group(surname="New", name="Patient", secondname="Test", birthday="12081996",
                  phone="79058128556", fromwhere="2ГИС", filial="")
    app.cbase.add_patient(group)
    with testit.step('Сохранить список пациентов после действий пользователя'):
        new_list = app.cbase.get_group_list()
    with testit.step('Проверить, что пациент добавлен в список'):
        assert len(old_list) + 1 == len(new_list)
        print("old_list =", len(old_list) + 1, ";", "new_list =", len(new_list))


def test_add_patient_without_filial_plugin_off(app):
    app.cbase_config.open_cbase_config()
    app.cbase_config.client_branch_activate(status="Отключено")
    # app.cbase.fill_newclient_form(
    #     Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
    #           fromwhere="2ГИС"))


def test_add_and_delete_patient(app):
    old_groups = app.cbase.get_group_list()
    app.cbase.change_filial(Group(filial="Филиал 1"))
    app.cbase.fill_newclient_form(
        Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.cbase.submit_newpatient_creation()
    app.cbase.delete_new_patient(search_name="Пациент")
    new_groups = app.cbase.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_patient_for_search(app):
    if app.cbase.count("АТЕСТ-Добавить") == 0:
        app.cbase.change_filial(Group())
        app.cbase.fill_newclient_form(
            Group(surname="Утест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС"))
        app.cbase.submit_newpatient_creation()


@testit.displayName('Удаление пациента')
@testit.externalId('test_delete_patient')
def test_delete_patient(app):
    with testit.step('Открыть список пациентов и проверить наличие пациента'):
        if app.cbase.count("NEW") == 0:
            with testit.step('Если пациент отсутствует, добавляем'):
                app.cbase.add_patient_for(
                    Group(surname="New", name="Patient", secondname="Test", birthday="12081980",
                          phone="79058889556",
                          fromwhere="2ГИС", filial=""))
    with testit.step('Сохранить список пациентов до удаления'):
        old_groups = app.cbase.get_group_list()
    with testit.step('Найти и удалить пациента'):
        app.cbase.delete_new_patient(search_name="NEW")
    with testit.step('Сохранить список пациентов после удаления'):
        new_groups = app.cbase.get_group_list()
    with testit.step('Сравнить списки, убедиться, что пациент удален'):
        assert len(old_groups) - 1 == len(new_groups)
        old_groups[0:1] = []
        assert old_groups == new_groups


def test_del_patient(app):
    old_groups = app.cbase.get_group_list()
    app.cbase.delete_new_patient(search_name="ТЕСТ-Добавить")
    new_groups = app.cbase.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
