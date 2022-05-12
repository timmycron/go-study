import graphene
from flashcards.graphql.query import Query


schema = graphene.Schema(query=Query)
