from graphql_jwt.testcases import JSONWebTokenClient


def test_list_decks(django_db_setup, authenticated_client: JSONWebTokenClient, list_decks_query: str):
    """
    Test that we can list all flashcard decks through our graphql endpoint
    :param django_db_setup:
    :param authenticated_client: JSONWebTokenClient
    :param list_decks_query: str
    """
    content = authenticated_client.execute(list_decks_query).to_dict()

    assert 'errors' not in content
    assert 'decks' in content['data']

    decks = content['data']['decks']

    assert len(decks) == 2


def test_list_decks_unauthenticated(django_db_setup, unauthenticated_client: JSONWebTokenClient, list_decks_query: str):
    """
    Test that we can't list all flashcard decks if we're unauthenticated
    :param django_db_setup:
    :param unauthenticated_client: JSONWebTokenClient
    :param list_decks_query: str
    """
    content = unauthenticated_client.execute(list_decks_query).to_dict()
    assert 'errors' in content


def test_get_deck(django_db_setup, authenticated_client: JSONWebTokenClient, get_deck_query: str):
    """
    Test that we can get a single deck by ID and that it contains the flashcards
    :param django_db_setup:
    :param authenticated_client: JSONWebTokenClient
    :param get_deck_query: str
    """
    content = authenticated_client.execute(get_deck_query).to_dict()

    assert 'errors' not in content

    deck = content['data']['deck']

    assert deck['title'] == 'Spanish'
    assert deck['description'] == 'Learn some Spanish'
    assert len(deck['flashcards']) == 2


def test_get_deck_unauthenticated(django_db_setup, unauthenticated_client: JSONWebTokenClient, get_deck_query: str):
    """
    Test that we can't list all flashcard decks if we're unauthenticated
    :param django_db_setup:
    :param unauthenticated_client: JSONWebTokenClient
    :param get_deck_query: str
    """
    content = unauthenticated_client.execute(get_deck_query).to_dict()
    assert 'errors' in content
