# utils/literature_review.py
from utils.groq_api import call_groq

def search_literature(query):
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    prompt = f"""
    Recommend 5 highly relevant academic papers for this query: {query}.
    For each paper, include:
    - Title, Authors, Publication Year
    - A brief summary of its contribution to the field
    - Relevance score (High, Medium, Low)
    - Open-access alternatives if the paper is behind a paywall
    """
    return call_groq(prompt)

def summarize_paper(paper_title):
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
    return call_groq(prompt)