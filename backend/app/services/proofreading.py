# utils/proofreading.py
from utils.groq_api import call_groq

def proofread(text):
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
    return call_groq(prompt)