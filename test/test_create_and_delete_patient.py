
from model.group import Group


def test_add_and_delete_patient(app):
    old_groups = app.group.get_group_list()
    app.group.change_filial(Group(filial="Филиал 1"))
    app.group.fill_newclient_form(
        Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient(search_name="Пациент")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_add_patient(app):
    old_groups = app.group.get_group_list()
    group = Group(surname="АТЕСТ-Добавить", name="Таблицы", secondname="БББ", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 2")
    app.group.add_patient(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_patient_for_search(app):
    if app.group.count("DРед-Фамилия") == 0:
        app.group.change_filial(Group())
        app.group.fill_newclient_form(
            Group(surname="Утест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС"))
        app.group.submit_newpatient_creation()


def test_delete_patient(app):
    if app.group.count("DРед-Фамилия") == 0:
        app.group.add_patient_for_del(
            Group(surname="Утест", name="Добавить", secondname="Удалить", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 1"))
    old_groups = app.group.get_group_list()
    app.group.delete_new_patient(search_name="Утест")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_del_patient(app):
    old_groups = app.group.get_group_list()
    app.group.delete_new_patient(search_name="ТЕСТ-Добавить")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
