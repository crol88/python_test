from model.group import Group


def test_add_and_delete_patient(app):
    # app.session.login(username="Директор1", password="123456")
    app.group.change_filial(filial="Филиал 1")
    app.group.fill_newclient_form(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient(search_name="Бтест")
    # app.session.logout()


def test_patient_for_search(app):
    app.group.change_filial(filial="Филиал 1")
    app.group.fill_newclient_form(Group(surname="Бтест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()


def test_search_patient(app):
    # app.session.login(username="Директор1", password="123456")
    app.group.edit_patient_data(search_name="ФамилияАвтоТест")
    # app.session.logout()


def test_delete_patient(app):
    # app.session.login(username="Директор1", password="123456")
    app.group.delete_new_patient(search_name="Бтест")
    # app.session.logout()
