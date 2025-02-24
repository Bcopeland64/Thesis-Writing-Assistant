from utils.groq_api import call_groq

def improve_writing(text):
    prompt = f"Improve the clarity, coherence, and academic tone of this text: {text}."
    return call_groq(prompt)

def check_logical_flow(text):
    prompt = f"Check the logical flow and argument strength of this text: {text}. Provide suggestions for improvement."
    return call_groq(prompt)