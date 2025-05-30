# utils/methodology_guidance.py
from backend.app.services.groq_service import call_groq_async

async def suggest_methodology(research_question):
    if not research_question.strip():
        raise ValueError("Research question cannot be empty.")
    prompt = f"""
    Suggest a suitable research methodology for this research question: {research_question}.
    Justify the choice and provide examples of similar studies using the same methodology.
    Highlight ethical considerations for this methodology.
    Suggest software/tools for implementing the methodology.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Methodology suggestion is unavailable because the API key is not configured by the administrator."
    return result

async def suggest_data_collection(methodology):
    if not methodology.strip():
        raise ValueError("Methodology cannot be empty.")
    prompt = f"""
    Suggest data collection techniques for this methodology: {methodology}.
    Include tools or software recommendations for implementation.
    Suggest data validation techniques to ensure reliability.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Data collection suggestion is unavailable because the API key is not configured by the administrator."
    return result