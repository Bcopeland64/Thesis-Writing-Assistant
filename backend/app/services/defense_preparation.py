# utils/defense_preparation.py
from utils.groq_api import call_groq

def get_defense_questions():
    prompt = """
    Provide 5 common thesis defense questions and their follow-up questions.
    Include tips for answering each question confidently.
    Suggest stress management techniques for handling nerves during the defense.
    """
    return call_groq(prompt)

def prepare_responses(response_text):
    if not response_text.strip():
        raise ValueError("Response text cannot be empty.")
    prompt = f"""
    Prepare a polished response to this defense question: {response_text}.
    Include strategies for staying calm and confident during the defense.
    Provide body language tips for confident delivery (e.g., posture, eye contact).
    """
    return call_groq(prompt)