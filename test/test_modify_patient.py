from model.group import Group


def test_edit_patient_name(app):
    app.session.login(username="Директор1", password="123456")
    app.group.edit_patient_data(Group(name="new name"))
    app.session.logout()


def test_edit_patient_surname(app):
    app.session.login(username="Директор1", password="123456")
    app.group.search_patient(search_name="Редактор")
    app.group.edit_patient_data(Group(surname="АААТест"))
    app.session.logout()


def test_edit_patient_secondname(app):
    app.session.login(username="Директор1", password="123456")
    app.group.edit_patient_data(Group(secondname="new secondname"))
    app.session.logout()
