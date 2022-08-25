
def test_delete_patient(app):
    app.session.login(username="Директор1", password="123456")
    app.group.fill_newclient_form(Group(surname="Тест", name="Добавить-Удалить", secondname="Пациента",
                                  datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
    app.group.submit_newpatient_creation()
    app.group.delete_new_patient()