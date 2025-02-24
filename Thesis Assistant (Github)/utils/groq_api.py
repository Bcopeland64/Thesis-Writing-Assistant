# utils/groq_api.py
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace with your actual Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Use the correct Groq API endpoint
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Verified endpoint <button class="citation-flag" data-index="9">

def call_groq(prompt, max_tokens=100, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Replace with the model you want to use <button class="citation-flag" data-index="7">
        "messages": [{"role": "user", "content": prompt}],  # Correct payload structure <button class="citation-flag" data-index="7">
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        # Parse the response correctly <button class="citation-flag" data-index="7">
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        return f"Error: {response.status_code}, {response.text}"