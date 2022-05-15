import graphene
import auth.schema
import product.schema

class Query(product.schema.Query, auth.schema.Query, graphene.ObjectType):
    pass

class Mutation(product.schema.Mutation, auth.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(mutation=Mutation, query=Query)
