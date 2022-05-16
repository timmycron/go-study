from graphene import Field, ObjectType
from .types import UserType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required

User = get_user_model()


class Query(ObjectType):
    current_user = Field(UserType)

    @login_required
    def resolve_current_user(root, info):
        """
        Get the current user if logged in
        :return: User
        """
        user = info.context.user
        return user
