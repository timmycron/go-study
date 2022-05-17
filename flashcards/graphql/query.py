from graphene import Field, Int, ObjectType, List
from graphql_jwt.decorators import login_required
from flashcards.models import Deck
from flashcards.graphql.types import DeckType


class Query(ObjectType):
    deck = Field(DeckType, id=Int())
    decks = List(DeckType)

    @login_required
    def resolve_deck(self, info, id):
        """
        Get a single flashcard deck by ID if logged in
        :return: Deck
        """
        return Deck.objects.get(id=id)

    @login_required
    def resolve_decks(root, info):
        """
        Get a list of all flashcard decks if logged in
        :return: Deck[]
        """
        return Deck.objects.all()
