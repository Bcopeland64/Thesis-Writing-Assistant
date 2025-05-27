from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app import schemas, models # Assuming __init__.py in app will expose these
from backend.app.crud import crud_user
from backend.app.auth import security
from backend.app.db.session import get_db # To be created
from backend.app.core.config import settings # To be created

router = APIRouter()

# This should be defined here and security.py should import it, or it should be passed around.
# For now, define it here. security.py's get_current_user will need this.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") # Corrected tokenUrl

@router.post("/auth/register", response_model=schemas.user.User)
def register_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    created_user = crud_user.create_user(db=db, user=user)
    return created_user

@router.post("/auth/login", response_model=schemas.user.Token)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud_user.get_user_by_email(db, email=form_data.username) # OAuth2 uses username for email
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(
        data={"sub": user.email} # "sub" is standard for subject (user identifier)
    )
    return {"access_token": access_token, "token_type": "bearer"}

from backend.app.models import user as models_user # Import User model for response_model type hint

# Ensure get_current_active_user is imported correctly
# If security.py imports oauth2_scheme from this file, and this file imports
# security.get_current_active_user, this creates a circular dependency.
# This is often resolved by Python's import system if one of the imports is inside a function
# or if the imported objects are not used at the module level initialization.
# `Depends(security.get_current_active_user)` should be fine as it's resolved at request time.

@router.get("/users/me", response_model=schemas.user.User)
async def read_users_me(current_user: models_user.User = Depends(security.get_current_active_user)):
    return current_user
