

def test_edit_comments(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments(comments="Comment")


def test_edit_comments_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments_none()


def test_edit_first_record_date(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date(date="11.09.2001")


def test_edit_first_record_date_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date_none()


def test_edit_id1c(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c(id1c="073111")


def test_edit_id1c_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c_none()


def test_edit_fromwhere(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere()
    app.information.select_random_fromwhere()


def test_edit_fromwhere_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere_none()


def test_sms_status_no(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.edit_sms_status_no()


def test_sms_status_yes(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.edit_sms_status_yes()


def test_edit_points_field(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_points_field(points="points")


def test_edit_points_field_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_points_field_none()


def test_edit_total_summ(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ(summ="100500")


def test_edit_total_summ_none(app):
    app.information.change_filial(selected_filial="Филиал 1")
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_total_summ_none()
