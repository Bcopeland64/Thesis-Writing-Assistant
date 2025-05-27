import random
import string

from backend.app.schemas.user import UserCreate

def random_lower_string(length: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))

def random_email() -> str:
    return f"{random_lower_string(length=10)}@{random_lower_string(length=5)}.com"

def get_random_user_create_data() -> UserCreate:
    email = random_email()
    password = random_lower_string(length=12)
    full_name = random_lower_string(length=10).capitalize()
    return UserCreate(email=email, password=password, full_name=full_name)

# Example for generating headers with a token
def get_auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}
