# Joke & Fact Lab

A small Streamlit app that generates a technology-related joke and an interesting fact using the Groq API.

## Features

- Generates a programming, AI, cloud, cybersecurity, or developer-life joke
- Generates a related technology fact
- Makes one LLM API call only when the Generate button is clicked
- Uses structured JSON output for reliable joke and fact fields

## Tech Stack

- Python
- Streamlit
- Groq API
- OpenAI Python SDK
- python-dotenv

## Local Setup

1. Clone this repository.

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. Install Dependencies

   ```python
   python -m pip install -r requirements.txt

4. Create a .env file and add your GROQ API key.

   ```bash
   GROQ_API_KEY=your_actual_key_here

5. Run the App

   ```python
   streamlit run joke_fact_generator.py
