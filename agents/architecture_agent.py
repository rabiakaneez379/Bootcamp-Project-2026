import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# Connect to Groq Cloud AI
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=st.secrets["GROQ_API_KEY"]
)


# Create the architecture prompt
prompt = ChatPromptTemplate.from_template("""
You are a professional software architect.

Design a practical technical architecture for the following software project.

Important:
- Prefer a simple monolithic architecture for small and student/bootcamp projects.
- Do NOT recommend microservices unless the project clearly requires them.
- Avoid unnecessary complexity.
- Choose technologies that are realistic for the selected programming language.
- Make the architecture easy to develop, test, and demonstrate.

Project Name: {project_name}

Programming Language: {language}

Project Description:
{description}

Requirements Analysis:
{requirements}

Provide a structured architecture report containing:

1. System Architecture
2. Main Components
3. User Roles
4. Database Design
5. API Design
6. Technology Stack
7. Project Folder Structure
8. Data Flow
9. Security Considerations
10. Development Recommendations

Use simple, clear language.
Make the architecture practical for a student/bootcamp project.
""")


# Create the AI chain
chain = prompt | llm


# Architecture Agent function
def design_architecture(
    project_name,
    description,
    language,
    requirements
):

    response = chain.invoke({
        "project_name": project_name,
        "description": description,
        "language": language,
        "requirements": requirements
    })

    return response.content