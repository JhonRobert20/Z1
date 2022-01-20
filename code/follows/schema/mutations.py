import graphene
from graphql_jwt.decorators import login_required
from graphql_auth.types import ExpectedErrorType

from ..models import Follow
from .nodes import FollowNode


class AcceptFollowMutation(graphene.relay.ClientIDMutation):
    class Input:
        follower_id = graphene.ID(required=True)

    follow = graphene.Field(FollowNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, follower_id, **kwargs):
        user = info.context.user

        follow = Follow.objects.get(followed=user, follower_id=follower_id)
        follow.accepted = True
        follow.save()
        return AcceptFollowMutation(success=True, follow=follow)


class SendFollowMutation(graphene.relay.ClientIDMutation):
    class Input:
        followed_id = graphene.ID(required=True)

    follow = graphene.Field(FollowNode)
    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, followed_id, **kwargs):
        user = info.context.user
        
        if int(user.pk) != int(followed_id):
            follow = Follow.objects.create(
                follower=user, followed_id=followed_id, accepted=False)
            return SendFollowMutation(success=True, follow=follow)

        return SendFollowMutation(success=False, follow=None)


class DeleteFollowMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.Field(ExpectedErrorType)

    @login_required
    def mutate_and_get_payload(self, info, id, **kwargs):
        user = info.context.user

        try:
            follow = Follow.objects.get(pk=id)
        except Follow.DoesNotExist:
            errors = {
                'follow': [
                    {
                        'message': 'This follow does not exist'
                    }
                ]
            }
            return DeleteFollowMutation(success=False, errors=errors)

        if follow.follower != user:
            raise PermissionError(
                'You do not have the permission to perform this action')

        follow.delete()
        return DeleteFollowMutation(success=True)
