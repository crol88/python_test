
from model.group import Group


def test_add_vip_patient(app):
    if app.cbase.count("ADD-VIP") == 0:
        app.cbase.add_patient_for(
            Group(surname="ADD-VIP", name="name", secondname="secondname", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ADD-VIP")
    app.basic_info.add_mark(mark="VIP")
    app.infocard_mainpage.open_cbase_vip_no_manager()
    app.infocard_mainpage.check_cbase_vip(vip_client="ADD-VIP")


def test_vip_list(app):
    if app.cbase.count("VIP-LIST") == 0:
        app.cbase.add_patient_for(
            Group(surname="VIP-LIST", name="name", secondname="secondname", birthday="19041987", phone="79051278556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="VIP-LIST")
    app.basic_info.add_mark(mark="VIP")
    app.infocard_mainpage.open_cbase_vip_list()
    app.infocard_mainpage.check_cbase_vip_list(vip_client="VIP-LIST NAME SECONDNAME")


def test_add_client_without_filial(app):
    if app.cbase.count("WITHOUT") == 0:
        app.cbase.add_patient_for(
            Group(surname="CLIENT", name="WITHOUT", secondname="FILIAL", birthday="22041989", phone="79051271596",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="CLIENT WITHOUT FILIAL")
    app.infocard_mainpage.check_without_filial()


def test_add_with_filial(app):
    if app.cbase.count("WITH-ONE") == 0:
        app.cbase.add_patient_for(
            Group(surname="WITH-ONE", name="FILIAL", secondname="ONE", birthday="18111996", phone="79051138596",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.cbase.search_patient(search_name="WITH-ONE FILIAL ONE")
    app.infocard_mainpage.check_filial(enter_filial="Филиал 1")


def test_add_note(app):
    if app.cbase.count("NOTE") == 0:
        app.cbase.add_patient_for(
            Group(surname="NOTE", name="ADD", secondname="TEST", birthday="19111994", phone="79051139796",
                  fromwhere="2ГИС", filial="Филиал 1"))
    app.cbase.search_patient(search_name="NOTE ADD TEST")
    app.infocard_mainpage.add_note(enter_text="test add note")
