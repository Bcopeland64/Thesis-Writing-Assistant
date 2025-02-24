# utils/methodology_guidance.py

def suggest_methodology(research_question):
    """
    Suggests a suitable research methodology based on the research question.
    """
    if "quantitative" in research_question.lower() or "statistical" in research_question.lower():
        return "Quantitative Methodology: Use surveys, experiments, or statistical analysis."
    elif "qualitative" in research_question.lower() or "interview" in research_question.lower():
        return "Qualitative Methodology: Use interviews, case studies, or thematic analysis."
    else:
        return "Mixed Methods: Combine both qualitative and quantitative approaches for comprehensive insights."

def suggest_data_collection(methodology):
    """
    Suggests data collection techniques based on the chosen methodology.
    """
    if "quantitative" in methodology.lower():
        return "Data Collection Techniques: Surveys, Experiments, Observations, or Secondary Data Analysis."
    elif "qualitative" in methodology.lower():
        return "Data Collection Techniques: Interviews, Focus Groups, Case Studies, or Document Analysis."
    else:
        return "Data Collection Techniques: Combine surveys/interviews with observations or document analysis."
