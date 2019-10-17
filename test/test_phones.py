import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_number == clear(contact_from_edit_page.home_number)
    assert contact_from_home_page.work_number == clear(contact_from_edit_page.work_number)
    assert contact_from_home_page.mobile_number == clear(contact_from_edit_page.mobile_number)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_number == contact_from_edit_page.home_number
    assert contact_from_view_page.work_number == contact_from_edit_page.work_number
    assert contact_from_view_page.mobile_number == contact_from_edit_page.mobile_number
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone



def clear(s):
# что заменять, на что заменять, где заменять
   return re.sub("[() -]", "", s)