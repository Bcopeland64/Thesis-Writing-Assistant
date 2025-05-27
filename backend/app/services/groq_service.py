import requests
from fastapi import HTTPException, status
from backend.app.core.config import settings # Import settings

# Use the correct Groq API endpoint
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Placeholder for a more specific Groq API error
class GroqAPIError(Exception):
    pass

def call_groq(prompt: str, max_tokens: int = 100, temperature: float = 0.7) -> str:
    if not settings.GROQ_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="GROQ_API_KEY not configured",
        )

    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Or make this configurable via settings or params
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=30) # Added timeout
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX or 5XX)

        response_data = response.json()
        content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            # Handle cases where content might be empty or not in expected structure
            raise GroqAPIError("Empty or malformed response from Groq API")
        return content

    except requests.exceptions.RequestException as e:
        # Handle network errors, timeout, etc.
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error connecting to Groq API: {e}",
        )
    except GroqAPIError as e:
        # Handle specific API errors (e.g., empty content)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Groq API error: {e}",
        )
    except Exception as e:
        # Catch any other unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred with Groq API: {e}",
        )