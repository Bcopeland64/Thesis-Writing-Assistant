# utils/presentation_preparation.py
from backend.app.services.groq_service import call_groq_async

async def create_presentation_outline(topic):
    if not topic.strip():
        raise ValueError("Topic cannot be empty.")
    prompt = f"""
    Create a detailed presentation outline for this topic: {topic}.
    Include slide-by-slide content suggestions and design tips for visual appeal.
    Suggest audience engagement strategies (e.g., storytelling, Q&A prompts).
    Provide templates for slide designs (minimalistic, infographic-style).
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Presentation outline generation is unavailable because the API key is not configured by the administrator."
    return result