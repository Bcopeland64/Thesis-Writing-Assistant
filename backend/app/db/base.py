from backend.app.db.base_class import Base # Will create base_class.py next
from backend.app.models.user import User # Ensure User model is imported

# Potentially other models will be imported here as well

# Function to create database tables
# from backend.app.db.session import engine # This will be used in main.py for startup event

# def init_db():
#     Base.metadata.create_all(bind=engine)
