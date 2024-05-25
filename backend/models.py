from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    alias = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    modelos = relationship("Modelo", back_populates="owner")


class Modelo(Base):
    __tablename__ = "modelos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    imprimacion = Column(String, index=True)
    visibilidad = Column(Boolean, index=True)
    imagen = Column(String)
    resumen = Column(String, index=True)
    idUser = Column(Integer, ForeignKey("users.id"))

    partes = relationship("Parte", back_populates="owner")

    owner = relationship("User", back_populates="modelos")


class Parte(Base):
    __tablename__ = "partes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    imagen = Column(String)
    idModelo = Column(Integer, ForeignKey("modelos.id"))

    owner = relationship("Modelo", back_populates="partes")


class Paso(Base):
    __tablename__ = "pasos"

    id = Column(Integer, primary_key=True)
    idColor = Column(Integer, ForeignKey("colores.id"))
    nombre = Column(String, index=True)
    idParte = Column(Integer, ForeignKey("partes.id"))
    comentario = Column(String)


class Color(Base):
    __tablename__ = "colores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    codigoHex = Column(String, index=True)
    marca = Column(String, index=True)
