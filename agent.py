import os

from crewai import Agent, Task, Crew, Process

from tools import study_calculator
from memory import create_memory


def create_study_tutor():

    llm = {
        "model": "groq/openai/gpt-oss-120b",
        "api_key": os.getenv("GROQ_API_KEY"),
        "temperature": 0.3
    }

    tutor = Agent(
        role="Study Tutor",

        goal=(
            "Help students understand academic concepts clearly "
            "and improve their learning through simple explanations, "
            "examples, questions, and feedback."
        ),

        backstory=(
            "You are a patient and friendly study tutor. "
            "You explain difficult concepts in simple language. "
            "You adapt explanations to the student's level. "
            "You use examples and step-by-step explanations when useful. "
            "You remember relevant information from previous study sessions."
        ),

        llm=llm,

        tools=[study_calculator],

        allow_delegation=False,

        verbose=True
    )

    return tutor


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
        3. Give an example when useful.
        4. Break difficult concepts into smaller steps.
        5. If the student asks for practice questions, create them.
        6. If the student provides an answer, evaluate it and explain mistakes.
        7. Use the Study Calculator tool when a mathematical calculation
           is required.
        8. Use relevant previous memory when it helps the student.
        """,

        expected_output=(
            "A clear, accurate and student-friendly tutoring response."
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
