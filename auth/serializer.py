import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import User

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)
