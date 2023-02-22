import allure

from model.group import Group
from model.group import Chair


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Создание и настройка кресла")
def test_add_chair(app):
    if app.settings.chair_availability(Chair(title="test-chair")) == 0:
        app.settings.add_chair(Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
    app.settings.check_chair(Chair(title="test-chair"))


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Удаление кресла")
@allure.description("Сначала сгенерировать тестовые данные, добавить в настройки системы кресло")
def test_delete_chair(app):
    app.settings.open_employees_chair()
    app.settings.add_chair(Chair(title="del-chair", sorting="10", department="Терапевты", filial="Филиал 1"))
    app.settings.delete_chair(Chair(title="del-chair"))


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Ручное добавление пользователя")
def test_manual_add_user(app):
    if app.settings.user_availability(Group(login="new-user-test")) == 0:
        app.settings.add_user()
        app.settings.fill_new_user_form(Group(surname="Surname", name="Name", secondname="Secondname",
                                              login="new-user-test", mail="newmail@mail.ru",
                                              phone="79041871637", user_group="Врач"))


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Удаление пользователя")
@allure.description("Сначала сгенерировать тестовые данные, добавить в пользователя в систему")
def test_delete_user(app):
    if app.settings.user_availability(Group(login="del-user-test")) == 0:
        app.settings.add_user()
        app.settings.fill_new_user_form(Group(surname="Surname", name="Name", secondname="Secondname",
                                              login='del-user-test', mail='delete@mail.ru', phone='79041871379'))
    app.settings.delete_user(Group(login='del-user-test'))


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Добавление пользователя в список врачей")
def test_add_doctor(app):
    if app.settings.doctor_availability(Group(surname="Surname")) == 0:
        app.settings.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                         login='new-user-test', mail='newmail@mail.ru', phone='79041871637'))
    app.settings.open_employees_doctor()
    app.settings.add_doctor(Group(surname="Surname", department="Терапевты"))
    # app.settings.add_department(department="Терапевты")


@allure.epic("Настройка системы")
@allure.tag("Предварительная настройка")
@allure.title("Удалить пользователя из списка врачей")
def test_delete_doc(app):
    if app.settings.doctor_availability(Group(surname="Удалить")) == 0:
        app.settings.add_user_step(Group(surname="Удалить", name="Name", secondname="Secondname",
                                         login='delusertest', mail='delmail@mail.ru', phone='79041871472'))
        app.settings.open_employees_doctor()
        app.settings.add_doctor(Group(surname="Удалить", department="Терапевты"))
        # app.settings.add_department(department="Терапевты")
    app.settings.delete_doctor(Group(surname="Удалить"))


@allure.epic("Настройка системы")
@allure.tag("Настройка расписания")
@allure.title("Настройка графика работы врача на день")
@allure.description("Перед началом, проверить тестовые данные, при необходимости сгенерировать их")
def test_add_doc_schedule(app):
    if app.settings.schedule_availability(Group(surname="Surname")) == 0:
        if app.settings.chair_availability(Chair(title="test-chair")) == 0:
            app.settings.add_chair(Chair(title="test-chair", sorting="9", department="Терапевты", filial="Филиал 1"))
        if app.settings.doctor_availability(Group(surname="Surname")) == 0:
            app.settings.add_user_step(Group(surname="Surname", name="Name", secondname="Secondname",
                                             login='new-user-test', mail='newmail@mail.ru',
                                             phone='79041871637', user_group="Врач"))
            app.settings.open_employees_doctor()
            # app.settings.add_doctor(Group(login="new-user-test"))
            app.settings.add_doctor(Group(surname="Surname", department="Терапевты"))
            # app.settings.add_department(department="Терапевты")
    # app.settings.schedule_availability(Group(surname="Surname"))
    app.settings.open_schedule_set()
    app.settings.check_doc_schedule(Group(surname="Surname"))


@allure.description("Добавить врачу расписание на сегодняшний день")
def test_fill_doc_schedule_day(app):
    app.settings.add_schedule_step()
    # app.settings.schedule_availability(Group(surname="Surname"))
    app.settings.fill_doc_schedule(Group(surname="Surname"))
    app.settings.fill_date_picker()
    app.settings.fill_chair_selection(Chair(title="test-chair"))
    app.settings.default_interval_selection(Group(s_time="13:00"))
    app.settings.default_schedule_correction()
    app.settings.schedule_confirm()


@allure.description("Добавить врачу расписание на завтра")
def test_fill_doc_schedule_tomorrow(app):
    app.settings.add_schedule_step()
    app.settings.fill_doc_schedule_tomorrow(Group(surname="Surname"))
    app.settings.fill_date_picker_tomorrow()
    app.settings.fill_chair_selection(Chair(title="test-chair"))
    app.settings.default_interval_selection(Group(s_time="16:00"))
    app.settings.default_schedule_correction()
    app.settings.schedule_confirm()


@allure.description("Удалить расписание врача на завтра")
def test_delete_schedule_tomorrow(app):
    app.settings.add_schedule_step()
    if app.settings.day_graph_availability(Group(surname="Surname")) == 0:
        app.settings.fill_doc_schedule_tomorrow(Group(surname="Surname"))
        app.settings.fill_date_picker_tomorrow()
        app.settings.fill_graph_day_form(Chair(title="test-chair"))
    app.settings.delete_day_doc_schedule(Group(surname="Surname"))


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
