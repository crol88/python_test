from model.group import Group
import allure


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Добавить черновик приема")
def test_canban_draft(app):
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


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Удалить прием из черновика")
def test_delete_canban_draft(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts(service="Профессиональная гигиена: дентикюр Norma") == 0:
        app.tplan.select_optimal_tplan(area="Шейка зуба",
                                       problem="Зубные отложения",
                                       variants="Снятие зубных отложений/ Профессиональная гигиена",
                                       var_next="Профессиональная гигиена Norma",
                                       doctor="Гигиенистова2 Анна Андреевна")
    app.tplan.delete_canban_draft()


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Утвердить прием из черновика")
def test_canban_approve(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts(service="Профессиональная гигиена: дентикюр Norma") == 0:
        app.tplan.select_optimal_tplan(area="Шейка зуба",
                                       problem="Зубные отложения",
                                       variants="Снятие зубных отложений/ Профессиональная гигиена",
                                       var_next="Профессиональная гигиена Norma",
                                       doctor="Гигиенистова2 Анна Андреевна")
    app.tplan.canban_approved(service="Профессиональная гигиена: дентикюр Norma")


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Удалить утвержденный прием")
def test_delete_canban_approve(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts(service="Профессиональная гигиена: дентикюр Norma") == 0:
        if app.tplan.check_approved(service="Профессиональная гигиена: дентикюр Norma") == 0:
            app.tplan.select_optimal_tplan(area="Шейка зуба",
                                           problem="Зубные отложения",
                                           variants="Снятие зубных отложений/ Профессиональная гигиена",
                                           var_next="Профессиональная гигиена Norma",
                                           doctor="Гигиенистова2 Анна Андреевна")
            app.tplan.canban_approved(service="Профессиональная гигиена: дентикюр Norma")
    app.tplan.delete_canban_approve()


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Согласовать план лечения")
def test_approve_tplan(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts(service="Профессиональная гигиена: дентикюр Norma") == 0:
        if app.tplan.check_approved(service="Профессиональная гигиена: дентикюр Norma") == 0:
            app.tplan.select_optimal_tplan(area="Шейка зуба",
                                           problem="Зубные отложения",
                                           variants="Снятие зубных отложений/ Профессиональная гигиена",
                                           var_next="Профессиональная гигиена Norma",
                                           doctor="Гигиенистова2 Анна Андреевна")
            app.tplan.canban_approved(service="Профессиональная гигиена: дентикюр Norma")
    app.tplan.approve_tplan()


@allure.epic("Работа с приемом пациента")
@allure.tag("План лечения")
@allure.title("Отменить согласование")
def test_cancel_approval(app):
    if app.cbase.count("ПЛАН-ЛЕЧЕНИЯ") == 0:
        app.cbase.add_patient_for(
            Group(surname="План-лечения", name="Тест", secondname="Тест", birthday="14082002",
                  phone="79058881557",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="ПЛАН-ЛЕЧЕНИЯ")
    app.tplan.open_treatment_plan()
    if app.tplan.check_drafts(service="Профессиональная гигиена: дентикюр Norma") == 0:
        if app.tplan.check_approved(service="Профессиональная гигиена: дентикюр Norma") == 0:
            app.tplan.select_optimal_tplan(area="Шейка зуба",
                                           problem="Зубные отложения",
                                           variants="Снятие зубных отложений/ Профессиональная гигиена",
                                           var_next="Профессиональная гигиена Norma",
                                           doctor="Гигиенистова2 Анна Андреевна")
            app.tplan.canban_approved(service="Профессиональная гигиена: дентикюр Norma")
    app.tplan.cancel_approval()



