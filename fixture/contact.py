#задание 10 попытка8
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import random
import string
import calendar

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
        #self.return_to_home_page()
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
         # self.app.open_home_page()
         wd = self.app.wd
         wd.find_element_by_link_text("home page").click()

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
                cells = element.find_elements_by_tag_name("td")
                surname_text = cells[1].text
                name_text = cells[2].text
                address_text = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                #нарезка
                all_emails = cells[4].text
                all_phones = cells[5].text
                #all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=surname_text, firstname=name_text, company_address = address_text,
                                                  id=id, all_emails_from_home_page = all_emails,
                                                  all_phones_from_home_page = all_phones))
                                                 # home_number=all_phones[0], mobile_number=all_phones[1],
                                                  #work_number=all_phones[2], homephone=all_phones[3]))
        return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()

        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()

        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        company_address = wd.find_element_by_name("address").get_attribute("value")

        home_number = wd.find_element_by_name("home").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        homephone = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")



        return Contact(firstname=firstname, lastname=lastname, id=id, company_address=company_address,
                        home_number=home_number, work_number=work_number,
                        mobile_number=mobile_number, homephone=homephone, email= email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        homephone = re.search("P: (.*)", text).group(1)


        return Contact(home_number=home_number, work_number=work_number,
                        mobile_number=mobile_number, homephone=homephone)



    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.group_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" %id).click()



    def modify_contact_by_id(self, id, new_data):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # open modification form
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']"%id).click()
        #find_element_by_xpath(".//img[@alt='Edit']").click()
        self.fill_form(new_data)
        self.update_changes()
        self.return_to_home_page()
        self.contact_cache = None



#id = element.find_element_by_name("selected[]").get_attribute("value")