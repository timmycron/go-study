from graphql_jwt.testcases import JSONWebTokenClient
# must include all fixture imports from separate files for pytest to function properly
from tests.users.conftest import *
from tests.flashcards.conftest import *
"""
Herein lies pytest configurations and fixtures useful for testing the entire project
"""


@pytest.fixture
def unauthenticated_client() -> JSONWebTokenClient:
    """
    Fixture to allow tests to use an unauthenticated client
    :return: JSONWebTokenClient
    """
    client = JSONWebTokenClient()
    return client


@pytest.fixture
def authenticated_client(base_user: User) -> JSONWebTokenClient:
    """
    Fixture to allow tests to use an authenticated client. Creates a user as a side effect.
    :return: JSONWebTokenClient
    """
    client = JSONWebTokenClient()
    client.authenticate(base_user)
    return client
