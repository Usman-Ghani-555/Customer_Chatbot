import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit setup
st.set_page_config(page_title="Kings Pizza Shop Chatbot 🍕", page_icon="🍕")
st.title("🍕 Kings Pizza Shop Customer Support Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful pizza shop assistant. Greet customers, answer menu and delivery questions, and take pizza orders politely."}
    ]

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Ask me about pizzas, deals, or delivery...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message instantly
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or gpt-4o / gpt-5 if you have access
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
