import json
import os
import shutil
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List, Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


tags_metadata = [
    {"name": "Modelos", "description": "APIs for modelos"},
    {"name": "Partes", "description": "APIs for partes"},
    {"name": "Pasos", "description": "APIs for pasos"},
    {"name": "Users", "description": "APIs for users"},
    {"name": "Colores", "description": "APIs for colores"},
    {"name": "Imagen", "description": "APIs for imagen"},
    {"name": "API", "description": "importaciones API colores"},
]


# MODELOS operations
@app.post("/modelos/", response_model=schemas.Modelo, tags=["Modelos"])
def create_modelo(modelo: schemas.ModeloCreate, db: Session = Depends(get_db)):
    return crud.create_modelo(db=db, modelo_create=modelo)


@app.get("/modelos/count", response_model=schemas.ModeloCount, tags=["Modelos"])
def count_modelos(db: Session = Depends(get_db)):
    count = crud.count_modelos(db)
    return {"count": count}


# SHOW ALL MODELOS
# @app.get("/modelos/", response_model=List[schemas.Modelo], tags=["Modelos"])
# def read_modelos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    modelos = crud.get_modelos(db, skip=skip, limit=limit)
#    return modelos


@app.get("/modelos/", response_model=List[schemas.Modelo], tags=["Modelos"])
def read_modelos_visible(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    modelos = crud.get_modelos_visible(db, skip=skip, limit=limit)
    return modelos


@app.get("/modelos/{modelo_id}", response_model=schemas.Modelo, tags=["Modelos"])
def read_modelo(modelo_id: int, db: Session = Depends(get_db)):
    db_modelo = crud.get_modelo(db, modelo_id=modelo_id)
    if db_modelo is None:
        raise HTTPException(status_code=404, detail="Modelo not found")
    return db_modelo


@app.put("/modelos/{modelo_id}", response_model=schemas.Modelo, tags=["Modelos"])
def update_modelo(
    modelo_id: int, modelo_update: schemas.ModeloUpdate, db: Session = Depends(get_db)
):
    db_modelo = crud.get_modelo(db, modelo_id=modelo_id)
    if db_modelo is None:
        raise HTTPException(status_code=404, detail="Modelo not found")
    return crud.update_modelo(
        db=db, modelo_id=modelo_id, modelo_update=modelo_update, db_model=models.Modelo
    )


@app.delete("/modelos/{modelo_id}", response_model=schemas.Modelo, tags=["Modelos"])
def delete_modelo(modelo_id: int, db: Session = Depends(get_db)):
    return crud.delete_modelo(db=db, modelo_id=modelo_id)

@app.get("/search_modelo", response_model=List[schemas.Modelo], tags=["Modelos"])
def search_modelo(search: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(models.Modelo)
    
    if search:
        query = query.filter(models.Modelo.nombre.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()

# PARTES operations
@app.post("/partes/", response_model=schemas.Parte, tags=["Partes"])
def create_parte(parte: schemas.ParteCreate, db: Session = Depends(get_db)):
    return crud.create_parte(db=db, parte_create=parte)


@app.get("/partes/", response_model=List[schemas.Parte], tags=["Partes"])
def read_partes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    partes = db.query(models.Parte).offset(skip).limit(limit).all()
    return partes


@app.get("/partes/count", response_model=schemas.ParteCount, tags=["Partes"])
def count_partes(db: Session = Depends(get_db)):
    count = crud.count_partes(db)
    return {"count": count}


@app.get("/getPartes/{id_modelo}", response_model=List[schemas.Parte], tags=["Partes"])
def read_partes_by_IDModelo(
    id_modelo: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    partes = crud.get_partes_by_id_modelo(db, id_modelo, skip=skip, limit=limit)
    return partes


@app.get("/partes/{parte_id}", response_model=schemas.Parte, tags=["Partes"])
def read_parte(parte_id: int, db: Session = Depends(get_db)):
    db_parte = crud.get_parte(db, parte_id=parte_id)
    if db_parte is None:
        raise HTTPException(status_code=404, detail="Parte not found")
    return db_parte


@app.put("/partes/{parte_id}", response_model=schemas.Parte, tags=["Partes"])
def update_parte(
    parte_id: int, parte_update: schemas.ParteUpdate, db: Session = Depends(get_db)
):
    db_parte = crud.get_parte(db, parte_id=parte_id)
    if db_parte is None:
        raise HTTPException(status_code=404, detail="Parte not found")
    return crud.update_parte(
        db=db, parte_id=parte_id, parte_update=parte_update, db_parte=models.Parte
    )


@app.delete("/partes/{parte_id}", response_model=schemas.Parte, tags=["Partes"])
def delete_parte(parte_id: int, db: Session = Depends(get_db)):
    return crud.delete_parte(db=db, parte_id=parte_id)


@app.get("/search_partes", response_model=List[schemas.Parte], tags=["Partes"])
def search_partes(search: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(models.Parte)
    
    if search:
        query = query.filter(models.Parte.nombre.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()

# PASOS operations
@app.post("/pasos/", response_model=schemas.Paso, tags=["Pasos"])
def create_paso(paso: schemas.PasoCreate, db: Session = Depends(get_db)):
    return crud.create_paso(db=db, paso_create=paso)


@app.get("/getPasos/{id_parte}", response_model=List[schemas.Paso], tags=["Pasos"])
def read_pasos_by_IDPartes(
    id_parte: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    pasos = crud.get_pasos_by_id_partes(db, id_parte, skip=skip, limit=limit)
    return pasos


@app.get("/pasos/", response_model=List[schemas.Paso], tags=["Pasos"])
def read_pasos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pasos = crud.get_pasos(db, skip=skip, limit=limit)
    return pasos


@app.get("/pasos/{paso_id}", response_model=schemas.Paso, tags=["Pasos"])
def read_paso(paso_id: int, db: Session = Depends(get_db)):
    db_paso = crud.get_paso(db, paso_id=paso_id)
    if db_paso is None:
        raise HTTPException(status_code=404, detail="Paso not found")
    return db_paso


@app.delete("/pasos/{paso_id}", response_model=schemas.Parte, tags=["Pasos"])
def delete_paso(paso_id: int, db: Session = Depends(get_db)):
    return crud.delete_paso(db=db, paso_id=paso_id)


@app.put("/pasos/{paso_id}", response_model=schemas.Paso, tags=["Pasos"])
def update_paso(
    paso_id: int, paso_update: schemas.PasoUpdate, db: Session = Depends(get_db)
):
    db_paso = crud.get_paso(db, paso_id=paso_id)
    if db_paso is None:
        raise HTTPException(status_code=404, detail="Paso not found")
    return crud.update_paso(
        db=db, paso_id=paso_id, paso_update=paso_update, db_paso=models.Paso
    )


# USERS operations
@app.post("/users/", response_model=schemas.User, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)


# COLORS operations
@app.post("/colores/", response_model=schemas.Color, tags=["Colores"])
def create_color(color: schemas.ColorCreate, db: Session = Depends(get_db)):
    return crud.create_color(db=db, color=color)


@app.get("/colores/", response_model=List[schemas.Color], tags=["Colores"])
def read_colores(db: Session = Depends(get_db)):
    colores = crud.get_colores(db)
    return colores


@app.get("/colores/{color_id}", response_model=schemas.Color, tags=["Colores"])
def read_color(color_id: int, db: Session = Depends(get_db)):
    db_color = crud.get_color(db, color_id=color_id)
    if db_color is None:
        raise HTTPException(status_code=404, detail="Color not found")
    return db_color


@app.put("/colores/{color_id}", response_model=schemas.Color, tags=["Colores"])
def update_color(
    color_id: int, color_data: schemas.ColorUpdate, db: Session = Depends(get_db)
):
    # Verificar si el color existe en la base de datos
    db_color = crud.get_color(db, color_id)
    if db_color is None:
        raise HTTPException(status_code=404, detail="Color not found")

    # Actualizar los campos del color con los datos proporcionados
    for field, value in color_data.dict().items():
        setattr(db_color, field, value)

    # Guardar los cambios en la base de datos
    db.commit()
    db.refresh(db_color)

    # Devolver el color actualizado
    return db_color


@app.delete("/colores/{color_id}", response_model=schemas.Color, tags=["Colores"])
def delete_color(color_id: int, db: Session = Depends(get_db)):
    # Verificar si el color existe en la base de datos
    db_color = crud.get_color(db, color_id)
    if db_color is None:
        raise HTTPException(status_code=404, detail="Color not found")

    # Eliminar el color de la base de datos
    crud.delete_color(db, color_id=color_id)

    # Devolver el color eliminado
    return db_color


@app.post("/import-colores/", tags=["Colores"])
def import_colores_from_json(db: Session = Depends(get_db)):
    try:
        file_path = os.path.join("front/static/", "paints.json")  # Ruta del archivo de pinturas, revisar al publicar/mover
        if not os.path.exists(file_path):
            return JSONResponse(
                status_code=404, content={"message": "paints.json no encontrado"}
            )

        with open(file_path, "r") as file:
            data = json.load(file)
            
        # Normalizar los nombres de los campos y eliminar el atributo "tipo"
        for color_data in data:
            color_data["nombre"] = color_data.pop("Nombre", None)
            color_data["marca"] = color_data.pop("Marca", None)
            color_data["codigoHex"] = color_data.pop("Hex", None)
            color_data.pop("Tipo", None)

        # Crear los objetos ColorCreate y guardarlos en la base de datos si no existen
        for color_data in data:
            existing_color = crud.get_color_by_name(db, nombre=color_data["nombre"])
            if existing_color:
                print(f"Color '{color_data['nombre']}' ya existe. Saltando.")
                continue
            color = schemas.ColorCreate(**color_data)
            crud.create_color(db=db, color=color)

        return JSONResponse(
            status_code=200, content={"message": "Datos de colores importados correctamente"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": f"Error al importar datos de colores: {e}"}
        )

@app.get("/search_colores", response_model=List[schemas.Color], tags=["Colores"])
def search_colores(search: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(models.Color)
    
    if search:
        query = query.filter(models.Color.nombre.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()


# IMAGEN
@app.post("/upload/", tags=["Imagen"])
async def upload_image(file: UploadFile = File(...)):
    try:
        # Crear carpeta si no existe
        if not os.path.exists("static/images"):
            os.makedirs("static/images")

        # Guardar la imagen en el servidor
        with open(f"front/static/images/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(
            status_code=200, content={"message": "Imagen subida correctamente"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": f"Error al subir la imagen: {e}"}
        )
