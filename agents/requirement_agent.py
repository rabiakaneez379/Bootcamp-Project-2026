from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# Connect to the local AI model
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
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