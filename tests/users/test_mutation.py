from graphql_jwt.testcases import JSONWebTokenClient
from tests.users.conftest import User, DEFAULT_EMAIL, DEFAULT_PASSWORD


def test_create_user(db, unauthenticated_client: JSONWebTokenClient):
    """
    Test that we can create a user
    :param db:
    :param unauthenticated_client: JSONWebTokenClient
    """
    mutation = '''
        mutation {
            userCreate(email: "test@test.com", password: "test") {
                user {
                    email
                }
            }
        }
    '''
    content = unauthenticated_client.execute(mutation).to_dict()
    assert 'errors' not in content
    assert content == {'data': {'userCreate': {'user': {'email': 'test@test.com'}}}}


def test_login(base_user: User, unauthenticated_client: JSONWebTokenClient):
    """
    Test that we can login as a user
    :param base_user: User
    :param unauthenticated_client: JSONWebTokenClient
    """
    mutation = f'''
        mutation {{
            tokenAuth(email: "{DEFAULT_EMAIL}", password: "{DEFAULT_PASSWORD}") {{
                token
            }}
        }}
    '''
    content = unauthenticated_client.execute(mutation).to_dict()
    assert 'errors' not in content
    assert content['data']['tokenAuth']['token']
