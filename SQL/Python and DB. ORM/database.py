import sqlalchemy
from sqlalchemy.orm import sessionmaker


def create_engine():
    DSN = "postgresql://postgres:majkl4321@localhost:5432/netology"
    engine = sqlalchemy.create_engine(DSN)
    return engine


def create_tables(engine):
    from models import Base
    Base.metadata.create_all(engine)


def get_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
