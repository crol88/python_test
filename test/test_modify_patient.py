from model.group import Group


def test_edit_patient_name(app):
    app.group.search_patient(search_name="Абелин")
    app.group.edit_patient_data(Group(name="АТест-ред-имя"))


def test_edit_patient_surname(app):
    app.group.search_patient(search_name="Абелин")
    app.group.edit_patient_data(Group(surname="АТест-Ред-Фамилия"))


def test_edit_patient_secondname(app):
    app.group.search_patient(search_name="АБАРШЕВ-ТЕСТ")
    app.group.edit_patient_data(Group(secondname="Ред-Отчество"))
