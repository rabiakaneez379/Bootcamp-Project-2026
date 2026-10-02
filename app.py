import streamlit as st

from agents.requirement_agent import analyze_requirements
from agents.architecture_agent import design_architecture
from agents.code_agent import generate_code


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="DevPilot AI",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main application background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #0f172a 100%
    );
    color: #f8fafc;
}


/* Main content width */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Main title */
h1 {
    font-size: 3.2rem !important;
    font-weight: 800 !important;
    text-align: center;
    color: #ffffff;
    margin-bottom: 0.2rem;
}


/* Subtitle */
h2 {
    color: #38bdf8 !important;
    font-weight: 700 !important;
}


/* Section headings */
h3 {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
}


/* Normal text */
p {
    color: #cbd5e1;
}


/* Input labels */
label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}


/* Text input and text area */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}


/* Input focus */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2) !important;
}


/* Primary button */
.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    ) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 1rem !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    transition: all 0.3s ease;
}


/* Button hover */
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(6, 182, 212, 0.35);
}


/* Divider */
hr {
    border-color: #334155 !important;
}


/* Success message */
div[data-testid="stAlert"] {
    border-radius: 10px !important;
}


/* Code blocks */
.stCodeBlock {
    border-radius: 12px !important;
    border: 1px solid #334155 !important;
}


/* Markdown content */
[data-testid="stMarkdownContainer"] {
    color: #cbd5e1;
}


/* Spinner */
.stSpinner > div {
    color: #38bdf8 !important;
}


/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    margin-top: 40px;
    padding: 20px;
    border-top: 1px solid #334155;
}


/* Agent cards */
.agent-card {
    background: linear-gradient(
        145deg,
        #1e293b,
        #0f172a
    );
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px;
    margin: 10px 0;
    text-align: center;
    transition: all 0.3s ease;
}


.agent-card:hover {
    border-color: #38bdf8;
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}


.agent-icon {
    font-size: 2.5rem;
}


.agent-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #f8fafc;
}


.agent-description {
    font-size: 0.9rem;
    color: #94a3b8;
}


/* Project summary cards */
.summary-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 10px;
}


</style>
""", unsafe_allow_html=True)



# ==========================================
# MAIN HEADING
# ==========================================

st.title("🤖 DevVoyra")

st.subheader(
    "Your Autonomous AI Software Development Team"
)

st.write(
    "Describe your software idea, and DevPilot AI will help "
    "you plan, generate, test, and improve your code."
)

st.divider()

# ==========================================
# AI AGENTS
# ==========================================

st.markdown("### 🧩 Your AI Development Team")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-icon">🧠</div>
        <div class="agent-title">Requirement Agent</div>
        <div class="agent-description">
            Understands your project idea and
            converts it into clear requirements.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-icon">🏗️</div>
        <div class="agent-title">Architecture Agent</div>
        <div class="agent-description">
            Designs the system architecture,
            database, APIs and project structure.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="agent-card">
        <div class="agent-icon">💻</div>
        <div class="agent-title">Code Agent</div>
        <div class="agent-description">
            Generates project structure and
            starter source code.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.divider()

# ==========================================
# USER INPUT
# ==========================================

st.header("🚀 Start a New Project")

project_name = st.text_input(
    "Project Name",
    placeholder="e.g. Student Management System"
)

project_description = st.text_area(
    "Describe your software idea",
    placeholder=(
        "Explain what you want your application to do, "
        "which features it should include, and how it should work..."
    ),
    height=180
)

programming_language = st.selectbox(
    "Choose Programming Language",
    [
        "Python",
        "JavaScript",
        "HTML/CSS",
        "Java"
    ]
)


# ==========================================
# START PROJECT
# ==========================================

if st.button(
    "Start Building My Project",
    type="primary"
):

    # Check input
    if (
        not project_name.strip()
        or not project_description.strip()
    ):

        st.warning(
            "Please enter a project name and description."
        )

    else:

        st.success(
            "Your project request has been received!"
        )


        # ==========================================
        # PROJECT SUMMARY
        # ==========================================

        st.subheader("📋 Project Summary")

        st.write(
            "**Project Name:**",
            project_name
        )

        st.write(
            "**Programming Language:**",
            programming_language
        )

        st.write(
            "**Project Description:**",
            project_description
        )


        # ==========================================
        # REQUIREMENT ANALYSIS AGENT
        # ==========================================

        st.divider()

        st.subheader(
            "🧠 Requirement Analysis Agent"
        )

        try:

            with st.spinner(
                "AI Agent is analyzing your requirements..."
            ):

                analysis = analyze_requirements(
                    project_name,
                    project_description,
                    programming_language
                )

            st.success(
                "Requirement analysis completed!"
            )

            st.markdown(analysis)

        except Exception as e:

            st.error(
                "The Requirement Analysis Agent "
                "could not complete the analysis."
            )

            st.caption(
                "Please make sure Ollama is running and "
                "the llama3.2:3b model is installed."
            )

            st.exception(e)

            st.stop()


        # ==========================================
        # ARCHITECTURE AGENT
        # ==========================================

        st.divider()

        st.subheader(
            "🏗️ Architecture Agent"
        )

        try:

            with st.spinner(
                "Architecture Agent is designing your system..."
            ):

                architecture = design_architecture(
                    project_name,
                    project_description,
                    programming_language,
                    analysis
                )

            st.success(
                "Architecture design completed!"
            )

            st.markdown(architecture)

        except Exception as e:

            st.error(
                "The Architecture Agent could not "
                "complete the design."
            )

            st.exception(e)

            st.stop()


        # ==========================================
        # CODE GENERATION AGENT
        # ==========================================

        st.divider()

        st.subheader(
            "💻 Code Generation Agent"
        )

        try:

            with st.spinner(
                "Code Agent is generating your project..."
            ):

                generated_code = generate_code(
                    project_name,
                    project_description,
                    programming_language,
                    analysis,
                    architecture
                )

            st.success(
                "Code generation completed!"
            )

            st.markdown(generated_code)

        except Exception as e:

            st.error(
                "The Code Generation Agent could not "
                "generate the project."
            )

            st.exception(e)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "DevPilot AI | Multi-Agent Software Development Assistant"
)
