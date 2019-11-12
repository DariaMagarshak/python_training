#import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="257"))
    for item in l:
        print("ITEM = ",item)
    print(len(l))
   # l = db.get_contact_info(Contact(id="222"))
   # print(l)


finally:
    #connection.close()
    #db.destroy()
    pass



    ##cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
       # print(row)