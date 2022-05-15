import graphene 
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Product

class ProductType(SQLAlchemyObjectType):
    
    class Meta:
        model = Product
        interfaces = (graphene.relay.Node,)
        fields = "__all__"