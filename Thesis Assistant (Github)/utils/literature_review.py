# utils/literature_review.py
from utils.groq_api import call_groq

def search_literature(query):
    """
    Searches for relevant academic papers based on the query.
    """
    prompt = f"Recommend 3-5 relevant academic papers for this query: {query}. Provide their titles and authors."
    return call_groq(prompt)

def summarize_paper(paper_title):
    """
    Summarizes a specific paper by extracting key components.
    """
    prompt = f"""
    Analyze the paper titled "{paper_title}" and provide the following details in a structured format:
    1. Source Information (Title, Authors, Publication Year)
    2. Research Question or Hypothesis
    3. Methodology
    4. Population and Sample
    5. Data Collection and Analysis
    6. Findings and Results
    7. Discussion and Conclusion
    8. References and Citations
    9. Overall Quality and Relevance
    10. Potential Biases and Limitations
    11. Future Research Directions
    """
    return call_groq(prompt)
