# utils/thesis_structure.py
from utils.groq_api import call_groq

def generate_outline(format_style="apa"):
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
    return call_groq(prompt)