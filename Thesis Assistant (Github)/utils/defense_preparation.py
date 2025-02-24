# utils/defense_preparation.py
def get_defense_questions():
    questions = [
        "What is the main contribution of your research?",
        "How does your work compare to existing literature?",
        "What are the limitations of your study?"
    ]
    return "\n- ".join(questions)

def prepare_responses(text):
    return f"Here’s how you can respond: {text}"