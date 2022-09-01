from model.group import Group


def test_add_and_delete_patient(app):
    app.group.change_filial(Group(filial="Филиал 1"))
    app.group.fill_newclient_form(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient(search_name="Бтест")


def test_add_patient(app):
    app.group.add_patient(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                datapicker="12081980", phone="79058889556", fromwhere="2ГИС", filial="Филиал 1"))


def test_patient_for_search(app):
    app.group.change_filial(Group())
    app.group.fill_newclient_form(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()


def test_delete_patient(app):
    if app.group.count() == 0:
        app.group.add_patient_for_del(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                            datapicker="12081980", phone="79058889556", fromwhere="2ГИС",
                                            filial="Филиал 1"))
    app.group.delete_new_patient(search_name="Бтест")
