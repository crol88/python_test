from model.group import Group


def test_upload_patient_photo(app):
    if app.cbase.count("PHOTO") == 0:
        app.cbase.add_patient_for(
            Group(surname="PHOTO", name="ADD", secondname="TEST", birthday="12111991", phone="79058887546",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="PHOTO")
    app.infocard_mainpage.upload_photo()


def test_delete_upload_patient_photo(app):
    if app.cbase.count("PHOTO") == 0:
        app.cbase.add_patient_for(
            Group(surname="PHOTO", name="ADD", secondname="TEST", birthday="12111991", phone="79058887546",
                  fromwhere="2ГИС"))
        app.cbase.search_patient(search_name="PHOTO")
        app.infocard_mainpage.upload_photo()
    app.cbase.search_patient(search_name="PHOTO")
    app.infocard_mainpage.delete_photo()


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


def test_add_insurance_mark(app):
    if app.cbase.count("INSURANCE") == 0:
        app.cbase.add_patient_for(
            Group(surname="INSURANCE", name="MARK", secondname="TEST", birthday="22031997", phone="79051768556",
                  fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="INSURANCE")
    app.basic_info.add_mark(mark="Страховой")


def test_add_blacklist_mark(app):
    if app.cbase.count("BLACKLIST") == 0:
        app.cbase.add_patient_for(
            Group(surname="BLACKLIST", name="MARK", secondname="TEST", birthday="13031993", phone="79051766656",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="BLACKLIST")
    app.basic_info.add_mark(mark="Черный список")


def test_delete_mark_vip_new(app):
    if app.cbase.count("MARK-TEST") == 0:
        app.cbase.add_patient_for(
            Group(surname="MARK-TEST", name="MARK", secondname="TEST", birthday="13031993", phone="79051766656",
                  fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="MARK-TEST")
    app.basic_info.delete_some_mark(mark="vip")


def test_delete_mark_blacklist_new(app):
    if app.cbase.count("MARK-TEST") == 0:
        app.cbase.add_patient_for(
            Group(surname="MARK-TEST", name="MARK", secondname="TEST", birthday="13031993", phone="79051766656",
                  fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="MARK-TEST")
    app.basic_info.delete_some_mark(mark="blacklist")


def test_delete_mark_insurance_new(app):
    if app.cbase.count("MARK-TEST") == 0:
        app.cbase.add_patient_for(
            Group(surname="MARK-TEST", name="MARK", secondname="TEST", birthday="13031993", phone="79051766656",
                  fromwhere="2ГИС"))
    app.cbase.search_patient(search_name="MARK-TEST")
    app.basic_info.delete_some_mark(mark="insurance")


# def test_delete_vip_mark(app):
#     if app.cbase.count("VIP-LIST") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="VIP-LIST", name="name", secondname="secondname", birthday="19041987", phone="79051278556",
#                   fromwhere="2ГИС", filial=""))
#     app.cbase.search_patient(search_name="VIP-LIST")
#     if app.infocard_mainpage.mark(mark="VIP", check_mark="VIP") == 0:
#         app.basic_info.add_mark(mark="VIP")
#     app.infocard_mainpage.delete_vip_mark(status="VIP")
#
#
# def test_delete_insurance_mark(app):
#     if app.cbase.count("INSURANCE") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="INSURANCE", name="MARK", secondname="TEST", birthday="22031997", phone="79051768556",
#                   fromwhere="2ГИС", filial=""))
#     app.cbase.search_patient(search_name="INSURANCE")
#     if app.infocard_mainpage.mark(mark="Страховой", check_mark="Страховой") == 0:
#         app.basic_info.add_mark(mark="Страховой")
#     app.infocard_mainpage.delete_mark(mark="Страховой", status="Страховой")
#
#
# def test_delete_blacklist_mark(app):
#     if app.cbase.count("BLACKLIST") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="BLACKLIST", name="MARK", secondname="TEST", birthday="13031993", phone="79051766656",
#                   fromwhere="2ГИС", filial=""))
#     app.cbase.search_patient(search_name="BLACKLIST")
#     if app.infocard_mainpage.mark(mark="Черный список", check_mark="Черный список") == 0:
#         app.basic_info.add_mark(mark="Черный список")
#     app.infocard_mainpage.delete_mark(mark="Черный список", status="Черный список")


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
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="WITH-ONE FILIAL ONE")
    app.infocard_mainpage.check_filial(enter_filial="Филиал 1")


def test_add_note(app):
    if app.cbase.count("NOTE") == 0:
        app.cbase.add_patient_for(
            Group(surname="NOTE", name="ADD", secondname="TEST", birthday="19111994", phone="79051139796",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="NOTE ADD TEST")
    app.infocard_mainpage.add_note(enter_text="test add note")


def test_choice_coordinator(app):
    if app.cbase.count("ADD-VIP") == 0:
        app.cbase.add_patient_for(
            Group(surname="ADD-VIP", name="name", secondname="secondname", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ADD-VIP")
    app.infocard_mainpage.choice_coordinator(filial="Филиал 1", manager="Координатор: Супер Пользователь С.С.")


def test_choice_doctor(app):
    if app.cbase.count("ADD-VIP") == 0:
        app.cbase.add_patient_for(
            Group(surname="ADD-VIP", name="name", secondname="secondname", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ADD-VIP")
    app.infocard_mainpage.select_doctor()


def test_add_personal_discount(app):
    if app.cbase.count("ADD-VIP") == 0:
        app.cbase.add_patient_for(
            Group(surname="ADD-VIP", name="name", secondname="secondname", birthday="12081980", phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ADD-VIP")
    app.infocard_mainpage.personal_discount()
