import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

st.set_page_config(
    page_title="LLM MCQ Generator",
    page_icon="📝"
)

st.title("LLM MCQ Generator")
st.write("Generate Multiple Choice Questions using LLM")

topic = st.text_input("Enter Topic")

number = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate MCQs"):

    if topic == "":
        st.warning("Please enter a topic.")

    elif not HF_TOKEN:
        st.error("Hugging Face API Key not found. Check your .env file.")

    else:
        client = InferenceClient(
            api_key=HF_TOKEN,
            provider="groq"
        )

        prompt = f"""
Create {number} multiple choice questions about {topic}.

Difficulty level: {difficulty}

For each question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Make sure each question has exactly four options.
Do not repeat questions.
"""

        with st.spinner("Generating MCQs..."):

            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=2500
                )

                result = response.choices[0].message.content

                st.subheader("Generated MCQs")
                st.write(result)

            except Exception as e:
                st.error("Error generating MCQs")
                st.write(str(e))
