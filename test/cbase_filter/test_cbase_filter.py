# from model.group import Group
#
#
# def test_open_cbase_filter(app):
#     app.cbase.open_cbase()
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.check_filter_status()
#
#
# def test_filter_by_surname(app):
#     app.cbase.open_cbase()
#     if app.cbase.count("TEST-FIL") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="TEST-FIL", name="name", secondname="secondname", birthday="17071977",
#                   phone="79058175315", fromwhere="2ГИС"))
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.fill_surname_filter(surname="TEST-FIL")


# def test_filter_by_name(app):
#     app.cbase.open_cbase()
#     if app.cbase.count("TEST-FIL-NAME") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="surname", name="TEST-FIL-NAME", secondname="secondname", birthday="17071977",
#                   phone="79058176258", fromwhere="2ГИС"))
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.fill_name_filter(name="TEST-FIL-NAME")
#
#
# def test_filter_by_secondname(app):
#     app.cbase.open_cbase()
#     if app.cbase.count("TEST-SECFIL") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="surname", name="name", secondname="TEST-SECFIL", birthday="17071977",
#                   phone="79058143749", fromwhere="2ГИС"))
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.fill_secondname_filter(secondname="TEST-SECFIL")
#
#
# def test_filter_by_birthday(app):
#     app.cbase.open_cbase()
#     if app.cbase.count("TEST-DATE") == 0:
#         app.cbase.add_patient_for(
#             Group(surname="TEST-DATE", name="name", secondname="secondname", birthday="17071977",
#                   phone="79058143656", fromwhere="2ГИС"))
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.fill_birthday_filter(birthday="17.07.1977")
#
#
# def test_filter_by_sex_male(app):
#     app.cbase.open_cbase()
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.add_sex_filter()
#     app.cbase_filter.select_sex_filter(sex="Мужской")
#     app.cbase_filter.get_sex_filter_result_male()
#
#
# def test_filter_by_sex_female(app):
#     app.cbase.open_cbase()
#     app.cbase_filter.open_cbase_filter()
#     app.cbase_filter.add_sex_filter()
#     app.cbase_filter.select_sex_filter(sex="Женский")
#     app.cbase_filter.get_sex_filter_result_female()

