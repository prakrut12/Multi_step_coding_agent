import streamlit as st
from agent import planner, solver, debugger

st.title("🤖 Multi-Step Coding Agent (Gemini AI)")

problem = st.text_input("Enter your coding problem:")

if st.button("Run Agent"):
    if problem:

        st.subheader("🧠 Planning")
        st.write(planner(problem))

        st.subheader("💻 Code Generation")
        code = solver(problem)
        st.code(code)

        st.subheader("🔧 Code Improvement")
        st.write(debugger(problem))