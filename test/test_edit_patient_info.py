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
            Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SURNAME")
    app.group.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")


def test_edit_patient_surname_without_changes(app):
    # Активировать поле фамилия и сохранить без изменений
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


def test_edit_patient_name_without_changes(app):
    app.group.search_patient(search_name="SURNAME-EDIT")
    app.group.edit_patient_name_fill(text="NAME-EDIT")


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


def test_edit_patient_sex_male(app):
    if app.group.count(check_patient="SEX-MALE") == 0:
        app.group.add_patient_for_del(
            Group(surname="SEX-MALE", name="ПОЛ", secondname="МУЖСКОЙ", birthday="21101984",
                  phone="79051593692",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SEX-MALE")
    app.group.edit_patient_sex(sex="Мужской")


def test_edit_patient_sex_female(app):
    if app.group.count(check_patient="SEX-FEMALE") == 0:
        app.group.add_patient_for_del(
            Group(surname="SEX-FEMALE", name="ПОЛ", secondname="МУЖСКОЙ", birthday="23101985",
                  phone="79051158692",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.group.search_patient(search_name="SEX-FEMALE")
    app.group.edit_patient_sex(sex="Женский")


def test_edit_patient_inn(app):
    app.group.search_patient(search_name="SURNAME")
    app.group.edit_patient_inn()
