# задание 17
import pytest
from fixture.application import Application
import jsonpickle
import json
import os.path
import importlib


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    # получаем доступ к сохраненному параметру через объект request
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
           target = json.load(f)
    #base_url = request.config.getoption("--baseUrl")
    #username = request.config.getoption("--username")
    #password = request.config.getoption("--password")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=target['browser'], base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
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
