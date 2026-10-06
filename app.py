import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ORION AI", page_icon="⚡")

st.title("⚡ ORION - AI Assistant")
st.write("System Online. Standing by for instructions, Boss.")

# Streamlit secrets se key uthayega, nahi toh screen par box dikhayega
api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    user_query = st.text_input("Ask ORION anything...")

    if st.button("Send to ORION") and user_query:
        with st.spinner("ORION is thinking..."):
            try:
                prompt = f"You are ORION, a highly intelligent JARVIS-like AI assistant. Always address the user as 'Boss'. Always speak and respond in natural Hindi / Hinglish. Maintain a smart, loyal, professional, and powerful tone. User query: {user_query}"
                response = model.generate_content(prompt)
                st.write("### ORION:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
              
