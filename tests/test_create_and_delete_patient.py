# -*- coding: utf-8 -*-
import testit
from model.group import Group


@testit.displayName('Добавление нового пациента')
@testit.externalID('test_add_patient')
def test_add_patient(app):
    old_list = app.cbase.get_patient_list()
    group = Group(surname="АТЕСТ-Добавить", name="Таблицы", secondname="БББ", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 2")
    app.cbase.add_patient(group)
    new_list = app.cbase.get_group_list()
    assert len(old_list) + 1 == len(new_list)
    print("old_list =", len(old_list) + 1, ";", "new_list =", len(new_list))


@testit.displayName('test_add_and_delete_patient')
@testit.externalID('test_add_patient')
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
#
#
# def test_patient_for_search(app):
#     if app.cbase.count("АТЕСТ-Добавить") == 0:
#         app.cbase.change_filial(Group())
#         app.cbase.fill_newclient_form(
#             Group(surname="Утест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
#                   fromwhere="2ГИС"))
#         app.cbase.submit_newpatient_creation()


# @testit.externalID('Simple_autotest2_{name}')
# @testit.displayName('Simple autotest 2 - {name}')
# def test_delete_patient(app):
#     if app.cbase.count("DРед-Фамилия") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="Утест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
#                   fromwhere="2ГИС", filial="Филиал 1"))
#     old_groups = app.cbase.get_group_list()
#     app.cbase.delete_new_patient(search_name="Утест")
#     new_groups = app.cbase.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []
#     assert old_groups == new_groups


# def test_del_patient(app):
#     old_groups = app.cbase.get_group_list()
#     app.cbase.delete_new_patient(search_name="ТЕСТ-Добавить")
#     new_groups = app.cbase.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []
#     assert old_groups == new_groups
