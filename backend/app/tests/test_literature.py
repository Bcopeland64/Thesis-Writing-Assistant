import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from backend.app.models.user import User as UserModel # For type hinting
from backend.app.core.config import settings

# Assuming API_V1_STR is /api/v1 or defined in settings.
# For this project, it's /api/v1 as per router prefix in main.py
API_V1_LITERATURE_PREFIX = "/api/v1/literature"

# Test successful search
def test_search_literature_success(authenticated_client: TestClient, test_user: UserModel):
    with patch("backend.app.services.literature_service.call_groq") as mock_call_groq:
        mock_call_groq.return_value = "Mocked search results"
        
        response = authenticated_client.get(
            f"{API_V1_LITERATURE_PREFIX}/search",
            params={"query": "test query"}
        )
        assert response.status_code == 200
        assert response.json() == "Mocked search results"
        mock_call_groq.assert_called_once()
        # You can add more specific checks for the prompt passed to call_groq if needed

def test_search_literature_not_authenticated(client: TestClient):
    response = client.get(
        f"{API_V1_LITERATURE_PREFIX}/search",
        params={"query": "test query"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

def test_search_literature_empty_query(authenticated_client: TestClient):
    # The service layer literature_service.search_literature raises ValueError for empty query.
    # The router converts this to a 400 HTTPException.
    # No need to mock call_groq here as it shouldn't be reached.
    response = authenticated_client.get(
        f"{API_V1_LITERATURE_PREFIX}/search",
        params={"query": " "} # Empty or whitespace query
    )
    assert response.status_code == 400
    # The detail message comes from the ValueError in literature_service.py
    assert "Query cannot be empty" in response.json()["detail"]


def test_search_literature_groq_fails(authenticated_client: TestClient):
    with patch("backend.app.services.literature_service.call_groq") as mock_call_groq:
        # Simulate an HTTPException raised by groq_service.call_groq
        from fastapi import HTTPException
        mock_call_groq.side_effect = HTTPException(status_code=503, detail="Groq service unavailable")
        
        response = authenticated_client.get(
            f"{API_V1_LITERATURE_PREFIX}/search",
            params={"query": "test query for failure"}
        )
        assert response.status_code == 503
        assert response.json()["detail"] == "Groq service unavailable"

# Test successful summarization
def test_summarize_paper_success(authenticated_client: TestClient, test_user: UserModel):
    with patch("backend.app.services.literature_service.call_groq") as mock_call_groq:
        mock_call_groq.return_value = "Mocked paper summary"
        
        response = authenticated_client.get(
            f"{API_V1_LITERATURE_PREFIX}/summarize",
            params={"paper_title": "test paper title"}
        )
        assert response.status_code == 200
        assert response.json() == "Mocked paper summary"
        mock_call_groq.assert_called_once()

def test_summarize_paper_not_authenticated(client: TestClient):
    response = client.get(
        f"{API_V1_LITERATURE_PREFIX}/summarize",
        params={"paper_title": "test paper title"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

def test_summarize_paper_empty_title(authenticated_client: TestClient):
    response = authenticated_client.get(
        f"{API_V1_LITERATURE_PREFIX}/summarize",
        params={"paper_title": " "} # Empty or whitespace title
    )
    assert response.status_code == 400
    assert "Paper title cannot be empty" in response.json()["detail"]


def test_summarize_paper_groq_fails(authenticated_client: TestClient):
    with patch("backend.app.services.literature_service.call_groq") as mock_call_groq:
        from fastapi import HTTPException
        mock_call_groq.side_effect = HTTPException(status_code=500, detail="Groq internal error")
        
        response = authenticated_client.get(
            f"{API_V1_LITERATURE_PREFIX}/summarize",
            params={"paper_title": "test paper for failure"}
        )
        assert response.status_code == 500
        assert response.json()["detail"] == "Groq internal error"
