from model.group import Group


def test_add_new_patient(app):
    old_groups = app.group.get_group_list()
    app.group.change_filial(Group(filial="Филиал 1"))
    app.group.fill_newclient_form(Group(surname="Тест-Петров", name="Пётр", secondname="Петрович",
                                        datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Иванов", name="Иван", secondname="Иванович",
                                        datapicker="05061998", phone="79278815766", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Сидоров", name="Сидр", secondname="Сидорович",
                                        datapicker="02102005", phone="79273145866", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Кузнецов", name="Кузнец", secondname="Кузнецович",
                                        datapicker="12111990", phone="79278881237", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абаршев", name="Абар", secondname="Султанович",
                                        datapicker="10102010", phone="79271235966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абарыков", name="Тимур", secondname="Дмитриевич",
                                        datapicker="03082002", phone="79277853966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абахин", name="Михаил", secondname="Иванович",
                                        datapicker="25081999", phone="79279644966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абдуллин", name="Абдула", secondname="Владимирович",
                                        datapicker="14051995", phone="79271453966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абелин", name="Олег", secondname="Олегович",
                                        datapicker="16051998", phone="79277563668", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Тест-Абелин", name="Владислав", secondname="Владимирович",
                                        datapicker="16051998", phone="79277563668", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 10 == len(new_groups)
