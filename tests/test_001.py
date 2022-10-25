from model.group import Group
import testit


@testit.displayName('Редактировать фамилию пациента')
@testit.externalId('test_edit_patient_surname')
def test_edit_patient_surname(app):
    if app.basic_info.count(check_patient="SURNAME-EDIT") == 0:
        app.basic_info.add_patient_for(
            Group(surname="SURNAME", name="Артур", secondname="Артурович", birthday="12081980",
                  phone="79058889556",
                  fromwhere="2ГИС", filial=""))
    app.basic_info.search_patient(search_name="SURNAME")
    app.basic_info.edit_patient_surname(Group(surname="SURNAME-EDIT"), text="SURNAME-EDIT")
