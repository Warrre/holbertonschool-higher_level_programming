#!/usr/bin/python3
"""
Définition de la classe State et d'une instance Base.

Ce module contient la classe State qui représente la table states
d'une base de données MySQL.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Représente un état dans la base de données.

    Attributs:
        __tablename__ (str): Nom de la table dans la base de données.
        id (Column): Clé primaire auto-incrémentée.
        name (Column): Nom de l'état, limité à 128 caractères.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    