# utils/presentation_preparation.py
from utils.groq_api import call_groq

def create_presentation_outline(topic):
    if not topic.strip():
        raise ValueError("Topic cannot be empty.")
    prompt = f"""
    Create a detailed presentation outline for this topic: {topic}.
    Include slide-by-slide content suggestions and design tips for visual appeal.
    Suggest audience engagement strategies (e.g., storytelling, Q&A prompts).
    Provide templates for slide designs (minimalistic, infographic-style).
    """
    return call_groq(prompt)