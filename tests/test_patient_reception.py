from model.group import Group
import allure


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Добавить черновик приема")
def test_add_appointment_draft(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    app.tplan.select_optimal_tplan(area="Шейка зуба",
                                   problem="Зубные отложения",
                                   variants="Снятие зубных отложений/ Профессиональная гигиена",
                                   var_next="Профессиональная гигиена Norma",
                                   doctor="Гигиенистова2 Анна Андреевна")


def test_approve_appointment(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts() == 0:
        app.tplan.select_optimal_tplan(area="Шейка зуба",
                                       problem="Зубные отложения",
                                       variants="Снятие зубных отложений/ Профессиональная гигиена",
                                       var_next="Профессиональная гигиена Norma",
                                       doctor="Гигиенистова2 Анна Андреевна")