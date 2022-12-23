from model.group import Group


def test_dental_problem(app):
    if app.cbase.count("МЕДБЛОК") == 0:
        app.cbase.add_patient_for(
            Group(surname="Медблок", name="Тест", secondname="Тест", birthday="12082000",
                  phone="79058889369",
                  fromwhere="2ГИС", filial=""))
    app.tplan.open_treatment_chains()
    app.tplan.search_chains()
    a = app.tplan.check_chain_table()
    app.cbase.search_patient(search_name="МЕДБЛОК")
    app.tplan.open_treatment_plan()
    app.tplan.add_plan()
    app.tplan.select_all_teeth()
    b = app.tplan.select_problem()
    print("Варианты в плане лечения:", b)
    # common = set(a).intersection(b)
    common = [x for x in a if x in b]
    print("Варианты в настройке этапов:", common)
    assert common == b
    app.tplan.treatment_options()
    app.tplan.plan_approved()
    app.tplan.create_fact()
    # app.tplan.check_problem_after_fact()


def test_open_treatment_chains(app):
    app.tplan.open_treatment_chains()
    app.tplan.search_chains()
    app.tplan.check_chain_table()



