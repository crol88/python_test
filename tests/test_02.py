from model.group import Group
from model.group import Chair


def test_open_record_form(app):
    app.settings.schedule_availability(Group(surname="Second"))
    if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
        app.settings.fill_second_schedule()
    app.schedule.open_schedule()
    app.schedule.open_record_form()
    app.schedule.open_new_patient_form()
    app.schedule.fill_new_patient_form(Group(surname="Schedule"))
    app.schedule.fill_new_patient_record()


def test_schedule_hold_record(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.open_schedule()
        app.schedule.open_record_form()
        app.schedule.open_new_patient_form()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.hold_record(locator="SCHEDULE")
