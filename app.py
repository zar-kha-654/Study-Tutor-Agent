import streamlit as st
from agent import ask_tutor


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 20% 10%, rgba(0, 217, 255, 0.12), transparent 30%),
            radial-gradient(circle at 80% 20%, rgba(80, 100, 255, 0.10), transparent 30%),
            #050914;
        color: white;
    }

    /* Hide Streamlit menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 30px 20px 20px 20px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        color: #00d9ff;
        text-shadow:
            0 0 10px rgba(0, 217, 255, 0.7),
            0 0 25px rgba(0, 217, 255, 0.4);
    }

    .hero-subtitle {
        font-size: 18px;
        color: #aab7c8;
        margin-top: 10px;
    }

    /* Status */
    .status {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-top: 18px;
        padding: 8px 18px;
        border-radius: 30px;
        background: rgba(0, 217, 255, 0.08);
        border: 1px solid rgba(0, 217, 255, 0.3);
        color: #d9f9ff;
        font-size: 14px;
    }

    .status-dot {
        width: 9px;
        height: 9px;
        background: #00ff9d;
        border-radius: 50%;
        box-shadow: 0 0 12px #00ff9d;
    }

    /* Feature cards */
    .card {
        min-height: 190px;
        padding: 25px;
        border-radius: 20px;
        background: linear-gradient(
            145deg,
            rgba(14, 27, 48, 0.95),
            rgba(7, 15, 29, 0.95)
        );
        border: 1px solid rgba(0, 217, 255, 0.25);
        box-shadow:
            0 0 20px rgba(0, 217, 255, 0.05),
            inset 0 0 20px rgba(0, 217, 255, 0.02);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(0, 217, 255, 0.7);
        box-shadow:
            0 0 25px rgba(0, 217, 255, 0.15);
    }

    .card-icon {
        font-size: 38px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 23px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }

    .card-text {
        font-size: 15px;
        line-height: 1.6;
        color: #9eacbf;
    }

    /* Section title */
    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
        color: #ffffff;
    }

    /* Input labels */
    label {
        color: #dce8f5 !important;
        font-weight: 600 !important;
    }

    /* Text input */
    .stTextInput input,
    .stTextArea textarea {
        background-color: #0a1220 !important;
        color: white !important;
        border: 1px solid rgba(0, 217, 255, 0.25) !important;
        border-radius: 12px !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border: 1px solid #00d9ff !important;
        box-shadow: 0 0 10px rgba(0, 217, 255, 0.2) !important;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background-color: #0a1220 !important;
        border: 1px solid rgba(0, 217, 255, 0.25) !important;
        border-radius: 12px !important;
    }

    /* Ask button */
    .stButton > button {
        background: linear-gradient(
            90deg,
            #00bfff,
            #0077ff
        ) !important;

        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: 700 !important;

        box-shadow:
            0 0 15px rgba(0, 191, 255, 0.25);

        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 0 25px rgba(0, 191, 255, 0.5);
    }

    /* Response box */
    .response-box {
        background: rgba(10, 20, 35, 0.95);
        border: 1px solid rgba(0, 217, 255, 0.25);
        border-radius: 18px;
        padding: 25px;
        margin-top: 25px;
        color: #eaf6ff;
        line-height: 1.7;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.05);
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #68788d;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🎓 Study Tutor AI
        </div>

        <div class="hero-subtitle">
            Your intelligent study companion — learn concepts,
            practice questions, and improve your understanding.
        </div>

        <div class="status">
            <span class="status-dot"></span>
            AI Tutor Ready
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# FEATURE CARDS
# -----------------------------
st.markdown(
    '<div class="section-title">✨ What can I help you with?</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown(
        """
        <div class="card">

            <div class="card-icon">💡</div>

            <div class="card-title">
                Learn
            </div>

            <div class="card-text">
                Understand difficult concepts
                with simple explanations and
                useful examples.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:
    st.markdown(
        """
        <div class="card">

            <div class="card-icon">🧠</div>

            <div class="card-title">
                Practice
            </div>

            <div class="card-text">
                Generate practice questions
                and test your knowledge.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:
    st.markdown(
        """
        <div class="card">

            <div class="card-icon">⚡</div>

            <div class="card-title">
                Improve
            </div>

            <div class="card-text">
                Get personalized feedback
                and improve your answers.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# STUDY SECTION
# -----------------------------
st.markdown(
    '<div class="section-title">📚 Start Studying</div>',
    unsafe_allow_html=True
)


topic = st.text_input(
    "📖 Study Topic",
    placeholder="Example: Data Structures, Statistics, Python..."
)


mode = st.selectbox(
    "🎯 Study Mode",
    [
        "Explain Concept",
        "Practice Questions",
        "Check My Answer",
        "General Question"
    ]
)


question = st.text_area(
    "💬 What would you like to ask?",
    placeholder="Ask your Study Tutor anything...",
    height=150
)


# -----------------------------
# ASK BUTTON
# -----------------------------
if st.button(
    "✨ Ask Study Tutor",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        with st.spinner("🧠 Study Tutor is thinking..."):

            try:

                response = ask_tutor(
                    question=question,
                    topic=topic,
                    mode=mode
                )

                st.markdown(
                    f"""
                    <div class="response-box">

                    <h3>🤖 Study Tutor</h3>

                    {response}

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <div class="custom-footer">
        🎓 Study Tutor AI &nbsp;•&nbsp;
        Powered by CrewAI + Groq
    </div>
    """,
    unsafe_allow_html=True
)
