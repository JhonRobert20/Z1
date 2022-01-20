import graphene 
from graphql_auth.schema import UserNode
from .filters import UserFilterSet
from ..models import User


class IUserNode(UserNode):
	pk = graphene.Int(source='pk')
	class Meta:
			model = User
			exclude = ["password"]
			filterset_class = UserFilterSet
			interfaces = (graphene.relay.Node, )
