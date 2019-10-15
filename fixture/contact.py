from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_forms_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            #wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
            self.app.open_edit_page()

    def create(self, contact):
        wd = self.app.wd
        self.open_forms_page()
        self.fill_form(contact)

        self.applying_changes()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self,  index, new_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_elements_by_name("entry")[index].find_element_by_xpath(".//img[@alt='Edit']").click()

        self.fill_form(new_data)
        self.update_changes()
        self.return_to_home_page()
        self.contact_cache = None

    def modify(self):
        self.modify_contact_by_index(0)

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.company_address)
        self.change_field_value("home", contact.home_number)
        self.change_field_value("mobile", contact.mobile_number)
        self.change_field_value("work", contact.work_number)
        self.change_field_value("fax", contact.fax_number)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_data("bday", contact.bday)
        self.select_data("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_data("aday", contact.aday)
        self.select_data("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.homephone)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_data(self, field_name, data):
        wd = self.app.wd
        if data is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(data)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def update_changes(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def applying_changes(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("(//img[@alt='Edit'])")) > 0):
            wd.find_element_by_link_text("home").click()
        # self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                surname_text = element.find_elements_by_tag_name("td")[1].text
                name_text = element.find_elements_by_tag_name("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=surname_text, firstname=name_text, id=id))
        return list(self.contact_cache)

