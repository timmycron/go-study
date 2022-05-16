import graphene
import flashcards.graphql.query


class Query(flashcards.graphql.query.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


schema = graphene.Schema(query=Query)
