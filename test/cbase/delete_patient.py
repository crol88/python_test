

def test_del_patient_in_cbase(app):
    app.cbase.delete_new_patient(search_name="SURNAME-EDIT")
    app.cbase.delete_new_patient(search_name="SURNAME-EDIT")
    app.cbase.delete_new_patient(search_name="SURNAME-EDIT")
    app.cbase.delete_new_patient(search_name="SURNAME-EDIT")
    app.cbase.delete_new_patient(search_name="SURNAME-EDIT")
    app.cbase.delete_new_patient(search_name="ТЕСТ")
    app.cbase.delete_new_patient(search_name="ТЕСТ")
    app.cbase.delete_new_patient(search_name="ТЕСТ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    app.cbase.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")




