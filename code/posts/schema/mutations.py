import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType
from django.core.exceptions import ValidationError

from ..models import Post, Like
from .nodes import PostNode, LikeNode


class CreatePostMutation(graphene.relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        summary = graphene.String(required=True)

    post = graphene.Field(PostNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, **kwargs):
        user = info.context.user

        post = Post(user=user, **kwargs)

        try:
            post.full_clean()
        except ValidationError as e:
            return CreatePostMutation(success=False, errors=e.message_dict)

        post.save()
        return CreatePostMutation(success=True, post=post)


class UpdatePostMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        title = graphene.String()
        summary = graphene.String()

    post = graphene.Field(PostNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            errors = {
                'post': [
                    {
                        'message': 'This post does not exist'
                    }
                ]
            }
            return UpdatePostMutation(success=False, errors=errors)

        if post.user != user:
            raise PermissionError(
                'You do not have the permission to perform this action')

        for field, value in kwargs.items():
            setattr(post, field, value)

        try:
            post.full_clean()
        except ValidationError as e:
            return UpdatePostMutation(success=False, errors=e.message_dict)

        post.save()
        return UpdatePostMutation(success=True, post=post)


class DeletePostMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            errors = {
                'post': [
                    {
                        'message': 'This post does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return DeletePostMutation(success=False, errors=errors)

        if post.user != user:
            raise PermissionError(
                'You do not have the permission to perform this action')

        post.delete()
        return DeletePostMutation(success=True)



class CreateLikeMutation(graphene.relay.ClientIDMutation):
    class Input:
        post_id = graphene.ID(required=True)

    like = graphene.Field(LikeNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, post_id, **kwargs):
        user = info.context.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            errors = {
                'post': [
                    {
                        'message': 'This post does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return CreateLikeMutation(success=False, errors=errors)

        like = Like(user=user, post=post)

        try:
            like.full_clean()
        except ValidationError as e:
            return CreateLikeMutation(success=False, errors=e.message_dict)

        like.save()
        return CreateLikeMutation(success=True, like=like)


class DeleteLikeMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            like = Like.objects.get(pk=id)
        except Like.DoesNotExist:
            errors = {
                'like': [
                    {
                        'message': 'This like does not exist',
                        'code': 'does_not_exist'
                    }
                ]
            }
            return DeleteLikeMutation(success=False, errors=errors)

        if like.user != user:
            raise PermissionError(
                'You do not have the permission to perform this action')

        like.delete()
        return DeleteLikeMutation(success=True)
