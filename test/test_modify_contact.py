# задание 10
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="2", lastname="3", nickname="4", company="4",
                               company_address="5", home_number="6", mobile_number="7", work_number="8", fax_number="9", email="1",
                               email2="2", email3="3", homepage="4", bday="5", bmonth="April", byear="1920", aday="5",
                               amonth="April", ayear="1950", address2="1", homephone="1", notes="1")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify(Contact(firstname="New name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)