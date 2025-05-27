# utils/methodology_guidance.py
from utils.groq_api import call_groq

def suggest_methodology(research_question):
    if not research_question.strip():
        raise ValueError("Research question cannot be empty.")
    prompt = f"""
    Suggest a suitable research methodology for this research question: {research_question}.
    Justify the choice and provide examples of similar studies using the same methodology.
    Highlight ethical considerations for this methodology.
    Suggest software/tools for implementing the methodology.
    """
    return call_groq(prompt)

def suggest_data_collection(methodology):
    if not methodology.strip():
        raise ValueError("Methodology cannot be empty.")
    prompt = f"""
    Suggest data collection techniques for this methodology: {methodology}.
    Include tools or software recommendations for implementation.
    Suggest data validation techniques to ensure reliability.
    """
    return call_groq(prompt)