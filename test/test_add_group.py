# задание 10
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="sss", header="ssss", footer="sssddd"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
