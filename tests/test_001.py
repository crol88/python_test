from model.group import Group
import testit


@testit.displayName('Редактировать фамилию пациента')
@testit.externalId('test_edit_patient_surname')
def test_edit_patient_surname(app):
    with testit.step('Открыть список пациентов и проверить наличие пациента'):
        if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
            with testit.step('Если пациент отсутствует, добавляем'):
                app.basic_info.add_patient_for(
                    Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                          phone="79058889556",
                          fromwhere="2ГИС", filial="Филиал 1"))
    with testit.step('Найти пациента через глобальный поиск'):
        app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")
