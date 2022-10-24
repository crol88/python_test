# -*- coding: utf-8 -*-

def test_del_patient_in_cbase(app):
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="АТЕСТ")
    app.cbase.delete_new_patient(search_name="УТЕСТ")
    app.cbase.delete_new_patient(search_name="УТЕСТ")
    app.cbase.delete_new_patient(search_name="УТЕСТ")
    app.cbase.delete_new_patient(search_name="УТЕСТ")
    app.cbase.delete_new_patient(search_name="тест")
    app.cbase.delete_new_patient(search_name="тест")
    app.cbase.delete_new_patient(search_name="тест")




