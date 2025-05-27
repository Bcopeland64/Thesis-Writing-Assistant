from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.schemas.user import User as UserSchema # Renamed to avoid conflict with models.User
from backend.app.auth.security import get_current_active_user
from backend.app.services import literature_service
from backend.app.models.user import User as UserModel # For type hinting current_user

router = APIRouter()

@router.get("/search", response_model=str) # Assuming the service returns a string for now
async def search_literature_endpoint(
    query: str = Query(..., min_length=3, description="Query to search for literature"),
    current_user: UserModel = Depends(get_current_active_user)
):
    try:
        results = literature_service.search_literature(query=query)
        return results
    except ValueError as e: # Catching specific errors from the service
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException as e: # Propagating HTTPExceptions from groq_service
        raise e
    except Exception as e: # Catch-all for other unexpected errors
        # Log the error e for debugging
        raise HTTPException(status_code=500, detail="An unexpected error occurred during literature search.")


@router.get("/summarize", response_model=str) # Assuming the service returns a string
async def summarize_paper_endpoint(
    paper_title: str = Query(..., min_length=3, description="Title of the paper to summarize"),
    current_user: UserModel = Depends(get_current_active_user)
):
    try:
        summary = literature_service.summarize_paper(paper_title=paper_title)
        return summary
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        # Log the error e for debugging
        raise HTTPException(status_code=500, detail="An unexpected error occurred during paper summarization.")

# Remove the test endpoint if no longer needed, or keep for testing
# @router.get("/test-literature")
# async def test_literature_endpoint(current_user: UserModel = Depends(get_current_active_user)):
#     return {"message": "Literature router is active", "user": current_user.email}
