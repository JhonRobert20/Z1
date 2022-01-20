import users.schema
import follows.schema
import posts.schema
import graphene


class Query(
    users.schema.Query,
	follows.schema.Query,
	posts.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    posts.schema.Mutation,
	follows.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
