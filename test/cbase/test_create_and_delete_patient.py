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
    app.cbase_config.client_branch_status(status="Отключено")
    app.cbase.select_all_filial(filial="Все филиалы")
    app.cbase.open_cbase()
    if app.cbase.count("PLUGIN-OFF") == 0:
        app.cbase.add_patient_for(
            Group(surname="Plugin-off", name="Client", secondname="Branch", birthday="19071997",
                  phone="79058547856", fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="PLUGIN-OFF")
    app.cbase.check_filial_info()


def test_add_patient_without_filial_plugin_on(app):
    app.cbase_config.open_cbase_config()
    app.cbase_config.client_branch_status(status="Включено")
    app.cbase.select_all_filial(filial="Все филиалы")
    app.cbase.open_cbase()
    if app.cbase.count("PLUGIN-ON") == 0:
        app.cbase.add_patient_for(
            Group(surname="Plugin-on", name="Client", secondname="Branch", birthday="19071997",
                  phone="79058547856", fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="PLUGIN-ON")
    app.cbase.check_filial_info()


def test_add_and_delete_patient(app):
    # old_groups = app.cbase.get_group_list()
    old_groups = app.cbase.get_patient_list()
    app.cbase.change_filial(Group(filial=""))
    app.cbase.fill_newclient_form(
        Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.cbase.submit_newpatient_creation()
    app.cbase.delete_new_patient(search_name="Пациент")
    # new_groups = app.cbase.get_group_list()
    new_groups = app.cbase.get_group_list()
    print("Кол-во пациентов до удаления:", len(old_groups), ';', 'Кол-во пациентов после удаления:', len(new_groups))
    assert len(old_groups) == len(new_groups)


def test_patient_for_search(app):
    if app.cbase.count("АТЕСТ-Добавить") == 0:
        # app.cbase.change_filial(Group())
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
    app.cbase.delete_new_patient(search_name="NEW")
    new_groups = app.cbase.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_add_patient_empty_surname(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="", name="Patient", secondname="Test",
                                         birthday="12081980", phone="79058875316", fromwhere="2ГИС"))
    app.cbase.check_empty_surname()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


def test_add_patient_empty_name(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="", secondname="Test",
                                         birthday="12081980", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_name()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


def test_add_patient_empty_secondname(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="",
                                         birthday="12081980", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_secondname()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


def test_add_patient_empty_birthday(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_birthday()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


def test_add_patient_empty_phone(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="12101987", phone="", fromwhere="2ГИС"))
    app.cbase.check_empty_phone()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


def test_add_patient_empty_fromwhere(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="12101987", phone="79058837941", fromwhere=""))
    app.cbase.check_empty_fromwhere()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)
