import pytest

from common.dbHelper import DBHelper


@pytest.fixture(scope="session", autouse=True)
def db():
    return DBHelper()
