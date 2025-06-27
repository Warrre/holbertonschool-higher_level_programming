#!/usr/bin/python3
"""
Définition de la classe City qui représente la table cities de la BDD.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Représente une ville dans la base de données.

    Attributs:
        __tablename__ (str): Nom de la table dans la base de données.
        id (Column): Clé primaire auto-incrémentée.
        name (Column): Nom de la ville, limité à 128 caractères.
        state_id (Column): ID de l'état auquel appartient
        la ville (clé étrangère).
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    