# utils/reference_management.py
from backend.app.services.groq_service import call_groq_async

async def generate_citation(title, author, year, style="apa"):
    if not title.strip() or not author.strip() or not year.strip():
        raise ValueError("Title, author, and year cannot be empty.")
    prompt = f"""
    Generate a citation for this source in {style.upper()} format:
    Title: {title}, Author: {author}, Year: {year}.
    Suggest citation management tools (e.g., Zotero, Mendeley).
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Citation generation is unavailable because the API key is not configured by the administrator."
    return result

async def detect_missing_references(text):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    prompt = f"""
    Analyze this text and detect any missing references or citations: {text}.
    Suggest potential sources to fill the gaps.
    Deduplicate redundant citations and suggest citation style conversions (APA, MLA, Chicago, IEEE).
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        # Using a generic message as this function is also related to references
        return "Reference management features are unavailable because the API key is not configured by the administrator."
    return result