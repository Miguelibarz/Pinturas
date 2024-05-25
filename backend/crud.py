from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


# CRUD operations for User model
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        alias=user.alias, email=user.email, hashed_password=user.hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user_update.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


# CRUD operations for Modelo model
def get_modelo(db: Session, modelo_id: int):
    return db.query(models.Modelo).filter(models.Modelo.id == modelo_id).first()


def get_modelos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Modelo).offset(skip).limit(limit).all()


def count_modelos(db: Session) -> int:
    return db.query(models.Modelo).count()


def get_modelos_visible(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Modelo)
        .filter(models.Modelo.visibilidad == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_modelo(db: Session, modelo_create: schemas.ModeloCreate):
    db_modelo = models.Modelo(
        nombre=modelo_create.nombre,
        imprimacion=modelo_create.imprimacion,
        visibilidad=modelo_create.visibilidad,
        resumen=modelo_create.resumen,
        idUser=modelo_create.idUser,
        imagen=modelo_create.imagen,
    )
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo


def update_modelo(
    db: Session,
    modelo_id: int,
    modelo_update: schemas.ModeloUpdate,
    db_model: models.Modelo,
):
    db_modelo = db.query(db_model).filter(models.Modelo.id == modelo_id).first()
    if db_modelo is None:
        raise HTTPException(status_code=404, detail="Modelo not found")
    for key, value in modelo_update.dict().items():
        setattr(db_modelo, key, value)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo


def delete_modelo(db: Session, modelo_id: int):
    modelo = db.query(models.Modelo).filter(models.Modelo.id == modelo_id).first()
    if modelo:
        db.delete(modelo)
        db.commit()
        return modelo
    return None


# CRUD operations for Parte model
def get_parte(db: Session, parte_id: int):
    return db.query(models.Parte).filter(models.Parte.id == parte_id).first()


def get_partes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parte).offset(skip).limit(limit).all()


def create_parte(db: Session, parte_create: schemas.ParteCreate):
    db_parte = models.Parte(nombre=parte_create.nombre, idModelo=parte_create.idModelo, imagen=parte_create.imagen)
    db.add(db_parte)
    db.commit()
    db.refresh(db_parte)
    return db_parte


def get_partes_by_id_modelo(
    db: Session, id_modelo: int, skip: int = 0, limit: int = 100
) -> List[models.Parte]:
    return (
        db.query(models.Parte)
        .filter(models.Parte.idModelo == id_modelo)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_parte(db: Session, parte_id: int, parte_update: schemas.ParteUpdate):
    db_parte = db.query(models.Parte).filter(models.Parte.id == parte_id).first()
    if db_parte:
        for key, value in parte_update.dict().items():
            setattr(db_parte, key, value)
        db.commit()
        db.refresh(db_parte)
        return db_parte
    return None


def delete_parte(db: Session, parte_id: int):
    parte = db.query(models.Parte).filter(models.Parte.id == parte_id).first()
    if parte:
        db.delete(parte)
        db.commit()
        return parte
    return None

def update_parte(db: Session, parte_id: int, parte_update: schemas.ParteUpdate, db_parte: models.Parte):
    db_parte = db.query(db_parte).filter(models.Parte.id == parte_id).first()
    if db_parte is None:
        raise HTTPException(status_code=404, detail="Parte not found")
    for key, value in parte_update.dict().items():
        setattr(db_parte, key, value)
    db.commit()
    db.refresh(db_parte)
    return db_parte

# CRUD operations for Paso model
def get_paso(db: Session, paso_id: int):
    return db.query(models.Paso).filter(models.Paso.id == paso_id).first()


def get_pasos_by_id_partes(
    db: Session, idParte: int, skip: int = 0, limit: int = 100
) -> List[models.Paso]:
    return (
        db.query(models.Paso)
        .filter(models.Paso.idParte == idParte)
        .offset(skip)
        .limit(limit)
        .all()
    )

def count_partes(db: Session) -> int:
    return db.query(models.Parte).filter(models.Parte.idModelo.isnot(None)).count()
#fix revisar

def get_pasos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paso).offset(skip).limit(limit).all()


def create_paso(db: Session, paso_create: schemas.PasoCreate):
    db_paso = models.Paso(
        nombre=paso_create.nombre,
        idColor=paso_create.idColor,
        idParte=paso_create.idParte,
        comentario=paso_create.comentario,
    )
    db.add(db_paso)
    db.commit()
    db.refresh(db_paso)
    return db_paso


def update(db: Session, db_model, id: int, obj_in):
    db_obj = db.query(db_model).filter(db_model.id == id).first()
    for var, value in obj_in.dict().items():
        setattr(db_obj, var, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_paso(db: Session, paso_id: int):
    paso = db.query(models.Paso).filter(models.Paso.id == paso_id).first()
    if paso:
        db.delete(paso)
        db.commit()
        return paso
    return None

def update_paso(db: Session, paso_id: int, paso_update: schemas.PasoUpdate, db_paso: models.Paso):
    db_paso = db.query(db_paso).filter(models.Paso.id == paso_id).first()
    if db_paso is None:
        raise HTTPException(status_code=404, detail="Paso not found")
    for key, value in paso_update.dict().items():
        setattr(db_paso, key, value)
    db.commit()
    db.refresh(db_paso)
    return db_paso


# CRUD operations for Color model
def get_color(db: Session, color_id: int):
    return db.query(models.Color).filter(models.Color.id == color_id).first()


def get_colores(db: Session):
    return db.query(models.Color).all()


def create_color(db: Session, color: schemas.ColorCreate):
    db_color = models.Color(**color.dict())
    db.add(db_color)
    db.commit()
    db.refresh(db_color)
    return db_color


def update_color(db: Session, color_id: int, color_update: schemas.ColorUpdate):
    db_color = db.query(models.Color).filter(models.Color.id == color_id).first()
    if db_color:
        for field, value in color_update.dict(exclude_unset=True).items():
            setattr(db_color, field, value)
        db.commit()
        db.refresh(db_color)
        return db_color
    return None

def delete_color(db: Session, color_id: int):
    # Buscar el color en la base de datos por su ID y eliminarlo
    db_color = db.query(models.Color).filter(models.Color.id == color_id).first()
    if db_color:
        db.delete(db_color)
        db.commit()
    else:
        raise ValueError("Color not found")
    
def get_color_by_name(db: Session, nombre: str):
    return db.query(models.Color).filter(models.Color.nombre == nombre).first()