from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture

def test_del_contact_from_group(app, orm):

    if len(app.contact.get_contact_list()) == 0:
        if len(app.group.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        app.contact.create(Contact(firstname="test"))

    elif len(app.group.get_group_list()) == 0:
            app.group.create(Group(name="test"))

    index_g = randrange(len(app.group.get_group_list()))
    random_group = app.group.get_group_list()[index_g]
    index_c = randrange(len(app.contact.get_contact_list_from_group(random_group)))
    random_contact = app.contact.get_contact_list_from_group(random_group)[index_c]
    # id_group = random_group.id
    id_contact = random_contact.id

    old_info = orm.get_contact_info(Group(id="%s" % id_contact))
    if old_info == []:
        app.contact.add_contact_to_group(index_c, random_group)
        old_info = orm.get_contact_info(Group(id="%s" % id_contact))

    app.contact.del_contact_from_group(index_c, random_group)
    new_info = orm.get_contact_info(Group(id="%s" % id_contact))
    old_info.remove(random_group)

    # сравниваем старый и новый списки
    assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)