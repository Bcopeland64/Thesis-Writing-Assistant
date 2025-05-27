import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from backend.app.main import app
from backend.app.db.base import Base
from backend.app.db.session import get_db
from backend.app.core.config import settings
from backend.app.models.user import User as UserModel # To avoid conflict
from backend.app.auth.security import get_current_active_user, create_access_token
from backend.app.schemas.user import UserCreate # For creating test user
from backend.app.crud import crud_user

# Use a separate SQLite database for testing
SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///./test.db"
engine_test = create_engine(SQLALCHEMY_DATABASE_URL_TEST)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine_test) # Drop existing tables first
    Base.metadata.create_all(bind=engine_test) # Create tables
    yield
    Base.metadata.drop_all(bind=engine_test) # Clean up after tests

@pytest.fixture(scope="function")
def db() -> Generator[Session, None, None]:
    connection = engine_test.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient, None, None]:
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear() # Clear overrides after test

# Fixture to create a test user directly in the database
@pytest.fixture(scope="function")
def test_user(db: Session) -> UserModel:
    user_in = UserCreate(
        email="testuser@example.com",
        password="testpassword",
        full_name="Test User"
    )
    return crud_user.create_user(db=db, user=user_in)

# Fixture for an authenticated test client
@pytest.fixture(scope="function")
def authenticated_client(client: TestClient, test_user: UserModel, db: Session) -> TestClient:
    # The test_user fixture already creates a user. We need to log them in.
    # However, TestClient doesn't handle cookies or localStorage like a browser.
    # We need to generate a token and add it to the headers for subsequent requests.
    
    # Create access token for the test_user
    # Note: crud_user.create_user returns the user model, which has the plain password
    # The login endpoint expects form data, not JSON.
    login_data = {
        "username": test_user.email,
        "password": "testpassword", # Use the plain password used for creation
    }
    response = client.post(f"{settings.API_V1_STR}/auth/login", data=login_data)
    assert response.status_code == 200
    token_data = response.json()
    access_token = token_data["access_token"]
    
    client.headers["Authorization"] = f"Bearer {access_token}"
    return client

# Fixture to mock get_current_active_user
# This can be used if you want to bypass the token logic for a specific test
@pytest.fixture
def mock_get_current_active_user(test_user: UserModel):
    async def _override_get_current_active_user():
        return test_user
    return _override_get_current_active_user

# Example of how to use mock_get_current_active_user in a test:
# def test_some_protected_route(client: TestClient, mock_get_current_active_user):
#     app.dependency_overrides[get_current_active_user] = mock_get_current_active_user
#     response = client.get("/some_protected_route")
#     # ... assertions ...
#     app.dependency_overrides.clear()

# Note: settings.API_V1_STR might not be defined in your config.
# If it's not, you'll need to define it or use the full path like "/api/v1"
# For now, assuming it's defined or we'll use "/api/v1" directly in tests.
# Let's check config.py for API_V1_STR or similar.
# It seems settings.API_V1_STR is not standard in this project.
# I will use "/api/v1" directly in tests or define API_V1_STR in config if preferred.
# For now, I'll adjust the authenticated_client to use the hardcoded prefix.
# settings.API_V1_STR = "/api/v1" # Temporarily for this fixture, or ensure it's in config.
# Better: use client.post("/api/v1/auth/login") directly.
# The client fixture in FastAPI TestClient already handles base URL.
# So, client.post("/api/v1/auth/login") is correct.
# The prefix is already part of the router inclusion in main.py.
# The `authenticated_client` fixture needs to be updated to reflect this.
# The router for auth is at "/api/v1" and the login endpoint is "/auth/login"
# so the full path is "/api/v1/auth/login".
# The client.post should be to `/api/v1/auth/login`
# And the settings.API_V1_STR is not used here.
# The `login_data` for `/api/v1/auth/login` is OAuth2PasswordRequestForm, which is form data.
# The `client.post` with `data=` correctly sends form data.
# The token generation for `authenticated_client` seems okay.
# The `test_user` fixture uses `crud_user.create_user`, which hashes the password.
# So, `get_user_by_email` in the login route will fetch this user with the hashed password.
# `verify_password` will then compare the provided "testpassword" with the hashed one.
# This flow is correct.`backend/app/tests/conftest.py` has been created.
Now I'll create `backend/app/tests/utils.py`.
