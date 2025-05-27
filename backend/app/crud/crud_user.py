from sqlalchemy.orm import Session
from backend.app.models import user as models_user
from backend.app.schemas import user as schemas_user
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models_user.User).filter(models_user.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models_user.User).filter(models_user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models_user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas_user.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models_user.User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_obj: models_user.User, obj_in: schemas_user.UserUpdate):
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    
    if "password" in update_data and update_data["password"]:
        hashed_password = pwd_context.hash(update_data["password"])
        del update_data["password"] # remove plain password
        update_data["hashed_password"] = hashed_password # add hashed password
        
    for field, value in update_data.items():
        setattr(db_obj, field, value)
        
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_user(db: Session, user_id: int):
    db_user = db.query(models_user.User).filter(models_user.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
