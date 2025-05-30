# utils/proofreading.py
from backend.app.services.groq_service import call_groq_async

async def proofread(text):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    prompt = f"""
    Proofread this text for grammar, spelling, and punctuation errors: {text}.
    Suggest improvements for clarity and precision.
    Identify overused words and suggest alternatives.
    Highlight idiomatic expressions that may confuse non-native speakers.
    Detect cultural biases in language usage and suggest neutral alternatives.
    Provide a readability score (Flesch-Kincaid Grade Level).
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Proofreading is unavailable because the API key is not configured by the administrator."
    return result