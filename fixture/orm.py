from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column= 'group_id')
        name = Optional (str, column= 'group_name')
        header = Optional (str, column= 'group_header')
        footer = Optional(str, column= 'group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table = 'address_in_groups', column = 'id', reverse = 'groups', lazy = True)


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column= 'id')
        firstname = Optional (str, column= 'firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        company_address = Optional(str, column='address')
        home_number = Optional(str, column='home')
        mobile_number = Optional(str, column='mobile')
        work_number = Optional(str, column='work')
        fax_number = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        bday = Optional(str, column='bday')
        bmonth = Optional(str, column='bmonth')
        byear = Optional(str, column='byear')
        aday = Optional(str, column='aday')
        amonth = Optional(str, column='amonth')
        ayear = Optional(str, column='ayear')
        address2 = Optional(str, column='address2')
        homephone = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table = 'address_in_groups', column = 'group_id', reverse = 'contacts', lazy = True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql',host=host, database=name, user=user, password=password, autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        #with db_session:
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, middlename=contact.middlename, lastname=contact.lastname,nickname = contact.nickname, company=contact.company, company_address=contact.company_address,
                            home_number=contact.home_number, mobile_number=contact.mobile_number, work_number=contact.work_number, fax_number=contact.fax_number, email=contact.email,
                            email2= contact.email2, email3=contact.email3, homepage=contact.homepage, bday=contact.bday, bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth,
                            ayear=contact.ayear, address2=contact.address2, homephone=contact.homephone, notes=contact.notes)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        #with db_session:
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))



    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select (g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))


    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select (g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

