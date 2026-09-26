from crewai.tools import tool


@tool("Study Calculator")
def study_calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    Use this tool when the student asks for a calculation.
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception:
        return "I could not calculate that expression."
