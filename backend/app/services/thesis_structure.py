# utils/thesis_structure.py
from backend.app.services.groq_service import call_groq_async

async def generate_outline(format_style="apa"):
    supported_styles = ["APA", "MLA", "Chicago", "IEEE"]
    if format_style not in supported_styles:
        raise ValueError(f"Unsupported format style: {format_style}. Choose from {supported_styles}.")
    prompt = f"""
    Generate a detailed thesis outline in {format_style.upper()} format.
    Include chapter-specific writing tips and templates for each section.
    Provide word count estimations for each section.
    Include checklists for completing each chapter.
    Suggest submission guidelines for different universities.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Thesis outline generation is unavailable because the API key is not configured by the administrator."
    return result