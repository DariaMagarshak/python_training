#import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="247"))
    for item in l:
        print(item)
    print(len(l))

finally:
    #connection.close()
    #db.destroy()
    pass



    ##cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
       # print(row)