from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify(Contact(firstname="1", middlename="2", lastname="3", nickname="4", company="4",
                               company_address="5", home_number="6", mobile_number="7", work_number="8", fax_number="9", email="1",
                               email2="2", email3="3", homepage="4", bday="5", bmonth="April", byear="1920", aday="5",
                               amonth="April", ayear="1950", address2="1", homephone="1", notes="1"))


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify(Contact(firstname="New name"))