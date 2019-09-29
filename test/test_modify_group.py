from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="w11", header="2222", footer="3333"))
    app.session.logout()
