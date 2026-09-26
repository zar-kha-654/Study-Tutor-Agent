import streamlit as st
from agent import ask_tutor


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #050914;
        color: white;
    }

    /* Main container */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
    }

    /* Main title */
    .main-title {
        font-size: 44px;
        font-weight: 800;
        color: #00d9ff;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        color: #9aa9c2;
        font-size: 18px;
        margin-bottom: 20px;
    }

    /* Status */
    .status {
        display: inline-block;
        padding: 7px 15px;
        border-radius: 20px;
        background-color: #071c2b;
        border: 1px solid #00c8ff;
        color: #6eeaff;
        font-size: 14px;
    }

    /* Feature cards */
    .card {
        background-color: #0a1222;
        border: 1px solid #12304a;
        border-radius: 18px;
        padding: 22px;
        min-height: 150px;
        margin-bottom: 15px;
    }

    .card:hover {
        border-color: #00c8ff;
    }

    .card-icon {
        font-size: 30px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin-top: 8px;
    }

    .card-text {
        color: #8998b0;
        font-size: 14px;
        margin-top: 5px;
    }

    /* Section title */
    .section-title {
        color: white;
        font-size: 24px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Response */
    .response {
        background-color: #081426;
        border: 1px solid #00c8ff;
        border-radius: 18px;
        padding: 25px;
        margin-top: 20px;
    }

    .response-title {
        color: #00d9ff;
        font-size: 20px;
        font-weight: 700;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(
            90deg,
            #008cff,
            #5b5cff
        );

        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-weight: 700;
    }

    .stButton button:hover {
        box-shadow: 0 0 20px #008cff;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🎓 Study Tutor")

    st.markdown(
        """
        ### 📚 Study Modes

        💡 **Explain Topic**

        Understand difficult concepts.

        ❓ **Ask Question**

        Ask your tutor anything.

        🧠 **Practice Quiz**

        Test your knowledge.

        ✅ **Check My Answer**

        Get feedback on your answer.
        """
    )

    st.divider()

    st.caption("Powered by CrewAI + Groq")


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="main-title">🎓 Study Tutor AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Your intelligent study companion — learn concepts,
        practice questions, and improve your understanding.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="status">
        🟢 AI Tutor Ready
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FEATURE CARDS
# =========================================================

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
                with simple explanations.
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
                Generate questions and
                test your knowledge.
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


# =========================================================
# STUDY INPUT
# =========================================================

st.markdown(
    '<div class="section-title">📚 Start Learning</div>',
    unsafe_allow_html=True
)


topic = st.text_input(
    "Study Topic",
    placeholder="Example: Data Structures"
)


mode = st.selectbox(
    "Study Mode",
    [
        "Explain Topic",
        "Ask Question",
        "Practice Quiz",
        "Check My Answer"
    ]
)


question = st.text_area(
    "💬 Your Question",
    placeholder=(
        "Example: Explain binary search "
        "like I am a beginner."
    ),
    height=140
)


# =========================================================
# ASK TUTOR
# =========================================================

if st.button("✨ Ask Study Tutor", use_container_width=True):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("🧠 Your tutor is thinking..."):

            try:

                response = ask_tutor(
                    question=question,
                    topic=topic,
                    mode=mode
                )

                st.markdown(
                    """
                    <div class="response">
                        <div class="response-title">
                            👨‍🏫 Study Tutor
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(response)

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 Study Tutor AI • CrewAI • Groq"
)
