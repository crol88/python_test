from model.group import Group
import allure


@allure.description("Запись нового пациента через расписание")
def test_open_record_form(app):
    app.settings.schedule_availability(Group(surname="Second"))
    if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
        app.settings.fill_second_schedule()
    app.schedule.open_schedule()
    app.schedule.open_new_record_form(timehelper="25")
    app.schedule.open_new_patient_form()
    app.schedule.fill_new_patient_form(Group(surname="Schedule"))
    app.schedule.fill_new_patient_record()


@allure.description("Выбор существующего пациента при создании приема")
def test_select_patient(app):
    if app.cbase.count("REACTSELECT") == 0:
        app.cbase.add_patient_for(
            Group(surname="Reactselect", name="Name", secondname="Patient", birthday="13101999",
                  phone="79058121458", fromwhere="2ГИС"))
    app.settings.schedule_availability(Group(surname="Second"))
    if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
        app.settings.fill_second_schedule()
    app.schedule.open_schedule()
    app.schedule.open_new_record_form(timehelper="20")
    app.schedule.select_patient(Group(surname="Reactselect"))
    app.schedule.fill_new_patient_record()


@allure.description("Отложенная запись через запись в расписании")
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


@allure.description("Навигация записи в расписании")
def test_task_panel_navigation(app):
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
    app.schedule.task_panel_navigation(locator="SCHEDULE")


@allure.description("Открыть информацию о пациенте через запись в расписании")
def test_task_panel_patient_information(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_patient_information(locator="SCHEDULE")


@allure.description("Открыть амбулаторную карту через запись в расписании")
def test_task_panel_paticard(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_paticard(locator="SCHEDULE")


@allure.description("Отметить результат посещения через расписание")
def test_task_panel_visit_result(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.mark_visit_result(locator="SCHEDULE")


@allure.description("Форма удаления записи в расписании")
def test_task_panel_delete_record(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_delete_record(locator="SCHEDULE")


@allure.description("Открыть форму отправки СМС через расписание")
def test_task_panel_send_sms(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_send_sms(locator="SCHEDULE")


@allure.description("Открыть форму копирования записи в расписании")
def test_task_panel_copy_record(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_copy_form(locator="SCHEDULE")


@allure.description("Открыть план лечения через запись в расписании")
def test_task_panel_medblock(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_open_medblock(locator="SCHEDULE")


@allure.description("Открыть форму пациент пришел")
def test_task_panel_patient_came(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_patient_came(locator="SCHEDULE")


@allure.description("Перенести запись в расписании")
def test_task_panel_move_record(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_move_record(locator="SCHEDULE")


@allure.description("Запланировать посещение через запись в расписании")
def test_task_panel_plan_visit(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.tp_plan_visit(locator="SCHEDULE")


@allure.description("Переход в кассу через запись в расписании")
def test_task_panel_pay(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
        app.schedule.schedule_new_patient()
        app.schedule.fill_new_patient_form(Group(surname="Schedule"))
        app.schedule.fill_new_patient_record()
    app.schedule.pay(locator="SCHEDULE")


@allure.description("Изменение расписания через режим редактирования")
def test_edit_schedule(app):
    app.schedule.open_schedule()
    if app.schedule.check_task_dnd(locator="EDIT-SCHED") == 0:
        app.settings.schedule_availability(Group(surname="Suredit"))
        if app.schedule.check_fill_schedule(Group(surname="Suredit")) == 0:
            app.settings.fill_edit_schedule()
        app.schedule.open_schedule()
    app.schedule.edit_mode()


@allure.description("Служебная запись в расписании")
def test_schedule_service_record(app):
    app.schedule.open_schedule()
    surname = "Second"
    if app.schedule.check_schedule_test_data(surname) == 0:
        app.settings.schedule_availability(Group(surname="Second"))
        if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
            app.settings.fill_second_schedule()
    app.schedule.open_service_record_form(surname, t_start="16:00", t_end="17:00")


def test_schedule_tp_dnd(app):
    app.schedule.open_schedule()
    if app.schedule.check_schedule_test_data(surname="Second") == 0:
        if app.schedule.check_task_dnd(locator="SCHEDULE") == 0:
            app.settings.schedule_availability(Group(surname="Second"))
            if app.schedule.check_fill_schedule(Group(surname="Second")) == 0:
                app.settings.fill_second_schedule()
    app.schedule.open_schedule()
    if app.schedule.check_schedule_test_data(surname="Suredit") == 0:
        if app.schedule.check_task_dnd(locator="EDIT-SCHED") == 0:
            app.settings.schedule_availability(Group(surname="Suredit"))
            if app.schedule.check_fill_schedule(Group(surname="Suredit")) == 0:
                app.settings.fill_edit_schedule()
    app.schedule.open_schedule()
    # app.schedule.open_service_record_form(surname="Suredit", t_start="17:00", t_end="18:00")
    app.schedule.tp_dnd()
