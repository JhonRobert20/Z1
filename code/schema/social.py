import graphene
from graphene_django.types import DjangoObjectType
from social.models import ExtendUser

class UserType(DjangoObjectType):
	class Meta:
		model = ExtendUser

class Query(graphene.ObjectType):
	users = graphene.List(UserType)

	def resolve_users(self, info, **kwargs):
		return ExtendUser.objects.all()
