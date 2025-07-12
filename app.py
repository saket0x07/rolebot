import streamlit as st
from core.chat_engine import get_bot_response
from core.history_manager import get_history, update_history
import json

# Load personas
with open("config/personas.json", "r") as f:
    personas = json.load(f)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar – Persona selector + clear chat
st.sidebar.title("🧠 Persona Settings")
persona_options = list(personas.keys())
selected_persona = st.sidebar.selectbox("Choose Bot Persona", persona_options)
st.sidebar.markdown(f"📝 {personas[selected_persona]['description']}")

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.history = []
    st.experimental_rerun()

# Header
st.title("WELCOME BACK YASHHHH 👋")
st.subheader("How Can I Help You Today?")

# Input box — do NOT rerun here
if prompt := st.chat_input("Ask me anything..."):
    update_history("user", prompt)
    response = get_bot_response(prompt, personas[selected_persona]["prompt"])
    update_history("assistant", response)

# Chat UI — show complete scrollable history
chat_container = st.container()
with chat_container:
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            align_style = "text-align: right;" if msg["role"] == "user" else "text-align: left;"
            st.markdown(f"<div style='{align_style}'>{msg['content']}</div>", unsafe_allow_html=True)

# Auto-scroll to bottom
st.markdown(
    """
    <script>
        var elements = document.getElementsByClassName('stChatMessage');
        if (elements.length > 0) {
            elements[elements.length - 1].scrollIntoView({ behavior: 'smooth' });
        }
    </script>
    """,
    unsafe_allow_html=True
)

