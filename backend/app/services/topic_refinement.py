# utils/topic_refinement.py
from utils.groq_api import call_groq

def refine_topic(topic):
    prompt = f"""
    Help me refine this thesis topic: {topic}.
    Provide 3-5 suggestions for narrowing the scope, along with potential keywords to focus on.
    Suggest interdisciplinary connections to broaden the scope of the research.
    Identify trending topics or gaps in the field related to this topic.
    """
    return call_groq(prompt)

def generate_research_question(topic):
    prompt = f"""
    Generate a clear and concise research question or hypothesis for this topic: {topic}.
    Include alternative phrasing options and explain why each is effective.
    Suggest potential collaborators or institutions working on similar topics.
    """
    return call_groq(prompt)