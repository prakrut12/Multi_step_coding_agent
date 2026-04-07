 🤖 Multi-Step Coding Agent 

A smart coding assistant that simulates an **agentic workflow** by breaking down problems into multiple steps: planning, code generation, and debugging.

This project is designed with a **hybrid approach**:
- ✅ Uses **Google Gemini API** for real AI responses (when available)
- ✅ Falls back to **built-in logic** when API quota is exceeded or unavailable



 🚀 Features

- 🧠 Planning Agent 
  Breaks the problem into step-by-step logic

- 💻 Code Generation Agent 
  Generates Python code for given problems

- 🔧Debugging Agent
  Detects errors and suggests improvements

- ⚡Hybrid AI System
  - Uses Gemini API when available
  - Switches to local fallback logic when API fails

⚙️ Installation
pip install streamlit google-generativeai

How to run:
python -m streamlit run app.py

Deployed Link: https://multistepcodingagent-in3q7auccsoy2ovrpvms4c.streamlit.app/

UI Preview image:

<img width="596" height="530" alt="image" src="https://github.com/user-attachments/assets/7bde408b-bcf0-493b-a395-3ce408052b1f" />


