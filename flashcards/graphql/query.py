import graphene
from flashcards.models import Deck, Flashcard
from flashcards.graphql.types import DeckType, FlashcardType


class Query(graphene.ObjectType):
    all_flashcards = graphene.List(FlashcardType)
    deck_by_title = graphene.Field(DeckType, title=graphene.String(required=True))

    def resolve_all_flashcards(root, info):
        # We can easily optimize query count in the resolve method
        return Flashcard.objects.select_related("deck").all()

    def resolve_deck_by_title(root, info, title):
        try:
            return Deck.objects.get(title=title)
        except Deck.DoesNotExist:
            return None
