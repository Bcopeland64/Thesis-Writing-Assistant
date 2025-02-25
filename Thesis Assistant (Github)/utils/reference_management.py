# utils/reference_management.py
from utils.groq_api import call_groq

def generate_citation(title, author, year, style="apa"):
    if not title.strip() or not author.strip() or not year.strip():
        raise ValueError("Title, author, and year cannot be empty.")
    prompt = f"""
    Generate a citation for this source in {style.upper()} format:
    Title: {title}, Author: {author}, Year: {year}.
    Suggest citation management tools (e.g., Zotero, Mendeley).
    """
    return call_groq(prompt)

def detect_missing_references(text):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    prompt = f"""
    Analyze this text and detect any missing references or citations: {text}.
    Suggest potential sources to fill the gaps.
    Deduplicate redundant citations and suggest citation style conversions (APA, MLA, Chicago, IEEE).
    """
    return call_groq(prompt)