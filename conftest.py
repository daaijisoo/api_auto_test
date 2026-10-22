import pytest
import requests

from api.user.index import User
from common.dbHelper import DBHelper


@pytest.fixture(scope="session", autouse=True)
def db():
    return DBHelper()


@pytest.fixture(scope="session", autouse=True)
def session():
    session = requests.session()
    yield session
    session.close()