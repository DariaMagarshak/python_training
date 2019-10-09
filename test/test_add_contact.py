# задание 10
from model.contact import Contact
from sys import maxsize


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Иван", middlename="Васильевич", lastname="Иванов", nickname="IVA_cat", company="ООО corp",
                               company_address="СПб, Лесная ул, 1", home_number="777-66-55", mobile_number="89218776342", work_number="3356721", fax_number="3356721", email="iva@mail.ru",
                               email2="iva@yandex.ru", email3="ivan_ivan@gmail.com", homepage="ivan.com", bday="17", bmonth="July", byear="1920", aday="17",
                               amonth="July", ayear="1950", address2="СПб, Лесная ул, 2", homephone="2233444", notes="-")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


