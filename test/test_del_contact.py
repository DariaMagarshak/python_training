# задание 13
from model.contact import Contact
import random



def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


#def test_delete_contact(app):
   # if app.contact.count() == 0:
    #    app.contact.create(Contact(firstname="test"))
   # old_contacts = app.contact.get_contact_list()
   # app.contact.delete_first_contact()
   # assert len(old_contacts) - 1 == app.contact.count()
   # new_contacts = app.contact.get_contact_list()
   # old_contacts[0:1] = []
  #  assert old_contacts == new_contacts