import json
import pytest
from graphene_django.utils.testing import graphql_query

# "This is used to mark a test function as requiring the database.
# It will ensure the database is set up correctly for the test.
# Each test will run in its own transaction which will be rolled back at the end of the test."
# - https://pytest-django.readthedocs.io/en/latest/helpers.html
pytestmark = pytest.mark.django_db


def test_list_decks(django_db_setup):
    """
    Test that we can list all flashcard decks through our graphql endpoint
    """
    query = '''
        query {
            decks {
                id
                title
                description
            }
        }
    '''
    response = graphql_query(query)
    content = json.loads(response.content)

    assert 'errors' not in content
    assert 'decks' in content['data']

    decks = content['data']['decks']

    assert len(decks) == 2


def test_get_deck(django_db_setup):
    """
    Test that we can get a single deck by ID and that it contains the flashcards
    """
    query = '''
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
    response = graphql_query(query)
    content = json.loads(response.content)

    assert 'errors' not in content

    deck = content['data']['deck']

    assert deck['title'] == 'Spanish'
    assert deck['description'] == 'Learn some Spanish'
    assert len(deck['flashcards']) == 2
