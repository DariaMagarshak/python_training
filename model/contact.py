# задание  13
from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, company_address=None, home_number=None,
                       mobile_number=None, work_number=None, fax_number=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None,
                       aday=None, amonth=None, ayear=None, address2=None, homephone=None, notes=None, id=None, all_emails_from_home_page = None, all_phones_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.company_address = company_address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax_number = fax_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.homephone = homephone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



