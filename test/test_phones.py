import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_number == clear(contact_from_edit_page.home_number)
    assert contact_from_home_page.work_number == clear(contact_from_edit_page.work_number)
    assert contact_from_home_page.mobile_number == clear(contact_from_edit_page.mobile_number)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)

def clear(s):
# что заменять, на что заменять, где заменять
   return re.sub("[() -]", "", s)