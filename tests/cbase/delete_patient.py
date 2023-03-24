# -*- coding: utf-8 -*-

def test_del_patient_in_cbase(app):
    app.cbase.delete_new_patient(search_name="ADD-VIP")
    app.cbase.delete_new_patient(search_name="BLACKLIST")
    app.cbase.delete_new_patient(search_name="CLIENT")
    app.cbase.delete_new_patient(search_name="INSURANCE")
    app.cbase.delete_new_patient(search_name="MARK-TEST")
    app.cbase.delete_new_patient(search_name="NOTE")
    app.cbase.delete_new_patient(search_name="PHOTO")
    app.cbase.delete_new_patient(search_name="PLUGIN-OFF")
    app.cbase.delete_new_patient(search_name="PLUGIN-ON")
    app.cbase.delete_new_patient(search_name="VIP-LIST")
    app.cbase.delete_new_patient(search_name="WITH-ONE")




