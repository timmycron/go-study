import pytest
from django.core.management import call_command
"""
This file allows us to run functions to configure our database before the tests run.
"""


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'flashcards.json')
