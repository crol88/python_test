def test_edit_comments(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments(comments="Comment")


def test_edit_comments_none(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_comments_none()


def test_edit_first_record_date(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date(date="11.09.2001")


def test_edit_first_record_date_none(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_first_record_date_none()


def test_edit_id1c(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c()


def test_edit_id1c_none(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_id1c_none()


def test_edit_fromwhere(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere()


def test_edit_fromwhere_none(app):
    app.information.search_patient(search_name="SURNAME")
    app.information.edit_fromwhere_none()



