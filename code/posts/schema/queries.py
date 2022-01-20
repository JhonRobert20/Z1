import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from django.db.models import Q

from follows.models import Follow
from ..models import Post
from .nodes import PostNode, LikeNode


class PostQuery(graphene.ObjectType):
    post = graphene.relay.Node.Field(PostNode)
    posts = DjangoFilterConnectionField(PostNode)
    my_posts = DjangoFilterConnectionField(PostNode)

    @login_required
    def resolve_my_posts(self, info, **kwargs):
        user = info.context.user
        return Post.objects.filter(user=user)

    @login_required
    def resolve_posts(self, info, **kwargs):
        user = info.context.user
        follows = Follow.objects.filter(accepted=True, follower=user)
        data = Follow.objects.none()

        if follows.exists():
            for follow in follows:
                print(follow.followed.username)
                posts_data = Post.objects.filter(Q(visibility='PB') | Q(
                    visibility="PO")).filter(user=follow.followed)
                if posts_data:
                    for post_data in posts_data:
                        data.append(post_data)

            new_datas = Post.objects.filter(user=user)
            join_datas = data | new_datas
            return join_datas

        else:
            my_posts_data = Post.objects.filter(user=user)
            join_datas = data | my_posts_data
            return Post.objects.filter(user=user)



class LikeQuery(graphene.ObjectType):
    like = graphene.relay.Node.Field(LikeNode)
    likes = DjangoFilterConnectionField(LikeNode)
