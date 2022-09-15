from model.group import Group


def test_del_patient_in_cbase(app):
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    app.group.delete_new_patient(search_name="SURNAME-EDIT")
    # app.group.delete_new_patient(search_name="ТЕСТ")
    # app.group.delete_new_patient(search_name="ТЕСТ")
    # app.group.delete_new_patient(search_name="ТЕСТ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")
    # app.group.delete_new_patient(search_name="АААТЕСТ-РЕДИМЯ")

# def test_edit_patient_postcode(app):
#     app.group.search_patient(search_name="SURNAME")
#     app.group.edit_patient_postcode(postcode="432001")
#
#
# def test_edit_patient_last_data(app):
#     app.group.search_patient(search_name="SURNAME")
#     app.group.edit_patient_last_data(data="10.10.2022")


