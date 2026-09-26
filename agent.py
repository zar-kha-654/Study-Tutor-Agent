import os
import litellm

from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM

from tools import study_calculator
from memory import create_memory


# --------------------------------------------------
# FIX FOR CREWAI + GROQ CACHE_BREAKPOINT ERROR
# --------------------------------------------------

_original_completion = litellm.completion


def completion_without_cache_breakpoint(*args, **kwargs):
    """
    Remove CrewAI's cache_breakpoint field before
    sending messages to Groq.
    """

    kwargs["caching"] = False

    messages = kwargs.get("messages", [])

    for message in messages:

        if isinstance(message, dict):

            message.pop("cache_breakpoint", None)

            content = message.get("content")

            if isinstance(content, list):

                for block in content:

                    if isinstance(block, dict):
                        block.pop("cache_breakpoint", None)

    return _original_completion(*args, **kwargs)


litellm.completion = completion_without_cache_breakpoint


# --------------------------------------------------
# CREATE STUDY TUTOR
# --------------------------------------------------

def create_study_tutor():

    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )

    tutor = Agent(

        role="Study Tutor",

        goal=(
            "Help students understand academic concepts clearly "
            "and improve their learning through simple explanations, "
            "examples, practice questions, and feedback."
        ),

        backstory=(
            "You are a patient and friendly study tutor. "
            "You explain difficult concepts in simple language. "
            "You adapt explanations to the student's level. "
            "You use examples and step-by-step explanations when useful. "
            "You help students practice and learn from their mistakes."
        ),

        llm=llm,

        tools=[study_calculator],

        allow_delegation=False,

        verbose=True
    )

    return tutor


# --------------------------------------------------
# ASK TUTOR
# --------------------------------------------------

def ask_tutor(question, topic, mode):

    tutor = create_study_tutor()

    memory = create_memory()

    task = Task(

        description=f"""
        Help the student with the following request.

        Study topic:
        {topic}

        Study mode:
        {mode}

        Student question:
        {question}

        Instructions:

        1. Answer the student's question clearly.

        2. Use simple language.

        3. Give examples when useful.

        4. Break difficult concepts into smaller steps.

        5. If the student asks for practice questions,
           create useful practice questions.

        6. If the student provides an answer,
           evaluate it and explain mistakes.

        7. Use the Study Calculator tool when
           a mathematical calculation is required.

        8. Be encouraging and student-friendly.

        9. Do not make the explanation unnecessarily complicated.
        """,

        expected_output=(
            "A clear, accurate, simple and student-friendly "
            "tutoring response."
        ),

        agent=tutor
    )

    crew = Crew(

        agents=[tutor],

        tasks=[task],

        process=Process.sequential,

        memory=memory,

        verbose=True
    )

    result = crew.kickoff()

    return str(result)
