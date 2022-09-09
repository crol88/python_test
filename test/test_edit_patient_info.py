from model.group import Group


# def test_edit_basic_patient_info(app):
#     app.basic.search_patient(search_name="Тест-Добавить")
#     basic_patient_info = app.basic.get_basic_patient_info()
#     edit_basic_patient_info = app.basic.get_basic_patient_info_after_edit()
#     assert basic_patient_info.surname == edit_basic_patient_info.surname
#     assert basic_patient_info.name == edit_basic_patient_info.name
#     assert basic_patient_info.secondname == edit_basic_patient_info.secondname
#     assert basic_patient_info.birthday == edit_basic_patient_info.birthday


def test_edit_patient_surname(app):
    if app.group.count(check_patient="SURNAME") == 0:
        app.group.add_patient_for_del(
            Group(surname="Surname-create", name="Артур", secondname="Артурович", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="Surname-create")
    app.group.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")


def test_open_close_edit_patient_surname(app):
    # Активировать поле фамилия и сохранить без изменений
    if app.group.count(check_patient="SURNAME-EDIT") == 0:
        app.group.add_patient_for_del(
            Group(surname="DРед-Фамилия", name="Добавить", secondname="Удалить", birthday="16101982",
                  phone="79067426332",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SURNAME-EDIT")
    app.group.edit_patient_surname_fill(text="SURNAME-EDIT")


def test_edit_patient_name(app):
    if app.group.count(check_patient="SURNAME-EDIT") == 0:
        app.group.add_patient_for_del(
            Group(surname="АААТест-редимя", name="Тест-редимя", secondname="Тест-редимя", birthday="16071979",
                  phone="79057147232",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="surname-edit")
    app.group.edit_patient_name(Group(name="NAME-EDIT"), text="NAME-EDIT")


def test_edit_patient_secondname(app):
    if app.group.count(check_patient="SURNAME-EDIT") == 0:
        app.group.add_patient_for_del(
            Group(surname="АААТест-редимя", name="Тест-ред", secondname="Тест-редотчество", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SURNAME-EDIT")
    app.group.edit_patient_secondname(Group(secondname="SECONDNAME-EDIT"), text="SECONDNAME-EDIT")


def test_edit_patient_birthday(app):
    if app.group.count(check_patient="SURNAME") == 0:
        app.group.add_patient_for_del(
            Group(surname="SURNAME", name="Тест-ред", secondname="Тест-редотчество", birthday="17111983",
                  phone="79051591232",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SURNAME")
    app.group.edit_patient_birthday(Group(birthday="21.12.1999"), text="21.12.1999")

