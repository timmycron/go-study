from graphql_jwt.testcases import JSONWebTokenClient
from tests.users.conftest import DEFAULT_EMAIL


def test_resolve_current_user(authenticated_client: JSONWebTokenClient, current_user_query: str):
    """
    Test that we can get the current user, the email is correct, and there isn't a password
    :param authenticated_client: JSONWebTokenClient
    :param current_user_query: str
    """
    content = authenticated_client.execute(current_user_query).to_dict()
    assert 'errors' not in content
    assert content == {'data': {'currentUser': {'email': DEFAULT_EMAIL}}}


def test_resolve_current_user_unauthenticated(unauthenticated_client: JSONWebTokenClient, current_user_query: str):
    """
    Test that we get an error if we try to get the current user without first authenticating
    :param unauthenticated_client: JSONWebTokenClient
    :param current_user_query: str
    """
    content = unauthenticated_client.execute(current_user_query).to_dict()
    assert 'errors' in content


def test_cannot_resolve_password(authenticated_client: JSONWebTokenClient):
    """
    Test that we cannot get the current users password, even if authenticated
    :param authenticated_client: JSONWebTokenClient
    """
    query = '''
            query {
                currentUser {
                    password
                }
            }
        '''
    content = authenticated_client.execute(query).to_dict()
    assert 'errors' in content
