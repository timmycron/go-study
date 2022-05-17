import pytest
from django.contrib.auth import get_user_model
"""
Herein lies pytest configurations and fixtures useful for testing the users app
Useful tutorial: https://realpython.com/django-pytest-fixtures/
"""

# Constants to allow easy validations
DEFAULT_EMAIL = "a@a.com"
DEFAULT_PASSWORD = "password"

User = get_user_model()


@pytest.fixture
def create_user_from_factory(db):
    """
    Use this throughout tests to easily create users with default values. If anything changes to
    user model, we want to only have this one function require updates.
    :param db: pytest database fixture, required to access DB in tests
    :return: function to allow us to create users easily with defaults
    """
    def create_user(
            email: str = DEFAULT_EMAIL,
            password: str = DEFAULT_PASSWORD,
            is_staff: str = False,
            is_superuser: str = False) -> User:
        user = User.objects.create_user(
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        return user
    return create_user


@pytest.fixture
def base_user(create_user_from_factory) -> User:
    """
    Get the most basic user required for most tests
    :return: User
    """
    return create_user_from_factory()


@pytest.fixture
def current_user_query() -> str:
    """
    Get a query for the current user with their email
    :return: str
    """
    return '''
            query {
                currentUser {
                    email
                }
            }
        '''
