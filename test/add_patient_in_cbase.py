from model.group import Group


def test_add_new_patient(app):
    app.group.change_filial(Group(filial="Филиал 1"))
    app.group.fill_newclient_form(Group(surname="Петров-Тест", name="Пётр", secondname="Петрович",
                                        datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Иванов-Тест", name="Иван", secondname="Иванович",
                                        datapicker="05061998", phone="79278815766", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Сидоров-Тест", name="Сидр", secondname="Сидорович",
                                        datapicker="02102005", phone="79273145866", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Кузнецов-Тест", name="Кузнец", secondname="Кузнецович",
                                        datapicker="12111990", phone="79278881237", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абаршев-Тест", name="Имя", secondname="Отчество",
                                        datapicker="10102010", phone="79271235966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абарыков-Тест", name="Имя", secondname="Отчество",
                                        datapicker="03082002", phone="79277853966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абахин-Тест", name="Имя", secondname="Отчество",
                                        datapicker="25081999", phone="79279644966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абдуллин-Тест", name="Имя", secondname="Отчество",
                                        datapicker="14051995", phone="79271453966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абелин-Тест", name="Имя", secondname="Отчество",
                                        datapicker="16051998", phone="79277563668", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абелин-Тест", name="Имя", secondname="Отчество",
                                        datapicker="16051998", phone="79277563668", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.push_button_newClient()
    app.group.fill_newclient_form(Group(surname="Абелин-Тест", name="Имя", secondname="Отчество",
                                        datapicker="16051998", phone="79277563668", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
