import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="ORION AI", page_icon="⚡", layout="centered")

st.title("⚡ ORION - AI Assistant")
st.write("System Online. Standing by for instructions...")

api_key = st.secrets.get("OPENAI_API_KEY", "")

if not api_key:
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # Camera / Image Input
    img_file = st.camera_input("Take a picture for ORION")
    
    # Text Query
    user_query = st.text_input("Ask ORION anything:")

    if st.button("Send to ORION") and user_query:
        with st.spinner("ORION is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "You are ORION, a highly intelligent JARVIS-like AI assistant. Always address the user as 'Boss'. Always speak and respond in natural Hindi / Hinglish. Maintain a smart, loyal, professional, and powerful tone."}
                              
                        {"role": "system", "content": "You are ORION, a futuristic, highly intelligent, JARVIS-like AI assistant. Speak concisely and smartly."},
                        {"role": "user", "content": user_query}
                    ]
                )
                st.success(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
              
