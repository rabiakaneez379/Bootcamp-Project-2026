import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# Connect to Groq Cloud AI
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=st.secrets["GROQ_API_KEY"]
)


# Create the prompt
prompt = ChatPromptTemplate.from_template("""
You are a professional software requirements analyst.

Analyze the following software project.

Project Name: {project_name}

Programming Language: {language}

Project Description: {description}

Provide a structured report containing:

1. Project Overview
2. Main Objectives
3. Functional Requirements
4. Non-Functional Requirements
5. Suggested Features
6. Recommended Technologies
7. Expected Output

Use simple, clear language.
""")


# Create the AI chain
chain = prompt | llm


def analyze_requirements(project_name, description, language):

    response = chain.invoke({
        "project_name": project_name,
        "language": language,
        "description": description
    })

    return response.content