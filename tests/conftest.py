import pytest

@pytest.fixture(scope='session')
def hello():
    return 'hellow'
