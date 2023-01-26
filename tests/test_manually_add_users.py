
from model.group import Group
from model.group import Chair


def test_add_chair(app):
    if app.settings.chair_availability(Chair(title="test-chair")) == 0:
        # app.settings.open_employees_chair()
        app.settings.add_chair(Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
    app.settings.check_chair(Chair(title="test-chair"))


def test_delete_chair(app):
    app.settings.open_employees_chair()
    old_list = app.settings.get_chair_list()
    app.settings.add_chair(Chair(title="del-chair", sorting="10", department="Терапевты", filial="Филиал 1"))
    app.settings.delete_chair(Chair(title="del-chair"))
    new_list = app.settings.get_chair_list()
    assert len(old_list) == len(new_list) - 1


def test_manual_add_user(app):
    if app.settings.user_availability(Group(login="new-user-test")) == 0:
        app.settings.add_user()
        app.settings.fill_new_user_form(Group(surname="Surname", name="Name", secondname="Secondname",
                                              login="new-user-test", mail="newmail@mail.ru", phone="79041871637"))


def test_delete_user(app):
    if app.settings.user_availability(Group(login="del-user-test")) == 0:
        app.settings.add_user()
        app.settings.fill_new_user_form(Group(surname="Surname", name="Name", secondname="Secondname",
                                              login='del-user-test', mail='delete@mail.ru', phone='79041871379'))
    app.settings.delete_user(Group(login='del-user-test'))


def test_add_doctor(app):
    if app.settings.doctor_availability(Group(surname="Surname")) == 0:
        app.settings.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                         login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))
    app.settings.open_employees_doctor()
    app.settings.add_doctor(Group(surname="Surname"))
    app.settings.add_department(department="Терапевты")
    # app.settings.add_department(department="Хирурги")


def test_delete_doc(app):
    if app.settings.doctor_availability(Group(surname="Удалить")) == 0:
        app.settings.add_user_step(Group(surname="Удалить", name="Name", secondname="Secondname",
                                         login='delusertest', mail='delmail@mail.ru', phone='79041871472'))
        app.settings.open_employees_doctor()
        app.settings.add_doctor(Group(surname="Удалить"))
        app.settings.add_department(department="Терапевты")
    app.settings.delete_doctor(Group(surname="Удалить"))


def test_add_doc_schedule(app):
    if app.settings.schedule_availability(Group(surname="Surname")) == 0:
        if app.settings.chair_availability(Chair(title="test-chair")) == 0:
            app.settings.add_chair(Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
        if app.settings.doctor_availability(Group(surname="Surname")) == 0:
            app.settings.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                             login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))
            app.settings.open_employees_doctor()
            # app.settings.add_doctor(Group(login="new-user-test"))
            app.settings.add_doctor(Group(surname="Surname"))
            app.settings.add_department(department="Терапевты")
    app.settings.schedule_availability(Group(surname="Surname"))
    app.settings.check_doc_schedule(Group(surname="Surname"))


def test_fill_doc_schedule_day(app):
    app.settings.add_schedule_step()
    # app.settings.schedule_availability(Group(surname="Surname"))
    app.settings.fill_doc_schedule(Group(surname="Surname"))
    app.settings.fill_date_picker()
    app.settings.fill_chair_selection(Chair(title="test-chair"))
    app.settings.default_interval_selection(Group(s_time="13:00"))
    app.settings.default_schedule_correction()
    app.settings.schedule_confirm()


def test_fill_doc_schedule_tomorrow(app):
    app.settings.add_schedule_step()
    app.settings.fill_doc_schedule_tomorrow(Group(surname="Surname"))
    app.settings.fill_date_picker_tomorrow()
    app.settings.fill_chair_selection(Chair(title="test-chair"))
    app.settings.default_interval_selection(Group(s_time="16:00"))
    app.settings.default_schedule_correction()
    app.settings.schedule_confirm()


def test_delete_schedule_tomorrow(app):
    app.settings.add_schedule_step()
    if app.settings.day_graph_availability(Group(surname="Surname")) == 0:
        app.settings.fill_doc_schedule_tomorrow(Group(surname="Surname"))
        app.settings.fill_date_picker_tomorrow()
        app.settings.fill_graph_day_form(Chair(title="test-chair"))
    app.settings.delete_day_doc_schedule(Group(surname="Surname"))


def test_open_record_form(app):
    app.settings.fill_second_schedule()
    app.schedule.open_schedule()
    app.schedule.open_record_form()
    app.schedule.open_new_patient_form()
    app.schedule.fill_new_patient_form()
    app.schedule.fill_new_patient_record()
