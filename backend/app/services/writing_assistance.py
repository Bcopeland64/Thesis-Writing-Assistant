# utils/writing_assistance.py
from backend.app.services.groq_service import call_groq_async

async def improve_writing(text, tone="academic", audience="academic"):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    prompt = f"""
    Improve the clarity, coherence, and academic tone of this text: {text}.
    Adjust the tone to be {tone} (options: academic, formal, conversational, persuasive).
    Optimize the text for an {audience} audience (options: academic, general).
    Check for plagiarism and suggest rephrasing if necessary.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Writing improvement is unavailable because the API key is not configured by the administrator."
    return result

async def check_logical_flow(text):
    if not text.strip():
        raise ValueError("Text cannot be empty.")
    prompt = f"""
    Check the logical flow and argument strength of this text: {text}.
    Provide detailed feedback on how to improve transitions between paragraphs.
    Highlight areas where arguments can be strengthened with evidence or examples.
    Suggest SEO optimization tips if the text is intended for online publication.
    """
    result = await call_groq_async(prompt)
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Logical flow checking is unavailable because the API key is not configured by the administrator."
    return result