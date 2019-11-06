# задание 17
import pytest
from fixture.application import Application
import jsonpickle
import json
import os.path
import importlib
from fixture.db import DbFixture


fixture = None
target = None
def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
           target = json.load(f)
    return target



@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))['web']
    # получаем доступ к сохраненному параметру через объект request
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=web_config['browser'], base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
#параметр browser, действие "сохранить параметр", дефолтное значение
    #parser.addoption("--browser", action="store", default = "firefox")
    #parser.addoption("--baseUrl", action="store", default = "http://localhost/addressbook/")
    #parser.addoption("--username", action="store", default = "admin")
    #parser.addoption("--password", action="store", default = "secret")
    parser.addoption("--target", action="store", default = "target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
   return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as ff:
        return jsonpickle.decode(ff.read())

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture