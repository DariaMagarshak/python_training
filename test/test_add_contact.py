# задание 13
from model.contact import Contact
from sys import maxsize
import pytest
import random
import string
import calendar

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits +""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


random_month1 = random.choice(calendar.month_name)
random_month2 = random.choice(calendar.month_name)
data = list(range(1, 32))
random_data1 = random.choice(data)
random_data2 = random.choice(data)
random_year1 = [random.choice(string.digits) for i in range(4)]
random_year2 = [random.choice(string.digits) for i in range(4)]


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="",
                               company_address="", home_number="", mobile_number="", work_number="", fax_number="", email="",
                               email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-",
                               amonth="-", ayear="", address2="", homephone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                               nickname=random_string("nickname", 10), company=random_string("company", 10),
                               company_address=random_string("company_address", 10), home_number=random_string("home_number", 10),
                               mobile_number=random_string("mobile_number", 10), work_number=random_string("work_number", 10), fax_number=random_string("fax_number", 10),
                               email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                               bday=str(random_data1), bmonth=random_month1, byear=random_year1, aday=str(random_data2), amonth=random_month2, ayear=random_year2, address2=random_string("address2", 10),
                               homephone=random_string("homephone", 10), notes=random_string("notes", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    #contact = Contact(firstname="Тест", middlename="1", lastname="Первый", nickname="IVA_cat", company="ООО corp",
                             #  company_address="СПб, Лесная ул, 1", home_number="777-66-55", mobile_number="89218776342", work_number="3356721", fax_number="3356721", email="iva@mail.ru",
                             #  email2="iva@yandex.ru", email3="ivan_ivan@gmail.com", homepage="ivan.com", bday="17", bmonth="July", byear="1920", aday="17",
                             #  amonth="July", ayear="1950", address2="СПб, Лесная ул, 2", homephone="2233444", notes="-")
