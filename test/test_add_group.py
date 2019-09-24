# дз 5
# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sss", header="ssss", footer="sssddd"))
    app.session.logout()


def test_add_empty_group(app):
    #app.find_element_by_name("username")
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
