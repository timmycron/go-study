from django.db import models


class Deck(models.Model):
    """
    Represents a deck of flashcards
    """
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    """
    Represents a flashcard containing a question and answer, both simple text
    """
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    deck = models.ForeignKey(Deck, related_name="flashcards", on_delete=models.CASCADE)

    def __str__(self):
        return self.question
