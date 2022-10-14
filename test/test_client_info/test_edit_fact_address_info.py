# -*- coding: utf-8 -*-
import testit


@testit.displayName('edit_fact_apartment')
@testit.externalId('056')
def test_edit_fact_apartment(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_apartment(apt="8")


@testit.displayName('edit_fact_apartment_none')
@testit.externalId('057')
def test_edit_fact_apartment_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_apartment_none()


@testit.displayName('edit_fact_house')
@testit.externalId('058')
def test_edit_fact_house(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_house(building="12")


@testit.displayName('dit_fact_house_none')
@testit.externalId('059')
def test_edit_fact_house_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_house_none()


@testit.displayName('edit_fact_city')
@testit.externalId('060')
def test_edit_fact_city(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_city(city="FACT-CITY")


@testit.displayName('dit_fact_city_none')
@testit.externalId('061')
def test_edit_fact_city_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_city_none()


@testit.displayName('edit_fact_country')
@testit.externalId('062')
def test_edit_fact_country(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_country(country="FACT-COUNTRY")


@testit.displayName('edit_fact_country_none')
@testit.externalId('063')
def test_edit_fact_country_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_country_none()


@testit.displayName('edit_fact_postcode')
@testit.externalId('064')
def test_edit_fact_postcode(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode(postcode="432005")


@testit.displayName('dit_fact_postcode_none')
@testit.externalId('065')
def test_edit_fact_postcode_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_postcode_none()


@testit.displayName('edit_fact_state')
@testit.externalId('066')
def test_edit_fact_state(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_state(state="FACT-STATE")


@testit.displayName('edit_fact_state_none')
@testit.externalId('067')
def test_edit_fact_state_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_state_none()


@testit.displayName('edit_fact_street')
@testit.externalId('068')
def test_edit_fact_street(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_street(street="FACT-STREET")


@testit.displayName('edit_fact_street_none')
@testit.externalId('069')
def test_edit_fact_street_none(app):
    app.address.search_patient(search_name="SURNAME")
    app.address.edit_fact_street_none()
