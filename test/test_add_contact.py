from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Иван", middlename="Васильевич", lastname="Котейкин", nickname="IVA_cat", company="Производство блинчиков corp",
                               company_address="СПб, Лесная ул, 1", home_number="777-66-55", mobile_number="89218776342", work_number="3356721", fax_number="3356721", email="iva_cat@mail.ru",
                               email2="kot_obormot@yandex.ru", email3="ivan_ivan@gmail.com", homepage="ivan.com", bday="12", bmonth="April", byear="1920", aday="12",
                               amonth="April", ayear="1950", address2="СПб, Лесная ул, 2", homephone="2233444", notes="уточнить по поводу блинчиков"))




