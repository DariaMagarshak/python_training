# задание 14
import re
from random import randrange
from model.contact import Contact


def test_match_contact(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    for index in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert contacts_from_home_page[index].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[index])
        assert contacts_from_home_page[index].lastname == contacts_from_db[index].lastname
        assert contacts_from_home_page[index].firstname == contacts_from_db[index].firstname
        assert contacts_from_home_page[index].company_address == contacts_from_db[index].company_address


def test_assert_contact_info(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # сравниваем телефоны
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # сравниваем почту
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # сравниваем фамилию
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # сравниваем имя
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    # сравниваем адрес
    assert contact_from_home_page.company_address == contact_from_edit_page.company_address


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home_number, contact.mobile_number, contact.work_number, contact.homephone]))))




def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))



def clear(s):
# что заменять, на что заменять, где заменять
   return re.sub("[() -]", "", s)