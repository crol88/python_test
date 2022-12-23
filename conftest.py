# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file, encoding="utf-8") as f:
            # with open(request.config.getoption("--target"), encoding="utf-8") as config_file:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(base_url=target['betav11'])
        fixture.session.login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
