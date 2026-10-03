import os
import json
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API Key was not found. Check your .env file")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

def generate_joke_and_fact(topic):
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        temperature = 0.7,
        messages=[
            {
                "role": "system",
                "content": (
                    "You create short, family-friendly jokes and concise, "
                    "well-established facts about any topic given to you. Return the response as JSON."
                ),
            },
            {
                "role": "user",
                "content": f"Create one joke and one fact about {topic}",
            },
        ],
        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "joke_and_fact",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "joke": {"type": "string"},
                        "fact": {"type": "string"},
                    },
                    "required": ["joke", "fact"],
                    "additionalProperties": False,
                },
            },
        },
    )

    return json.loads(response.choices[0].message.content)

st.set_page_config(page_title="Joke & Fact Lab", page_icon=":sparkles:")

st.title("Joke & Fact Lab")
st.write("Generate a joke and an interesting fact about technology and programming.")
topics = ["Python", "AI", "Cloud Computing", "Cybersecurity", "AWS", "Databases", "Coding", "Gym", "Eating Healthy", "Developer Life", "Working & Studying"]
selected_topic = st.selectbox("Choose to topic to know a joke and a fact about it: ",topics)

if st.button("Generate"):
    try:
        with st.spinner("Creating your joke and fact..."):
            result = generate_joke_and_fact(selected_topic)

        joke_column, fact_column = st.columns(2)

        with joke_column:
            st.subheader("Joke")
            st.info(result["joke"])

        with fact_column:
            st.subheader("Fact")
            st.success(result["fact"])

    except Exception:
        st.error("Something went wrong while generating the response. Please try again.")