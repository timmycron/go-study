import graphene
from flashcards.models import Deck
from flashcards.graphql.types import DeckType


class Query(graphene.ObjectType):
    deck = graphene.Field(DeckType, id=graphene.Int())
    decks = graphene.List(DeckType)

    def resolve_deck(self, info, id):
        """
        Get a single flashcard deck by ID
        :return: Deck
        """
        return Deck.objects.get(id=id)

    def resolve_decks(root, info):
        """
        Get a list of all flashcard decks
        :return: Deck[]
        """
        return Deck.objects.all()
