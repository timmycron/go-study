import pytest
from django.core.management import call_command
"""
Herein lies pytest configurations and fixtures useful for testing the flashcards app
"""


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'flashcards.json')


@pytest.fixture
def list_decks_query() -> str:
    """
    Get a query to list all decks with important attributes
    :return: str
    """
    return '''
            query {
                decks {
                    id
                    title
                    description
                }
            }
        '''


@pytest.fixture
def get_deck_query() -> str:
    """
    Get a query to get a single deck with flashcards
    :return: str
    """
    return '''
        query {
            deck(id: 1) {
                title
                description
                flashcards {
                    answer
                    question
                }
            }
        }
    '''
