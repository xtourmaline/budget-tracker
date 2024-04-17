# file: schema.py

from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'budget'

TABLES = {}
TABLES['user'] = (
    "CREATE TABLE `user` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `firstName` varchar(20) NOT NULL,"
    "  `lastName` varchar(20) NOT NULL,"
    "  `email` "
    "  `password` varchar(255),"
    "  `` date NO,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


# DROP DATABASE IF EXISTS budget_db;
# CREATE DATABASE budget_db;

# USE budget_db;

# CREATE TABLE User(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     firstName VARCHAR(20) NOT NULL
#     lastName VARCHAR(20) NOT NULL
#     password
# )


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key = True)
    email: Mapped[str] = mapped_column(String(255))


    email = db.Column(db.String(255), unique=True)
    firstName = db.Column(db.String(20), unique=True)
    lastName = db.Column(db.String(20), unique=True)

    def __init__(self, email, firstName, lastName, password):
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName
        self.__password = password

class Wallet():
    __tablename__ = "Wallets"

    id: Mapped[int] = mapped_column(primary_key = True)

class Transaction():
    __tablename__ = "Transactions"

    id: Mapped[int] = mapped_column(primary_key = True)