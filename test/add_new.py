# -*- coding: utf-8 -*-
#from selenium import webdriver
#import unittest
import pytest
from model.contact import Contact
from fixture.application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Иван", middlename="Васильевич", lastname="Котейкин", nickname="IVA_cat", company="Производство блинчиков corp",
                            company_address="СПб, Лесная ул, 1", home_number="777-66-55", mobile_number="89218776342", work_number="3356721", fax_number="3356721", email="iva_cat@mail.ru",
                            email2="kot_obormot@yandex.ru", email3="ivan_ivan@gmail.com", homepage="ivan.com", bday="12", bmonth="April", byear="1920", aday="12",
                            amonth="April", ayear="1950", address2="СПб, Лесная ул, 2", homephone="2233444", notes="уточнить по поводу блинчиков"))

    app.session_contact.logout()



