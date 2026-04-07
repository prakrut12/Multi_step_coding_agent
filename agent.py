import google.generativeai as genai

# 🔑 Put your Gemini API key here
import streamlit as st


genai.configure(api_key=st.secrets["GEMINI_API_KEY"]))

# Try loading model
try:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    use_ai = True
except:
    use_ai = False


# --- Planner ---
def planner(problem):
    if use_ai:
        try:
            res = model.generate_content(
                f"Break this coding problem into steps:\n{problem}"
            )
            if res.text:
                return res.text
        except:
            pass

    # ✅ fallback
    return f"""Step 1: Understand problem → {problem}
Step 2: Choose logic (recursion / loop)
Step 3: Implement solution"""


# --- Solver ---
def solver(problem):
    if use_ai:
        try:
            res = model.generate_content(
                f"Write clean Python code for:\n{problem}"
            )
            if res.text:
                return res.text
        except:
            pass

    # ✅ fallback logic
    problem = problem.lower()

    if "factorial" in problem:
        return """def factorial(n):
    return 1 if n==0 else n*factorial(n-1)"""

    elif "fibonacci" in problem:
        return """def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b"""

    return "AI can generate solution dynamically"


# --- Debugger ---
def debugger(code):
    if use_ai:
        try:
            res = model.generate_content(
                f"Find errors and improve this code:\n{code}"
            )
            if res.text:
                return res.text
        except:
            pass

    # ✅ fallback debugging
    errors = []

    if " if " in code and "=" in code and "==" not in code:
        errors.append("❌ Use '==' instead of '='")

    if "def" in code and ":" not in code.split("\n")[0]:
        errors.append("❌ Missing ':' after function definition")

    if errors:
        return "\n".join(errors)

    return "✨ Code looks fine"
