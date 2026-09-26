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
# SIMPLE AI-STYLE UI
# -----------------------------
st.markdown(
    """
    <style>

    .stApp {
        background: #050914;
        color: white;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
    }

    h1 {
        color: #00d9ff !important;
        text-align: center;
        font-size: 48px !important;
    }

    .subtitle {
        text-align: center;
        color: #aab7c8;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #0a1220 !important;
        color: white !important;
        border: 1px solid #164b68 !important;
        border-radius: 12px !important;
    }

    .stButton button {
        background: #0077ff !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# HEADER
# -----------------------------
st.title("🎓 Study Tutor AI")

st.markdown(
    '<p class="subtitle">Your intelligent study companion — learn concepts, practice questions, and improve your understanding.</p>',
    unsafe_allow_html=True
)

st.success("🟢 AI Tutor Ready")


# -----------------------------
# FEATURES
# -----------------------------
st.subheader("✨ What can I help you with?")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        💡 **Learn**

        Understand difficult concepts
        with simple explanations and
        useful examples.
        """
    )

with col2:
    st.info(
        """
        🧠 **Practice**

        Generate practice questions
        and test your knowledge.
        """
    )

with col3:
    st.info(
        """
        ⚡ **Improve**

        Get personalized feedback
        and improve your answers.
        """
    )


# -----------------------------
# STUDY SECTION
# -----------------------------
st.subheader("📚 Start Studying")

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
# ASK TUTOR
# -----------------------------
if st.button(
    "✨ Ask Study Tutor",
    use_container_width=True
):

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        with st.spinner("🧠 Study Tutor is thinking..."):

            try:

                response = ask_tutor(
                    question=question,
                    topic=topic,
                    mode=mode
                )

                st.subheader("🤖 Study Tutor")

                st.write(response)

            except Exception as e:

                st.error(f"Something went wrong: {e}")


# -----------------------------
# FOOTER
# -----------------------------
st.caption(
    "🎓 Study Tutor AI • Powered by CrewAI + Groq"
)
