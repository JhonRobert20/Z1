import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode

from ..models import Post, Like
from .filters import PostFilterSet


class PostNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    summary = graphene.String(source='summary')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Post
        filterset_class = PostFilterSet
        interfaces = (graphene.relay.Node,)


class LikeNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    user = graphene.Field(UserNode)

    def resolve_user(self, info, **kwargs):
        return self.user

    class Meta:
        model = Like
        filter_fields = {
            'id': ['exact'],
            'user__id': ['exact'],
            'post__id': ['exact']
        }
        interfaces = (graphene.relay.Node,)