import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .nodes import IUserNode


class IUserQuery(graphene.ObjectType):
    user = graphene.relay.Node.Field(IUserNode)
    users = DjangoFilterConnectionField(IUserNode)
