import streamlit as st
from agent import ask_tutor


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 170, 255, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(100, 50, 255, 0.10),
                transparent 30%
            ),
            #050914;
        color: #f5f7ff;
    }

    /* Remove Streamlit top spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #070d1c 0%,
            #050914 100%
        );

        border-right: 1px solid rgba(0, 195, 255, 0.15);
    }

    section[data-testid="stSidebar"] h2 {
        color: #00c8ff;
    }


    /* =========================
       HEADER
       ========================= */

    .hero {
        padding: 30px;
        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(0, 174, 255, 0.14),
                rgba(80, 50, 255, 0.10)
            );

        border: 1px solid rgba(0, 195, 255, 0.25);

        box-shadow:
            0 0 40px rgba(0, 174, 255, 0.08);

        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;

        background: linear-gradient(
            90deg,
            #00d9ff,
            #5b7cff,
            #a855f7
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #aebbd0;
        font-size: 17px;
    }


    /* =========================
       FEATURE CARDS
       ========================= */

    .feature-card {
        background: rgba(10, 18, 35, 0.75);

        border: 1px solid rgba(0, 195, 255, 0.15);

        border-radius: 18px;

        padding: 20px;

        min-height: 125px;

        transition: 0.2s ease;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.20);
    }

    .feature-card:hover {
        border-color: rgba(0, 195, 255, 0.45);

        box-shadow:
            0 0 25px rgba(0, 195, 255, 0.10);
    }

    .feature-icon {
        font-size: 28px;
    }

    .feature-title {
        font-weight: 700;
        margin-top: 8px;
        color: #ffffff;
    }

    .feature-text {
        color: #8e9bb2;
        font-size: 14px;
        margin-top: 5px;
    }


    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 22px;
        font-weight: 700;

        margin-top: 25px;
        margin-bottom: 15px;

        color: #f5f7ff;
    }


    /* =========================
       INPUTS
       ========================= */

    .stTextInput input,
    .stTextArea textarea {

        background-color: #080f20 !important;

        color: white !important;

        border: 1px solid rgba(0, 195, 255, 0.20) !important;

        border-radius: 12px !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {

        border: 1px solid #00c8ff !important;

        box-shadow:
            0 0 15px rgba(0, 200, 255, 0.15) !important;
    }


    /* =========================
       SELECT BOX
       ========================= */

    div[data-baseweb="select"] > div {

        background-color: #080f20 !important;

        border: 1px solid rgba(0, 195, 255, 0.20) !important;

        border-radius: 12px !important;

        color: white !important;
    }


    /* =========================
       BUTTON
       ========================= */

    .stButton > button {

        width: 100%;

        border-radius: 12px;

        border: 1px solid #00c8ff;

        background:
            linear-gradient(
                90deg,
                #008cff,
                #5b5cff
            );

        color: white;

        font-size: 16px;

        font-weight: 700;

        padding: 12px;

        transition: 0.2s ease;

        box-shadow:
            0 0 20px rgba(0, 174, 255, 0.20);
    }

    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 0 30px rgba(0, 200, 255, 0.40);
    }


    /* =========================
       RESPONSE CARD
       ========================= */

    .response-card {

        background:
            linear-gradient(
                135deg,
                rgba(7, 20, 38, 0.95),
                rgba(9, 16, 35, 0.95)
            );

        border: 1px solid rgba(0, 195, 255, 0.22);

        border-radius: 20px;

        padding: 25px;

        margin-top: 20px;

        box-shadow:
            0 0 30px rgba(0, 195, 255, 0.08);
    }

    .response-header {

        color: #00d9ff;

        font-size: 18px;

        font-weight: 700;

        margin-bottom: 12px;
    }


    /* =========================
       STATUS
       ========================= */

    .status {

        display: inline-flex;

        align-items: center;

        gap: 8px;

        padding: 7px 12px;

        border-radius: 20px;

        background: rgba(0, 200, 255, 0.08);

        border: 1px solid rgba(0, 200, 255, 0.20);

        color: #7deaff;

        font-size: 13px;
    }

    .status-dot {

        width: 8px;

        height: 8px;

        background: #00e5ff;

        border-radius: 50%;

        box-shadow:
            0 0 10px #00e5ff;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {

        text-align: center;

        color: #64748b;

        margin-top: 40px;

        font-size: 13px;
    }


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 30px;
        }

        .hero {
            padding: 22px;
        }

        .hero-subtitle {
            font-size: 14px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 🎓 Study Tutor")

    st.markdown(
        """
        <div class="status">
            <span class="status-dot"></span>
            AI Tutor Online
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 📚 Study Modes")

    st.markdown(
        """
        **💡 Explain Topic**

        Understand a concept simply.

        **❓ Ask Question**

        Ask your tutor anything.

        **🧠 Practice Quiz**

        Test your knowledge.

        **✅ Check My Answer**

        Get feedback on your answer.
        """
    )

    st.markdown("---")

    st.markdown("### ⚡ Powered By")

    st.caption("CrewAI")
    st.caption("Groq")
    st.caption("AI Memory")


# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

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

        <br>

        <div class="status">
            <span class="status-dot"></span>
            AI Tutor Ready
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">💡</div>

            <div class="feature-title">
                Learn
            </div>

            <div class="feature-text">
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
        <div class="feature-card">

            <div class="feature-icon">🧠</div>

            <div class="feature-title">
                Practice
            </div>

            <div class="feature-text">
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
        <div class="feature-card">

            <div class="feature-icon">⚡</div>

            <div class="feature-title">
                Improve
            </div>

            <div class="feature-text">
                Get personalized feedback
                and improve your answers.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# STUDY INPUT
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">📚 Start Learning</div>',
    unsafe_allow_html=True
)


topic = st.text_input(
    "Study Topic",
    placeholder="e.g. Data Structures, Statistics, Python..."
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
    "💬 What would you like to learn?",
    placeholder=(
        "Example: Explain binary search "
        "like I am a complete beginner."
    ),
    height=140
)


# ---------------------------------------------------------
# ASK BUTTON
# ---------------------------------------------------------

if st.button("✨ Ask Study Tutor"):

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        with st.spinner(
            "🧠 Your AI tutor is thinking..."
        ):

            try:

                response = ask_tutor(
                    question=question,
                    topic=topic,
                    mode=mode
                )

                st.markdown(
                    """
                    <div class="response-card">

                        <div class="response-header">
                            👨‍🏫 Study Tutor
                        </div>

                    """,
                    unsafe_allow_html=True
                )

                st.markdown(response)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">

        🎓 Study Tutor AI · Built with
        Streamlit + CrewAI + Groq

    </div>
    """,
    unsafe_allow_html=True
)
