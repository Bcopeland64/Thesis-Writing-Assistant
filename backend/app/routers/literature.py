import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.schemas.user import User as UserSchema # Renamed to avoid conflict with models.User
from backend.app.auth.security import get_current_active_user
from backend.app.services import literature_service
from backend.app.models.user import User as UserModel # For type hinting current_user

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/search", response_model=str) # Assuming the service returns a string for now
async def search_literature_endpoint(
    query: str = Query(..., min_length=3, description="Query to search for literature"),
    current_user: UserModel = Depends(get_current_active_user)
):
    try:
        results = literature_service.search_literature(query=query)
        if results == "Literature search is unavailable because the API key is not configured by the administrator.":
            raise HTTPException(status_code=412, detail=results)
        return results
    except ValueError as e: # Catching specific errors from the service
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException as e: # Propagating HTTPExceptions from groq_service
        raise e
    except Exception as e: # Catch-all for other unexpected errors
        logger.error(f"Unexpected error in search_literature_endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred during literature search.")


@router.get("/summarize", response_model=str) # Assuming the service returns a string
async def summarize_paper_endpoint(
    paper_title: str = Query(..., min_length=3, description="Title of the paper to summarize"),
    current_user: UserModel = Depends(get_current_active_user)
):
    try:
        summary = literature_service.summarize_paper(paper_title=paper_title)
        if summary == "Paper summarization is unavailable because the API key is not configured by the administrator.":
            raise HTTPException(status_code=412, detail=summary)
        return summary
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in summarize_paper_endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred during paper summarization.")

# Remove the test endpoint if no longer needed, or keep for testing
# @router.get("/test-literature")
# async def test_literature_endpoint(current_user: UserModel = Depends(get_current_active_user)):
#     return {"message": "Literature router is active", "user": current_user.email}
