# utils/defense_preparation.py
from backend.app.services.groq_service import call_groq_async

async def get_defense_questions():
    prompt = """
    Provide 5 common thesis defense questions and their follow-up questions.
    Include tips for answering each question confidently.
    Suggest stress management techniques for handling nerves during the defense.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Defense question suggestions are unavailable because the API key is not configured by the administrator."
    return result

async def prepare_responses(response_text):
    if not response_text.strip():
        raise ValueError("Response text cannot be empty.")
    prompt = f"""
    Prepare a polished response to this defense question: {response_text}.
    Include strategies for staying calm and confident during the defense.
    Provide body language tips for confident delivery (e.g., posture, eye contact).
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Defense response preparation is unavailable because the API key is not configured by the administrator."
    return result