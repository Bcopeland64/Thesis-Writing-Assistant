---

# **Thesis Assistant Platform**

The **Thesis Assistant Platform** is an all-in-one tool designed to support students throughout their thesis journey. From topic refinement to defense preparation, this platform leverages AI-powered utilities to streamline research, writing, and presentation tasks.

---

## **Features**

The platform offers the following utilities:

### **1. Topic Refinement & Research Question Development**
- Helps refine thesis topics and generate clear, concise research questions.
- Ideal for brainstorming and narrowing down ideas.

### **2. Literature Review Assistance**
- Recommends relevant academic papers and sources based on keywords.
- Summarizes key findings from academic papers to save time.

### **3. Writing Assistance & Draft Review**
- Improves clarity, coherence, and academic tone in your writing.
- Checks logical flow and argument strength in drafts.

### **4. Proofreading & Language Enhancement**
- Detects grammar, spelling, and punctuation errors.
- Enhances vocabulary and ensures consistency in terminology.

### **5. Time Management**
- Creates timelines for thesis tasks with deadlines.
- Helps track progress and stay organized.

### **6. Presentation Preparation**
- Generates outlines for thesis presentations.
- Ensures structured and professional delivery of your work.

### **7. Defense Preparation**
- Provides common defense questions and tips for responding effectively.
- Prepares students for thesis defense scenarios.

### **8. Reference Management**
- Generates citations in multiple formats (APA, MLA, Chicago).
- Simplifies reference formatting for academic writing.

### **9. Data Visualization**
- Visualizes datasets using plots and graphs.
- Supports basic data analysis and exploration.

---

## **Installation Instructions**

### **Prerequisites**
- Python 3.8 or higher installed.
- A Groq API key (sign up at [Groq](https://groq.com)).
- Basic knowledge of Python and Streamlit.

### **Step 1: Clone the Repository**
Clone the repository to your local machine:
```bash
git clone https://github.com/your-repo/thesis_assistant.git
cd thesis_assistant
```

### **Step 2: Set Up a Virtual Environment**
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Step 3: Install Dependencies**
Install the required dependencies:
```bash
pip install -r requirements.txt
```

For Spacy, download the language model:
```bash
python -m spacy download en_core_web_sm
```

### **Step 4: Configure the Groq API Key**
Add your Groq API key to a `.env` file in the project directory:
```plaintext
GROQ_API_KEY=your_groq_api_key
```

Alternatively, set it as an environment variable:
```bash
export GROQ_API_KEY=your_groq_api_key  # On macOS/Linux
set GROQ_API_KEY=your_groq_api_key     # On Windows
```

### **Step 5: Run the App**
Start the Streamlit app:
```bash
streamlit run main.py
```

The app will open in your default web browser.

---

## **Usage**

### **Sidebar Navigation**
- Use the radio buttons in the sidebar to select a feature (e.g., "Topic Refinement", "Literature Review").
- Input fields will dynamically update based on the selected feature.

### **Universal "Run" Button**
- After entering the required inputs, click the "Run" button to execute the selected task.
- Outputs will appear below the button with clear success messages.

---

## **Project Structure**

```
thesis_assistant/
│
├── main.py                # Main Streamlit app
├── utils/                 # Utility functions
│   ├── topic_refinement.py
│   ├── literature_review.py
│   ├── writing_assistance.py
│   ├── proofreading.py
│   ├── time_management.py
│   ├── presentation_preparation.py
│   ├── defense_preparation.py
│   ├── reference_management.py
│   └── data_visualization.py
├── data/                  # Store datasets or user progress
│   └── user_progress.json
├── .env                   # Environment variables (e.g., API keys)
└── requirements.txt        # List of dependencies
```

---

## **Contributing**

We welcome contributions to improve the Thesis Assistant Platform! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add YourFeatureName"`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions, feedback, or support, feel free to reach out:
- Email: brandon.copeland@iu-study.org
- GitHub Issues: https://github.com/Bcopeland64/Thesis-Writing-Assistant/issues

---

## **Acknowledgments**

- **Streamlit**: For providing an easy-to-use framework for building interactive web apps.
- **Groq API**: For enabling fast and efficient LLM inference.
- **Spacy**: For natural language processing capabilities.

---

T
