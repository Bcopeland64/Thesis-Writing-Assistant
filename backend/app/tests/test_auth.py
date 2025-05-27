from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest

from backend.app.core.config import settings
from backend.app.schemas.user import UserCreate
from backend.app.crud import crud_user
from backend.app.models.user import User as UserModel
from backend.app.tests.utils import random_email, random_lower_string

# Assuming API_V1_STR is /api/v1 or defined in settings.
# For this project, it's /api/v1 as per router prefix in main.py
API_V1_PREFIX = "/api/v1"


def test_user_registration_success(client: TestClient, db: Session):
    email = random_email()
    password = random_lower_string()
    full_name = "Test User Reg"
    
    response = client.post(
        f"{API_V1_PREFIX}/auth/register",
        json={"email": email, "password": password, "full_name": full_name},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == email
    assert data["full_name"] == full_name
    assert "id" in data
    assert "hashed_password" not in data # Ensure password is not returned

    user_in_db = crud_user.get_user_by_email(db, email=email)
    assert user_in_db is not None
    assert user_in_db.email == email

def test_user_registration_existing_email(client: TestClient, test_user: UserModel, db: Session):
    # test_user fixture already created a user with email "testuser@example.com"
    email = test_user.email
    password = random_lower_string()
    
    response = client.post(
        f"{API_V1_PREFIX}/auth/register",
        json={"email": email, "password": password, "full_name": "Another User"},
    )
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Email already registered"

def test_user_login_success(client: TestClient, test_user: UserModel):
    # test_user fixture creates user with email "testuser@example.com" and password "testpassword"
    login_data = {
        "username": test_user.email,
        "password": "testpassword",
    }
    response = client.post(f"{API_V1_PREFIX}/auth/login", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_user_login_incorrect_password(client: TestClient, test_user: UserModel):
    login_data = {
        "username": test_user.email,
        "password": "wrongpassword",
    }
    response = client.post(f"{API_V1_PREFIX}/auth/login", data=login_data)
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Incorrect email or password"

def test_user_login_nonexistent_user(client: TestClient):
    login_data = {
        "username": "nonexistent@example.com",
        "password": "anypassword",
    }
    response = client.post(f"{API_V1_PREFIX}/auth/login", data=login_data)
    assert response.status_code == 401 # Or 404, depending on how you want to signal this
    data = response.json()
    assert data["detail"] == "Incorrect email or password" # Current backend message

def test_get_current_user_me_success(authenticated_client: TestClient, test_user: UserModel):
    response = authenticated_client.get(f"{API_V1_PREFIX}/users/me")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user.email
    assert data["full_name"] == test_user.full_name
    assert data["id"] == test_user.id

def test_get_current_user_me_no_token(client: TestClient):
    response = client.get(f"{API_V1_PREFIX}/users/me")
    assert response.status_code == 401 # FastAPI's default for missing auth
    data = response.json()
    assert data["detail"] == "Not authenticated" # Default message from OAuth2PasswordBearer

def test_get_current_user_me_invalid_token(client: TestClient):
    response = client.get(
        f"{API_V1_PREFIX}/users/me",
        headers={"Authorization": "Bearer invalidtoken"},
    )
    assert response.status_code == 401
    data = response.json()
    # The detail message can vary based on JWT error (e.g. "Could not validate credentials", "Invalid token")
    # For now, we'll check that it's unauthorized. A more specific check might be needed if error messages are standardized.
    assert data["detail"] # Check that there is some detail message.
    # Example: assert data["detail"] == "Could not validate credentials" or similar from security.py's credentials_exception
    # The current credentials_exception in security.py is "Could not validate credentials"
    assert data["detail"] == "Could not validate credentials"

# To test with an expired token, one would need to:
# 1. Create a token with a very short expiry (e.g., 1 second).
# 2. Wait for it to expire.
# 3. Send the request.
# This is more involved and might be considered for more advanced testing.
# For now, an invalid token format covers a similar scenario of token rejection.
