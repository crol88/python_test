from model.group import Group


def test_edit_patient_name(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(name="new name"))
    app.session.logout()


def test_edit_patient_surname(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(name="new surname"))
    app.session.logout()


def test_edit_patient_secondname(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(name="new secondname"))
    app.session.logout()


def test_edit_patient_birthday(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(name="new datapicker"))
    app.session.logout()


def test_edit_patient_fromwhere(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(name="new fromwhere"))
    app.session.logout()


def test_edit_patient_phone(app):
    app.session.login(username="Директор1", password="123456")
    app.group.modify(Group(phone="new phone"))
    app.session.logout()
