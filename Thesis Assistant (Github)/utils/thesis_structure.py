# utils/thesis_structure.py

def generate_outline(format_style="apa"):
    """
    Generates a thesis outline based on the selected format style (APA, MLA, Chicago, IEEE).
    """
    if format_style.lower() == "apa":
        return """APA Thesis Outline:
        1. Title Page
        2. Abstract
        3. Table of Contents
        4. Introduction
        5. Literature Review
        6. Methodology
        7. Results
        8. Discussion
        9. Conclusion
        10. References
        11. Appendices"""
    
    elif format_style.lower() == "mla":
        return """MLA Thesis Outline:
        1. Title Page
        2. Abstract
        3. Table of Contents
        4. Introduction
        5. Background and Context
        6. Research Methodology
        7. Findings
        8. Analysis
        9. Conclusion
        10. Works Cited
        11. Appendices"""
    
    elif format_style.lower() == "chicago":
        return """Chicago Thesis Outline:
        1. Title Page
        2. Abstract
        3. Table of Contents
        4. Introduction
        5. Literature Review
        6. Research Design and Methodology
        7. Results and Analysis
        8. Discussion
        9. Conclusion
        10. Bibliography
        11. Appendices"""
    
    elif format_style.lower() == "ieee":
        return """IEEE Thesis Outline:
        1. Title Page
        2. Abstract
        3. Keywords
        4. Introduction
        5. Related Work
        6. Methodology
        7. Results and Discussion
        8. Conclusion
        9. References
        10. Appendices"""
    
    else:
        return "Unsupported format style. Please choose from APA, MLA, Chicago, or IEEE."
