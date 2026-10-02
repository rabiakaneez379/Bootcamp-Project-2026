import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Connect to Groq Cloud AI
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=st.secrets["GROQ_API_KEY"]
)

# Create the code generation prompt
prompt = ChatPromptTemplate.from_template("""
You are a professional software developer.

Generate a practical project structure and starter source code
for the following software project.

Project Name:
{project_name}

Programming Language:
{language}

Project Description:
{description}

Requirements Analysis:
{requirements}

System Architecture:
{architecture}

Instructions:

1. Create a clear project folder structure.
2. Identify the most important source files.
3. Generate working starter code for the main files.
4. Keep the implementation simple and suitable for a student
   or bootcamp project.
5. Do not use unnecessary technologies.
6. Use the selected programming language.
7. Clearly label every file.
8. Put code inside Markdown code blocks.
9. Make sure the generated code is consistent with the
   requirements and architecture.

Return the result in this format:

PROJECT STRUCTURE

[folder structure]

FILES

FILE: filename
[code]

FILE: filename
[code]

SETUP INSTRUCTIONS

[steps required to run the project]
""")

# Create the AI chain
chain = prompt | llm


def generate_code(
    project_name,
    description,
    language,
    requirements,
    architecture
):

    response = chain.invoke({
        "project_name": project_name,
        "description": description,
        "language": language,
        "requirements": requirements,
        "architecture": architecture
    })

    return response.content