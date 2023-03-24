# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить нового пациента через «Список пациентов»")
@allure.description("Перед началом, проверить тестовые данные, при необходимости сгенерировать их")
def test_add_patient(app):
    old_list = app.cbase.get_group_list()
    group = Group(surname="New", name="Patient", secondname="Test", birthday="12081996",
                  phone="79058128556", fromwhere="2ГИС", filial="")
    app.cbase.add_patient(group)
    new_list = app.cbase.get_group_list()
    assert old_list + 1 == new_list
    print("old_list =", old_list + 1, ";", "new_list =", new_list)


@allure.epic("База пациентов")
@allure.tag("Настройки cbase")
@allure.title("Добавить нового пациента через «Список пациентов» с выключенным плагином")
@allure.description("Плагин cbase «Прикреплять пациента ко всем филиалам автоматически»")
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


@allure.epic("База пациентов")
@allure.tag("Настройки cbase")
@allure.title("Добавить нового пациента через «Список пациентов» с включенным плагином")
@allure.description("Плагин cbase «Прикреплять пациента ко всем филиалам автоматически»")
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
    app.cbase.check_filial_switch_on()


@allure.epic("База пациентов")
@allure.tag("Настройки cbase")
@allure.title("Отображать список пациентов только если заданы критерии поиска выкл")
@allure.description("Плагин cbase «Отображать список пациентов только если заданы критерии поиска»")
def test_patient_search_criteria_set_off(app):
    app.cbase_config.open_cbase_config()
    app.cbase_config.search_criteria_set(status='Включено')
    app.cbase.open_cbase_temp()
    app.cbase.empty_patient_list()


@allure.epic("База пациентов")
@allure.tag("Настройки cbase")
@allure.title("Отображать список пациентов только если заданы критерии поиска вкл")
@allure.description("Плагин cbase «Отображать список пациентов только если заданы критерии поиска»")
def test_patient_search_criteria_set_on(app):
    app.cbase_config.open_cbase_config()
    app.cbase_config.search_criteria_set(status='Отключено')
    app.cbase.open_cbase_temp()
    app.cbase.get_patient_list()


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить и удалить нового пациента")
@allure.description("Проверить кол-во записей в базе пациентов")
def test_add_and_delete_patient(app):
    old_groups = app.cbase.get_group_list()
    app.cbase.change_filial(Group(filial=""))
    app.cbase.fill_newclient_form(
        Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.cbase.submit_newpatient_creation()
    app.cbase.delete_new_patient(search_name="Пациент")
    new_groups = app.cbase.get_group_list()
    print("Кол-во пациентов до удаления:", old_groups, ';', 'Кол-во пациентов после удаления:', new_groups)
    assert old_groups == new_groups


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Удалить пациента")
@allure.description("Проверить кол-во записей в базе пациентов")
def test_delete_patient(app):
    old_groups = app.cbase.get_group_list()
    if app.cbase.count("Delete") == 0:
        app.cbase.add_patient_for(
            Group(surname="Delete", name="Patient", secondname="Test", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.delete_new_patient(search_name="Delete")
    new_groups = app.cbase.get_group_list()
    assert old_groups == new_groups


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без фамилии")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_surname(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="", name="Patient", secondname="Test",
                                         birthday="12081980", phone="79058875316", fromwhere="2ГИС"))
    app.cbase.check_empty_surname()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без имени")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_name(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="", secondname="Test",
                                         birthday="12081980", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_name()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без отчества")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_secondname(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="",
                                         birthday="12081980", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_secondname()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без даты рождения")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_birthday(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="", phone="79058837941", fromwhere="2ГИС"))
    app.cbase.check_empty_birthday()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без телефона")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_phone(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="12101987", phone="", fromwhere="2ГИС"))
    app.cbase.check_empty_phone()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить пациента без выбора «Откуда о нас узнали»")
@allure.description("Проверить отработку обязательных полей в форме добавление пациента")
def test_add_patient_empty_fromwhere(app):
    old_list = app.cbase.get_patient_list()
    app.cbase.open_form_newclient()
    app.cbase.empty_newclient_form(Group(surname="Surname", name="name", secondname="secondname",
                                         birthday="12101987", phone="79058837941", fromwhere=""))
    app.cbase.check_empty_fromwhere()
    new_list = app.cbase.get_patient_list()
    assert len(old_list) == len(new_list)
