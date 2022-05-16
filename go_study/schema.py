from graphene import ObjectType, Schema
import flashcards.graphql.query
import users.graphql.query
import users.graphql.mutation


class Query(users.graphql.query.Query, flashcards.graphql.query.Query, ObjectType):
    pass


class Mutation(users.graphql.mutation.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
