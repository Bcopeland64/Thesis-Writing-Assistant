from utils.groq_api import call_groq

def refine_topic(topic):
    prompt = f"Help me refine this thesis topic: {topic}. Provide suggestions for narrowing the scope."
    return call_groq(prompt)

def generate_research_question(topic):
    prompt = f"Generate a clear research question or hypothesis for this topic: {topic}."
    return call_groq(prompt)