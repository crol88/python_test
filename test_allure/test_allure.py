from model.group import Group
import pytest


def test_edit_patient_surname(app):
    with pytest.allure.step('Открыть список пациентов и проверить наличие пациента'):
        if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
            with pytest.allure.step('Если пациента нет, добавляем его'):
                app.basic_info.add_patient_for(
                    Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                          phone="79058889556",
                          fromwhere="2ГИС", filial=""))
    with pytest.allure.step('Найти пациента через поиск'):
        app.basic_info.search_patient(search_name="SURNAME")
    with pytest.allure.step('Редактировать фамилию пациента и проверить результат'):
        app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")
