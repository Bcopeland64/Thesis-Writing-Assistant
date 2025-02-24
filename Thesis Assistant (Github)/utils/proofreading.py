from utils.groq_api import call_groq

def proofread(text):
    prompt = f"Proofread this text for grammar, spelling, and punctuation errors: {text}. Suggest improvements."
    return call_groq(prompt)