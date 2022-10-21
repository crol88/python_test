# # -*- coding: utf-8 -*-
# from model.group import Group
#
#
# def test_add_new_patient(app):
#     old_groups = app.cbase.get_group_list()
#     app.cbase.change_filial(Group(filial="Филиал 1"))
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Петров", name="Пётр", secondname="Петрович", birthday="10102010", phone="79278889966",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Иванов", name="Иван", secondname="Иванович", birthday="05061998", phone="79278815766",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Сидоров", name="Сидр", secondname="Сидорович", birthday="02102005", phone="79273145866",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Кузнецов", name="Кузнец", secondname="Кузнецович", birthday="12111990",
#               phone="79278881237", fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абаршев", name="Абар", secondname="Султанович", birthday="10102010", phone="79271235966",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абарыков", name="Тимур", secondname="Дмитриевич", birthday="03082002",
#               phone="79277853966", fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абахин", name="Михаил", secondname="Иванович", birthday="25081999", phone="79279644966",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абдуллин", name="Абдула", secondname="Владимирович", birthday="14051995",
#               phone="79271453966", fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абелин", name="Олег", secondname="Олегович", birthday="16051998", phone="79277563668",
#               fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     app.cbase.push_button_newClient()
#     app.cbase.fill_newclient_form(
#         Group(surname="Тест-Абелин", name="Владислав", secondname="Владимирович", birthday="16051998",
#               phone="79277563668", fromwhere="2ГИС"))
#     app.cbase.submit_newpatient_creation()
#     new_groups = app.cbase.get_group_list()
#     assert len(old_groups) + 10 == len(new_groups)
