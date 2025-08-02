from dbmodels import Base, engine
from cli import start


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    start()
