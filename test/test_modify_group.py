# задание 13
from model.group import Group
from random import randrange
import random

def test_modify_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="New group")
    app.group.modify_group_by_id(random_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(random_group)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_group_name(app):
    #if app.group.count() == 0:
     #   app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
  #  group = Group(name="New group")
  #  group.id = old_groups[0].id
  #  app.group.modify_first_group(group)
  #  assert len(old_groups) == app.group.count()
   # new_groups = app.group.get_group_list()
  #  old_groups[0] = group
   # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_group_header(app):
    #if app.group.count() == 0:
     #   app.group.create(Group(name="test1"))
   # old_groups = app.group.get_group_list()

    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test2"))
    #old_groups = app.group.get_group_list()
   # app.group.modify_first_group(Group(footer="New footer"))
   # new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)
