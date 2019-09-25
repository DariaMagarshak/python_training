from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Vasya", middlename="Vasilievich", lastname="Vasiliev", nickname="Vasya3333", company="Vasya1",
                               company_address="СПб, Лесная ул, 1", home_number="777-66-55", mobile_number="89218776342", work_number="3356721", fax_number="3356721", email="iva_cat@mail.ru",
                               email2="Vasya@yandex.ru", email3="Vasya@gmail.com", homepage="Vasya.com", bday="12", bmonth="April", byear="1920", aday="12",
                               amonth="April", ayear="1950", address2="СПб, Лесная ул, 2", homephone="2233444", notes="1"))
    app.session.logout()