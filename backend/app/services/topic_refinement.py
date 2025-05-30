# utils/topic_refinement.py
from backend.app.services.groq_service import call_groq_async

async def refine_topic(topic):
    prompt = f"""
    Help me refine this thesis topic: {topic}.
    Provide 3-5 suggestions for narrowing the scope, along with potential keywords to focus on.
    Suggest interdisciplinary connections to broaden the scope of the research.
    Identify trending topics or gaps in the field related to this topic.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Topic refinement is unavailable because the API key is not configured by the administrator."
    return result

async def generate_research_question(topic):
    prompt = f"""
    Generate a clear and concise research question or hypothesis for this topic: {topic}.
    Include alternative phrasing options and explain why each is effective.
    Suggest potential collaborators or institutions working on similar topics.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Research question generation is unavailable because the API key is not configured by the administrator."
    return result