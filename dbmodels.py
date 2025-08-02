from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase,
    mapped_column,
    Mapped,
    relationship,
)

from dotenv import load_dotenv
import os

load_dotenv(".env")
database_url = os.getenv("DATABASE_URL")

engine = create_engine(url=database_url)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class Domain(Base):
    __tablename__ = "domains"

    id: Mapped[int] = mapped_column(primary_key=True)
    domain: Mapped[str] = mapped_column(unique=True)

    credentials: Mapped[list["Credential"]] = relationship(
        back_populates="domain", cascade="all, delete-orphan"
    )


class Credential(Base):
    __tablename__ = "credentials"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id", ondelete="CASCADE"))

    domain: Mapped["Domain"] = relationship(back_populates="credentials")
