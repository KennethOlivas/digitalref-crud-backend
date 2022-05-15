from flask_sqlalchemy import SQLAlchemy
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField 
from sqlalchemy.exc import IntegrityError
from config.database import db_session
from product.models import Product
from product.serializer import ProductType


# Create Product mutation class
class CreateProduct(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)

    @classmethod
    def mutate(cls, _, info, name, description, price, quantity):
        try:
            product = Product(
                name=name,
                description=description,
                price=price,
                quantity=quantity
            )

            db_session.add(product)
            db_session.commit()

        except IntegrityError as e:
            return CreateProduct(error=f'{e.orig}')
        return CreateProduct(id=product.id, name=product.name, description=product.description, price=product.price, quantity=product.quantity)

# Update Product mutation class
class UpdateProduct(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)

    @classmethod
    def mutate(cls, _, info, id, name, description, price, quantity):
        try:
            product = Product.query.get(id)
            product.name = name
            product.description = description
            product.price = price
            product.quantity = quantity

            db_session.commit()

        except IntegrityError as e:
            return UpdateProduct(error=f'{e.orig}')
        return UpdateProduct(id=product.id, name=product.name, description=product.description, price=product.price, quantity=product.quantity)

# Delete Product mutation class
class DeleteProduct(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    @classmethod
    def mutate(cls, _, info, id):
        try:
            product = Product.query.get(id)
            db_session.delete(product)
            db_session.commit()

        except IntegrityError as e:
            return DeleteProduct(error=f'{e.orig}')
        return DeleteProduct(id=product.id)

class Mutation (graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

# Create Product query class
class Query (graphene.ObjectType):
  Products = SQLAlchemyConnectionField(ProductType.connection)

  

  
