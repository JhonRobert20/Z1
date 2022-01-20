import graphene
from graphql_auth.schema import MeQuery, UserQuery
from graphql_auth import mutations
from .queries import IUserQuery


class Query(
    MeQuery,
    IUserQuery,
	UserQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()