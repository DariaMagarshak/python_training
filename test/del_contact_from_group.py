from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture

def test_del_contact_from_group(app, orm):

    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))

    elif len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    #if len(orm.get_contacts_in_group(Group[0])) == 0:
       # app.contact.add_contact_to_group(0, orm.get_group_list()[0].id)

    index_g = randrange(len(app.group.get_group_list()))
    random_group = app.group.get_group_list()[index_g]
    index_c = randrange(len(app.contact.get_contact_list_from_group(random_group)))
    random_contact = app.contact.get_contact_list_from_group(random_group)[index_c]
    # id_group = random_group.id
    id_contact = random_contact.id

    # получаем старый список контактов в определенной группе
    # old_group_with_contacts = orm.get_contacts_in_group(Group(id="%s" % id_group))
    old_info = orm.get_contact_info(Group(id="%s" % id_contact))
    # удаляем случайный контакт из случайной группы
    app.contact.del_contact_from_group(index_c, random_group)

    # получаем новый список контактов в определенной группе
    # new_group_with_contacts = orm.get_contacts_in_group(Group(id="%s" % id_group))
    new_info = orm.get_contact_info(Group(id="%s" % id_contact))

    old_info.remove(random_group)

    # сравниваем старый и новый списки

   # assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)