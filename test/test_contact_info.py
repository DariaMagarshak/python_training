import re
from random import randrange


#сравниваем телефоны
def test_phones_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home_number, contact.mobile_number, contact.work_number, contact.homephone]))))


#сравниваем почту
def test_emails_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))


# сравниваем фамилию
def test_lastname_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


# сравниваем имя
def test_firstname_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


# сравниваем адрес
def test_address_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.company_address == contact_from_edit_page.company_address

def clear(s):
# что заменять, на что заменять, где заменять
   return re.sub("[() -]", "", s)