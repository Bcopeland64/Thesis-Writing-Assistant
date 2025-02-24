# utils/presentation_preparation.py
def create_presentation_outline(topic):
    outline = [
        "Introduction",
        "Background and Literature Review",
        "Research Methodology",
        "Results and Analysis",
        "Conclusion and Future Work"
    ]
    return f"Outline for {topic}:\n- " + "\n- ".join(outline)