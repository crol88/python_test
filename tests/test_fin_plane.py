from model.group import Group


def test_open_fin_plane(app):
    if app.cbase.count("ФИНПЛАН") == 0:
        app.cbase.add_patient_for(
            Group(surname="Финплан", name="Тест", secondname="Тест", birthday="12082002",
                  phone="79058889852",
                  fromwhere="2ГИС", filial=""))
    app.cbase.search_patient(search_name="Финплан")
    app.tplan.open_fin_plane()
    app.tplan.add_fin_plane_step()
