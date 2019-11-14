# задание 22
from model.contact import Contact
from model.group import Group
import random

def test_del_contact_to_group(app, orm):


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
        # проверяем список контактов, привязанных к текущей группе
        contact_in_group = list(orm.get_contacts_in_group(Group(id="%s" % gr_id)))

        # если такие контакты есть
        if contact_in_group != []:
            c_id = contact_in_group[0].id
            removing_contact = contact_in_group[0]
            # выходим из цикла
            break

        # если такие контакты отсутствуют
        else:
            # берем первый контакт из списка контактов
            removing_contact = app.contact.get_contact_list()[0]
            # вычисляем его идентификатор
            c_id = removing_contact.id
            # добавляем этот контакт в текущую группу
            app.contact.add_contact_to_group(c_id, current_group)

            # выходим из цикла
            break

# получаем начальный список контактов, не привязанных к текущей группе
    old_info = orm.get_contacts_not_in_group(Group(id="%s" % gr_id))
    app.contact.del_contact_from_group(int(c_id), current_group)
    # получаем новый список контактов, не привязанных к текущей группе
    new_info = orm.get_contacts_not_in_group(Group(id="%s" % gr_id))
    # в начальный список контактов, привязанных к текущей группе, добавляем контакт с идентификатором c_id
    old_info.append(removing_contact)
    # сравниваем отсортированные по идентификатору измененный начальный и новый списки контактов, привязанных к текущей группе
    assert sorted(old_info, key=Contact.id_or_max) == sorted(new_info, key=Contact.id_or_max)