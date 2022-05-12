from graphene_django import DjangoObjectType
from flashcards.models import Deck, Flashcard


class DeckType(DjangoObjectType):
    class Meta:
        model = Deck
        fields = ("id", "title", "description", "flashcards")


class FlashcardType(DjangoObjectType):
    class Meta:
        model = Flashcard
        fields = ("id", "question", "answer", "deck")
