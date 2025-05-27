import os
from typing import Optional # Import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Thesis Assistant API"
    PROJECT_VERSION: str = "1.0.0"

    # Database
    # SQLALCHEMY_DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    # Forcing SQLite for now as per instructions for simplicity
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"


    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key_that_should_be_in_env_file") # Replace with a strong key
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # Groq API Key
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")

settings = Settings()
