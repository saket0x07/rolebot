import streamlit as st

def get_history():
    if "history" not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

def update_history(role, content):
    st.session_state.history.append({"role": role, "content": content})
