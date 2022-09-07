from model.group import Group


def test_edit_patient_name(app):
    app.group.search_patient(search_name="Абелин")
    app.group.edit_patient_data(Group(name="АТест-ред-имя"))


def test_edit_patient_surname(app):
    old_groups = app.group.get_group_list()
    group = (Group(surname="АТест-Ред-Фамилия"))
    group.cbaseid = old_groups[0].cbaseid
    app.group.search_patient(search_name="Проверка")
    app.group.edit_patient_data(Group(group))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_patient_secondname(app):
    app.group.search_patient(search_name="ТЕСТ-АБАРШЕВ")
    app.group.edit_patient_data(Group(secondname="Ред-Два"))


def test_edit_patient_secondname_2(app):
    app.group.search_patient(search_name="ТЕСТ-АБАРШЕВ")
    app.group.edit_patient_data(Group(secondname="ТЕСТРЕД-Проверка"))


def test_edit_basic_patient_info(app):
    basic_patient_info = app.group.get_basic_patient_info()
    edit_basic_patient_info = app.group.get_basic_patient_info_after_edit()
    assert basic_patient_info.surname == edit_basic_patient_info.surname
    assert basic_patient_info.name == edit_basic_patient_info.name
    assert basic_patient_info.secondname == edit_basic_patient_info.secondname
    assert basic_patient_info.datapicker == edit_basic_patient_info.datapicker

