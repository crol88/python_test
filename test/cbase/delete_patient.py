

def test_del_patient_in_cbase(app):
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="ТЕСТ")
    app.group.delete_new_patient(search_name="ТЕСТ")
    app.group.delete_new_patient(search_name="ТЕСТ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")




