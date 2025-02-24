from utils.groq_api import call_groq

def search_literature(query):
    prompt = f"Recommend relevant academic papers and sources for this query: {query}."
    return call_groq(prompt)

def summarize_paper(paper_title):
    prompt = f"Summarize the key findings of this paper: {paper_title}."
    return call_groq(prompt)