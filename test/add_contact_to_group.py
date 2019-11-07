from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    index_c = randrange(len(app.contact.get_contact_list()))
    index_g = randrange(len(app.group.get_group_list()))
    random_contact_id = app.contact.get_contact_list()[index_c].id
    random_group = app.group.get_group_list()[index_g]
    id_group = str(random_group.id)
    #app.contact.add_contact_to_group(index_c, random_group)

    #assert sorted(ORMFixture.get_contacts_in_group(Group(id="id_group")), key=Contact.id_or_max) == sorted(app.contact.get_id_contact_list(), key=Contact.id_or_max)
    #assert random_contact_id ==
    d_b = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    l= d_b.get_contacts_in_group(Group(id="247"))


    for item in l:
        assert sorted(item[???], key=Contact.id_or_max) == sorted(
            app.contact.get_id_contact_list(), key=Contact.id_or_max)
