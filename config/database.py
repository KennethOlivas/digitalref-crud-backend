from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

password = 'password'
database = "digitalref_crud"

def get_engine(user, password, host, port, database):
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url)
    return engine

engine = get_engine(
    user="postgres",
    password=password,
    host="localhost",
    port=5432,
    database=database
)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.create_all(bind=engine)