# LLM MCQ Generator

LLM MCQ Generator is a Python-based web application that uses a Large Language Model to automatically generate multiple-choice questions from a user-provided topic.

## Project Overview

This application allows users to enter a topic, select the number of questions, and choose a difficulty level. The LLM generates MCQs with four options, the correct answer, and an explanation.

## Features

* Generate MCQs automatically using an LLM
* Enter any topic
* Select number of questions
* Select difficulty level
* Four options for each question
* Displays the correct answer
* Provides explanations
* Simple Streamlit web interface

## Technologies Used

* Python
* Streamlit
* Hugging Face
* Hugging Face Inference API
* Python-dotenv
* Large Language Model (LLM)

## Project Structure

```text
LLM-MCQ-Generator/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install streamlit huggingface_hub python-dotenv
```

## API Key Setup

Create a `.env` file in the project folder:

```text
HF_TOKEN=your_huggingface_token
```

Do not upload the `.env` file to GitHub.

## Run the Application

```bash
streamlit run app.py
```

The application will open in the browser.

## How It Works

```text
User enters topic
        ↓
Select number of questions
        ↓
Select difficulty
        ↓
LLM processes the prompt
        ↓
MCQs are generated
        ↓
Questions, options, answers and explanations are displayed
```

## Example

Topic:

```text
Self Attention in LLM
```

Difficulty:

```text
Medium
```

The application generates multiple-choice questions related to Self Attention in Large Language Models.

## Future Enhancements

* Automatic scoring
* Timer-based quiz
* Randomized questions
* Download MCQs as PDF
* Question history
* Multiple subject categories
* Database integration

## Conclusion

The LLM MCQ Generator demonstrates how Large Language Models can be integrated with a Streamlit application to create educational multiple-choice questions dynamically from user-provided topics.
