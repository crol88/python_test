from model.group import Group
from model.group import Chair


def test_fill_doc_schedule_day(app):
    app.settings.add_schedule_step()
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
    app.settings.default_interval_selection(Group(s_time="12:00"))
    app.settings.default_schedule_correction()
    app.settings.schedule_confirm()


def test(app):
    app.settings.add_schedule_step()
    if app.settings.day_graph_availability(Group(surname="Surname")) == 0:
        app.settings.fill_doc_schedule_tomorrow(Group(surname="Surname"))
        app.settings.fill_date_picker_tomorrow()
        app.settings.fill_graph_day_form(Chair(title="test-chair"))
    app.settings.delete_day_doc_schedule(Group(surname="Surname"))