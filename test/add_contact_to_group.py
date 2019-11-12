from model.contact import Contact
from model.group import Group
import re
from random import randrange
from fixture.orm import ORMFixture

def test_add_contact_to_group(app, orm):

    if len(app.contact.get_contact_list()) == 0:
        if len(app.group.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        app.contact.create(Contact(firstname="test"))
    elif len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="test"))



    for gr_indx in range(len(app.group.get_group_list())):

        current_group = app.group.get_group_list()[gr_indx]
        gr_id = str(current_group.id)
        contact_not_in_group = list(orm.get_contacts_not_in_group(Group(id="%s" % gr_id)))
        if contact_not_in_group !=[]:
            c_id = contact_not_in_group[0].id
            old_info = orm.get_contact_info(Group(id="%s" % c_id))
            app.contact.add_contact_to_group(c_id, current_group)
            new_info = orm.get_contact_info(Group(id="%s" % c_id))
            group_from_db = orm.get_group_list()[gr_indx]
            old_info.append(group_from_db)
        else:
            new_contact = app.contact.create(Contact(firstname="New contact2"))
            c_id = app.contact.get_contact_list()[len(app.group.get_group_list())+1].id
            old_info = orm.get_contact_info(Group(id="%s" % str(c_id)))
            app.contact.add_contact_to_group(c_id, current_group)
            new_info = orm.get_contact_info(Group(id="%s" % str(c_id)))
            group_from_db = orm.get_group_list()[gr_indx]
            old_info.append(group_from_db)

        assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)








   # index_c = randrange(len(app.contact.get_contact_list()))
    #index_g = randrange(len(app.group.get_group_list()))

    #random_group = app.group.get_group_list()[index_g]
    #random_contact = app.contact.get_contact_list()[index_c]
    #id_group = random_group.id
    #id_contact = random_contact.id

    #old_info = orm.get_contact_info(Group(id="%s" % c_id))
    # добавляем случайный контакт в случайную группу
    #app.contact.add_contact_to_group(index_c, random_group)
    #new_info = orm.get_contact_info(Group(id="%s" % c_id))
    #old_info.append(random_group)

    # сравниваем старый и новый списки
   # assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)

