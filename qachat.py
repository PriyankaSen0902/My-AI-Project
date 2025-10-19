from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key (must be in your .env file as GOOGLE_API_KEY)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🧠 List available models (optional debugging step)
# models = genai.list_models()
# for m in models.models:
#     print(m.name, m.supported_generation_methods)

# ✅ Initialize the Gemini 1.5 model (newer version)
#model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # or gemini-1.5-pro
model = genai.GenerativeModel("gemini-2.5-flash")


# Start chat session
chat = model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit UI setup
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    response = get_gemini_response(input_text)

    # Add user query to chat history
    st.session_state['chat_history'].append(("You", input_text))

    st.subheader("The Response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat history is:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
