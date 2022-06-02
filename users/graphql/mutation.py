from graphene import ObjectType, Field, Mutation, String
from django.contrib.auth import get_user_model
from .types import UserType
from graphql_jwt import ObtainJSONWebToken, Verify, Refresh, DeleteJSONWebTokenCookie, DeleteRefreshTokenCookie

User = get_user_model()


class CreateUser(Mutation):
    """
    This class allows us to create a user via a GraphQL mutation
    """
    user = Field(UserType)

    class Arguments:
        email = String(required=True)
        password = String(required=True)

    def mutate(self, info, email, password):
        """
        Override the mutate function to create and save the user
        :param email: str
        :param password: str
        :return: CreateUser
        """
        user = User(email=email)
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class Mutation(ObjectType):
    """
    Allow mutations to create a new user, authenticate via JWT, and perform the essential
    JWT token actions (verify, refresh, delete)
    """
    create_user = CreateUser.Field()
    authenticate_with_jwt = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()
    delete_token_cookie = DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = DeleteRefreshTokenCookie.Field()
