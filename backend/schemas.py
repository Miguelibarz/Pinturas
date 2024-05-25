from pydantic import BaseModel
from typing import List, Optional


# User schemas
class UserBase(BaseModel):
    alias: Optional[str]
    email: str


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# Modelo schemas
class ModeloBase(BaseModel):
    nombre: str
    imprimacion: Optional[str] = None
    visibilidad: bool
    resumen: Optional[str] = None
    idUser: int
    imagen: Optional[str] = None


class ModeloCreate(ModeloBase):
    pass


class ModeloUpdate(ModeloBase):
    pass


class Modelo(ModeloBase):
    id: int
    idUser: int

    class Config:
        orm_mode = True


class ModeloCount(BaseModel):
    count: int


# Parte schemas
class ParteBase(BaseModel):
    nombre: str
    idModelo: Optional[int] = None
    imagen: Optional[str] = None


class ParteCreate(ParteBase):
    pass


class ParteUpdate(ParteBase):
    pass


class Parte(ParteBase):
    id: int
    idModelo: Optional[int] = None

    class Config:
        orm_mode = True


class ParteCount(BaseModel):
    count: int


# Paso schemas
class PasoBase(BaseModel):
    nombre: str
    idColor: int
    idParte: int
    comentario: Optional[str] = None


class PasoCreate(PasoBase):
    pass


class PasoUpdate(PasoBase):
    pass


class Paso(PasoBase):
    id: int
    idColor: int
    idParte: int

    class Config:
        orm_mode = True

        # Color schemas


class ColorBase(BaseModel):
    nombre: str
    codigoHex: str
    marca: str


class ColorCreate(ColorBase):
    pass


class ColorUpdate(ColorBase):
    pass


class Color(ColorBase):
    id: int

    class Config:
        orm_mode = True
