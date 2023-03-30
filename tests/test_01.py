from model.group import Group
import allure


@allure.epic("База пациентов")
@allure.tag("Список пациентов")
@allure.title("Добавить и удалить нового пациента")
@allure.description("Проверить кол-во записей в базе пациентов")
def test_add_and_delete_patient(app):
    old_groups = app.cbase.get_group_list()
    app.cbase.change_filial(Group(filial=""))
    app.cbase.fill_newclient_form(
        Group(surname="Пациент", name="Для", secondname="Удаления", birthday="12081980", phone="79058889556",
              fromwhere="2ГИС"))
    app.cbase.submit_newpatient_creation()
    app.cbase.delete_new_patient(search_name="Пациент")
    new_groups = app.cbase.get_group_list()
    print("Кол-во пациентов до удаления:", old_groups, ';', 'Кол-во пациентов после удаления:', new_groups)
    assert old_groups == new_groups
