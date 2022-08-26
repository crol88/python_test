from model.group import Group


def test_add_and_delete_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.change_filial(filial="Филиал 1")
    app.group.fill_newclient_form(Group(surname="Атест", name="Добавить", secondname="Удалить",
                                        datapicker="12081980", phone="79058889556", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient()
    app.session.logout()
