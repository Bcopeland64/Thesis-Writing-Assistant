from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from backend.app.routers import auth as auth_router
from backend.app.routers import literature as literature_router
from backend.app.db.session import engine
from backend.app.db.base import Base
# Ensure User model is discoverable by Base.metadata for table creation
# This is typically done by importing the model module(s) where Base is used.
# For example, in backend/app/db/base.py we have `from backend.app.models.user import User`
# which makes User model part of Base.metadata

# Function to create DB tables
def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI(title="Thesis Assistant API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if your frontend runs on a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth_router.router, prefix="/api/v1", tags=["auth"])
app.include_router(literature_router.router, prefix="/api/v1/literature", tags=["literature"]) # Include the literature router

@app.get("/")
async def root():
    return {"message": "Welcome to Thesis Assistant API"}
