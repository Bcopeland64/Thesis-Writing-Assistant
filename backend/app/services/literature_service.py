# services/literature_service.py
from backend.app.services.groq_service import call_groq_async
from fastapi import HTTPException # For propagating errors if needed

async def search_literature(query: str): # Added type hint
    if not query.strip():
        # This could also be an HTTPException if called directly from a route handler
        # For a service layer, ValueError is often fine, to be caught by the router.
        raise ValueError("Query cannot be empty.")
    prompt = f"""
    Recommend 5 highly relevant academic papers for this query: {query}.
    For each paper, include:
    - Title, Authors, Publication Year
    - A brief summary of its contribution to the field
    - Relevance score (High, Medium, Low)
    - Open-access alternatives if the paper is behind a paywall
    """
    # Errors from call_groq (HTTPExceptions) will propagate up
    result = await call_groq_async(prompt, max_tokens=500) # Increased max_tokens for detailed search results
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Literature search is unavailable because the API key is not configured by the administrator."
    return result

async def summarize_paper(paper_title: str): # Added type hint
    if not paper_title.strip():
        raise ValueError("Paper title cannot be empty.")
    prompt = f"""
    Analyze the paper titled "{paper_title}" and provide the following details in a structured format:
    1. Source Information (Title, Authors, Publication Year)
    2. Research Question or Hypothesis
    3. Methodology
    4. Population and Sample
    5. Data Collection and Analysis
    6. Findings and Results
    7. Discussion and Conclusion
    8. References and Citations (extract key references)
    9. Overall Quality and Relevance
    10. Potential Biases and Limitations
    11. Future Research Directions
    12. Contribution to the Field
    13. Sentiment Analysis of the Paper's Tone (Positive, Neutral, Critical)
    """
    # Errors from call_groq (HTTPExceptions) will propagate up
    result = await call_groq_async(prompt, max_tokens=1000) # Increased max_tokens for detailed summary
    if result == "GROQ_API_KEY_NOT_CONFIGURED":
        return "Paper summarization is unavailable because the API key is not configured by the administrator."
    return result