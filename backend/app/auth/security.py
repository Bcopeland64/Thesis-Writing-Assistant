from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from backend.app.core.config import settings # Assuming settings will be in core.config
from backend.app.schemas.user import TokenData
from backend.app.models.user import User # To type hint current_user

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Will be defined in routers.auth
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") # Relative to /api/v1 if router is prefixed

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES will be in settings.py, default to 30 if not set
# SECRET_KEY will be in settings.py


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

from sqlalchemy.orm import Session
from backend.app.db.session import get_db # Import get_db
from backend.app.crud import crud_user # Import crud_user
from backend.app.schemas import user as schemas_user # Import user schemas

# Import oauth2_scheme from auth router
# This creates a circular dependency if auth.router also imports from security.
# Consider moving oauth2_scheme to a more central place or passing it.
# For now, let's assume it will be resolved by how modules are loaded or by refactoring later.
# Import oauth2_scheme from auth router
from backend.app.routers.auth import oauth2_scheme # This should work if router.auth doesn't import security.get_current_user directly at module level


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme) # oauth2_scheme will be resolved at runtime
) -> User: # Use User model for type hint
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email) # Use TokenData schema
    except JWTError:
        raise credentials_exception
    user = crud_user.get_user_by_email(db, email=token_data.email) # Use crud_user
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user), # Use User model
) -> User: # Use User model
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user
