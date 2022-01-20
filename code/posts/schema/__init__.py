from .mutations import CreatePostMutation, UpdatePostMutation, DeletePostMutation, CreateLikeMutation, DeleteLikeMutation
from .queries import PostQuery, LikeQuery

import graphene


class Query(
    PostQuery,
    LikeQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
    update_post = UpdatePostMutation.Field()
    delete_post = DeletePostMutation.Field()

    create_like = CreateLikeMutation.Field()
    delete_like = DeleteLikeMutation.Field()
