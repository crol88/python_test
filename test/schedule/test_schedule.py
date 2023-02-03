

def test_open_schedule(app):
    app.schedule.open_schedule()


def test_date_check(app):
    app.schedule.open_schedule()
    app.schedule.check_schedule_date()


def test_select_doctor_schedule(app):
    app.schedule.open_schedule()
    app.cbase.select_all_filial(filial="Все филиалы")
    app.schedule.select_doctor_schedule()


def test_select_multiple_doctors(app):
    app.schedule.open_schedule()
    app.cbase.select_all_filial(filial="Все филиалы")
    app.schedule.select_multiple_doctors()


def test_check_departments(app):
    app.schedule.open_schedule()
    app.cbase.select_all_filial(filial="Все филиалы")
    app.schedule.check_all_departments()


def test_check_doctor_department(app):
    app.schedule.open_schedule()
    app.cbase.select_all_filial(filial="Все филиалы")
    app.schedule.select_random_department()


def test_new_patient_record(app):
    app.schedule.open_schedule()
    app.cbase.select_all_filial(filial="Все филиалы")
    app.schedule.new_patient_record()
