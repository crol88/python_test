def test_edit_fact_apartment(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_apartment(apt="8")


def test_edit_fact_apartment_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_apartment_none()


def test_edit_fact_house(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_house(building="12")


def test_edit_fact_house_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_house_none()


def test_edit_fact_city(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_city(city="FACT-CITY")


def test_edit_fact_city_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_city_none()


def test_edit_fact_country(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_country(country="FACT-COUNTRY")


def test_edit_fact_country_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_country_none()


def test_edit_fact_postcode(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode(postcode="432005")


def test_edit_fact_postcode_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode_none()


def test_edit_fact_state(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_state(state="FACT-STATE")


def test_edit_fact_state_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_state_none()


def test_edit_fact_street(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_street(street="FACT-STREET")


def test_edit_fact_street_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_street_none()
