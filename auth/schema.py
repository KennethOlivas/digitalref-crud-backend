import graphene
from sqlalchemy.exc import IntegrityError
from flask_graphql_auth import create_access_token, create_refresh_token, query_header_jwt_required, mutation_header_jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from config.database import db_session
from auth.models import User
from config.helpers import check_email
from auth.serializer import UserType

class Register(graphene.Mutation):
    error = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    @classmethod
    def mutate(cls, _, info, username, password, email):
        if not check_email(email):
            return Register(error="Invalid email")
        try:
            new_user = User(
                username=username,
                password=generate_password_hash(password, method='sha256'),
                email=email
            )

            db_session.add(new_user)
            db_session.commit()

        except IntegrityError as e:
            return Register(error=f'{e.orig}')
        return Register(
            success=True, message=f'User {username} created')

class Login(graphene.Mutation):
    error = graphene.String()
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls, _, info, username, password):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return Login(error="Invalid username")
        if not check_password_hash(user.password, password):
            return Login(error="Invalid password")
        return Login(
            access_token=create_access_token(user.id),
            refresh_token=create_refresh_token(user.id)
        )

class Refresh(graphene.Mutation):
    new_token = graphene.String()

    class Arguments:
        refresh_token = graphene.String(required=True)

    @classmethod
    @mutation_header_jwt_required
    def mutate(cls, _):
        current_user = get_jwt_identity()
        return Refresh(new_token=create_access_token(identity=current_user))


class Mutation(graphene.ObjectType):
    register = Register.Field()
    login = Login.Field()
    refresh = Refresh.Field()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    @classmethod
    @query_header_jwt_required
    def resolve_user(cls, _, info, *args):
        return User.query.filter_by(user=get_jwt_identity()).first()