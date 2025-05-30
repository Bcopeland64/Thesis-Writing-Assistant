import httpx
from fastapi import HTTPException, status
from backend.app.core.config import settings

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class GroqAPIError(Exception):
    pass

async def call_groq_async(prompt: str, max_tokens: int = 100, temperature: float = 0.7) -> str:
    if not settings.GROQ_API_KEY:
        return "GROQ_API_KEY_NOT_CONFIGURED"

    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(GROQ_API_URL, headers=headers, json=data, timeout=30)
            response.raise_for_status()  # Raises httpx.HTTPStatusError for bad responses (4XX or 5XX)
            response_data = response.json() # Moved inside the block

        content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise GroqAPIError("Empty or malformed response from Groq API")
        return content

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Groq API request failed with status {e.response.status_code}: {e.response.text}",
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error connecting to Groq API: {e}",
        )
    except GroqAPIError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Groq API error: {e}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred with Groq API: {e}",
        )