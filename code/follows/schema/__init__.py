import graphene

from .queries import FollowQuery
from .mutations import AcceptFollowMutation, DeleteFollowMutation, SendFollowMutation


class Query(
    FollowQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    accept_follow = AcceptFollowMutation.Field()
    send_follow = SendFollowMutation.Field()
    delete_follow = DeleteFollowMutation.Field()
