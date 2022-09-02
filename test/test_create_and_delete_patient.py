from model.group import Group


def test_add_and_delete_patient(app):
    old_groups = app.group.get_group_list()
    app.group.change_filial(Group(filial="Филиал 1"))
    app.group.fill_newclient_form(Group(surname="Пациент", name="Для", secondname="Удаления",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient(search_name="Пациент")
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_add_patient(app):
    old_groups = app.group.get_group_list()
    app.group.add_patient(Group(surname="Проверка", name="Таблица", secondname="Ааа",
                                datapicker="12081980", phone="79058889556", fromwhere="2ГИС", filial="Филиал 2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_patient_for_search(app):
    app.group.change_filial(Group())
    app.group.fill_newclient_form(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()


def test_delete_patient(app):
    if app.group.count() == 0:
        app.group.add_patient_for_del(Group(surname="Утест", name="Добавить", secondname="Удалить",
                                            datapicker="12081980", phone="79058889556", fromwhere="2ГИС",
                                            filial="Филиал 1"))
    app.group.delete_new_patient(search_name="Утест")


def test_del_patient(app):
    old_groups = app.group.get_group_list()
    app.group.delete_new_patient(search_name="Бтест")
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
