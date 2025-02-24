# main.py
import streamlit as st
from utils.topic_refinement import refine_topic, generate_research_question
from utils.literature_review import search_literature, summarize_paper
from utils.writing_assistance import improve_writing, check_logical_flow
from utils.proofreading import proofread
from utils.time_management import create_timeline
from utils.reference_management import generate_citation
from utils.presentation_preparation import create_presentation_outline
from utils.data_visualization import plot_data
from utils.defense_preparation import get_defense_questions, prepare_responses

# Custom CSS for styling
st.markdown("""
<style>
    .sidebar .stRadio > div {
        margin-bottom: 15px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4285F4; /* Blue button */
        color: white;
        font-size: 18px;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 style='text-align: center; color: #4285F4;'>Thesis Assistant Platform</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your all-in-one tool for thesis research and writing.</p>", unsafe_allow_html=True)

# Sidebar Navigation with Radio Buttons
st.sidebar.title("Select a Feature")
feature = st.sidebar.radio(
    "Choose a Feature",
    [
        "Topic Refinement",
        "Literature Review",
        "Writing Assistance",
        "Proofreading",
        "Time Management",
        "Presentation Preparation",
        "Defense Preparation"
    ],
    key="feature_selection"
)

# Main Page Content
st.header(f"{feature}")

# Input Fields Based on Selected Feature
if feature == "Topic Refinement":
    topic = st.text_input("Enter your thesis topic:")
    task = st.radio("Task", ["Refine Topic", "Generate Research Question"])

elif feature == "Literature Review":
    query = st.text_input("Enter a keyword for literature search:")
    paper_title = st.text_input("Enter a paper title to summarize:")
    task = st.radio("Task", ["Search Literature", "Summarize Paper"])

elif feature == "Writing Assistance":
    text = st.text_area("Enter text for writing assistance:")
    task = st.radio("Task", ["Improve Writing", "Check Logical Flow"])

elif feature == "Proofreading":
    text = st.text_area("Enter text for proofreading:")
    task = "Proofread Text"

elif feature == "Time Management":
    tasks = st.text_area("Enter your tasks (one per line):").split("\n")
    task = "Create Timeline"

elif feature == "Presentation Preparation":
    topic = st.text_input("Enter your presentation topic:")
    task = "Create Presentation Outline"

elif feature == "Defense Preparation":
    response_text = st.text_area("Enter your response to a question:")
    task = st.radio("Task", ["Get Defense Questions", "Prepare Response"])

# Universal "Run" Button
if st.button("Run"):
    if feature == "Topic Refinement":
        if task == "Refine Topic":
            st.success("Refined Suggestions:")
            st.write(refine_topic(topic))
        elif task == "Generate Research Question":
            st.success("Generated Research Question:")
            st.write(generate_research_question(topic))

    elif feature == "Literature Review":
        if task == "Search Literature":
            with st.spinner("Searching..."):
                results = search_literature(query)
            st.success("Relevant Papers Found:")
            st.write(results)
        elif task == "Summarize Paper":
            summary = summarize_paper(paper_title)
            st.success("Summary:")
            st.write(summary)

    elif feature == "Writing Assistance":
        if task == "Improve Writing":
            improved_text = improve_writing(text)
            st.success("Improved Text:")
            st.write(improved_text)
        elif task == "Check Logical Flow":
            feedback = check_logical_flow(text)
            st.success("Feedback:")
            st.write(feedback)

    elif feature == "Proofreading":
        errors = proofread(text)
        st.success("Suggestions:")
        st.write(errors)

    elif feature == "Time Management":
        timeline = create_timeline(tasks)
        st.success("Your Timeline:")
        st.write(timeline)

    elif feature == "Presentation Preparation":
        outline = create_presentation_outline(topic)
        st.success("Presentation Outline:")
        st.write(outline)

    elif feature == "Defense Preparation":
        if task == "Get Defense Questions":
            questions = get_defense_questions()
            st.success("Common Defense Questions:")
            st.write(questions)
        elif task == "Prepare Response":
            prepared_response = prepare_responses(response_text)
            st.success("Prepared Response:")
            st.write(prepared_response)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2023 Thesis Assistant Platform. All rights reserved.</p>", unsafe_allow_html=True)