from model.group import Group
from model.group import Chair
import allure


def test_set_interval_schedule(app):
    app.settings.gen_interval_data()
    # app.settings.fill_doc_schedule(Group(surname="Interval"))


def test_add_work_shift(app):
    app.settings.open_work_shift_setting()
    app.settings.add_work_shift_template(name="Рабочая неделя 5/2", start="09:00", end="18:00")


def test_gen_plan(app):
    app.settings.gen_treatment_plan_data()
    app.settings.gen_treatment_plan_schedule()
