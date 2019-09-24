
from selenium import webdriver
from fixture.session_contact import SessionContact
from fixture.contact import ContactHelper

class ApplicationContact:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionContact(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")


    def destroy(self):
        self.wd.quit()