from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, orm):
    def find_adding_contact():
        if len(app.contact.get_contact_list()) == 0:
            if len(app.group.get_group_list()) == 0:
                app.group.create(Group(name="test"))
            app.contact.create(Contact(firstname="test"))
        elif len(app.group.get_group_list()) == 0:
            app.group.create(Group(name="test"))

        for gr_indx in range(len(app.group.get_group_list())):
            # получаем группу по текущему индексу
            current_group = app.group.get_group_list()[gr_indx]
            # получаем id текущей группы
            gr_id = str(current_group.id)
            # проверяем, список контактов, которые не привязаны к текущей группе
            contact_not_in_group = list(orm.get_contacts_not_in_group(Group(id="%s" % gr_id)))

            # если это последняя группа в цикле
            if gr_indx == -1:
                # если есть контакты, которые еще не привязаны к группе (список не пустой)
                if contact_not_in_group != []:
                    c_id = contact_not_in_group[0].id
                    adding_contact = contact_not_in_group[0]
                # если все имеющиеся контакты уже привязаны к группе (список пустой)
                else:
                    # создаем новый контакт
                    app.contact.create(Contact(firstname="New contact3"))
                    c_id = app.contact.get_contact_list()[-1].id
                    adding_contact = orm.get_contact_list()[-1]

            # если это не последняя группа в цикле
            else:
                # если есть контакты, которые еще не привязаны к группе (список не пустой)
                if contact_not_in_group != []:
                    c_id = contact_not_in_group[0].id
                    adding_contact = contact_not_in_group[0]

    return adding_contact, gr_id, c_id, current_group ???




    # получаем начальный список контактов, привязанных к текущей группе
    old_info = orm.get_contacts_in_group(Group(id="%s" % gr_id))
    app.contact.add_contact_to_group(c_id, current_group)
    # получаем новый список контактов, привязанных к текущей группе
    new_info = orm.get_contacts_in_group(Group(id="%s" % gr_id))
    # в начальный список контактов, привязанных к текущей группе, добавляем контакт с идентификатором c_id
    old_info.append(adding_contact)
    # сравниваем отсортированные по идентификатору измененный начальный и новый списки контактов, привязанных к текущей группе
    assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)






