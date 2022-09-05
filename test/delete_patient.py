from model.group import Group


def test_del_patient_in_cbase(app):
    app.group.delete_new_patient(search_name="Проверка")
    app.group.delete_new_patient(search_name="Проверка")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")
    app.group.delete_new_patient(search_name="Тест")

