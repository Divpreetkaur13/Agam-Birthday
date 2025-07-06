import streamlit as st
from PIL import Image
import base64
import time

# Setup
st.set_page_config(page_title="Agam's Birthday 🎂", page_icon="🎉", layout="centered")

# Set background image
def set_bg(img_path):
    with open(img_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Autoplay audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Typewriter message
def typewriter_effect(text):
    container = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        text_with_breaks = full_text.replace('\\n', '<br>').replace('\n', '<br>')
        rendered_html = f"""
        <div style='
            font-family: "Courier New", monospace;
            font-size: 22px;
            font-weight: bold;
            color: white;
            text-align: center;
            text-shadow: 1px 1px 5px black;
            background-color: rgba(0, 0, 0, 0.4);
            padding: 20px;
            border-radius: 10px;
            margin-top: -420px;
            margin-left: auto;
            margin-right: auto;
            width: 85%;
        '>
        {text_with_breaks}
        </div>
        """
        container.markdown(rendered_html, unsafe_allow_html=True)
        time.sleep(0.03)

# Set background
set_bg("image.jpg")

# Session tracking
if "step" not in st.session_state:
    st.session_state.step = 0

# Step 0: Click for Surprise
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: white;'>🎉 Click for Surprise 🎉</h1>", unsafe_allow_html=True)
    if st.button("Click for Surprise"):
        st.session_state.step = 1
        st.rerun()

# Step 1: Show photo + heading + audio
elif st.session_state.step == 1:
    st.image("agam.jpeg", use_container_width=True)
    st.markdown("""
        <h1 style='
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 2px 2px 8px #000000;
            margin-top: 20px;
            font-family: "Trebuchet MS", sans-serif;
        '>
            🎾 Happy Birthday Agam! 🎾
        </h1>
    """, unsafe_allow_html=True)
    autoplay_audio("birthdaysong.mp3")
    if st.button("Next"):
        st.session_state.step = 2
        st.rerun()

# Step 2: Message on image + audio
elif st.session_state.step == 2:
    st.image("message.png", use_container_width=True)
    autoplay_audio("birthdaysong.mp3")

    birthday_message = """
Dear Agam,

Today, the court of life celebrates a true champion — YOU. 🏆  
Your strength, discipline, and passion for tennis inspire us all.  
Just like your killer serves and unstoppable forehands,  
may this year bring victories, joy, and endless love.  

Keep swinging for the stars, chasing every dream, and living with purpose.  

🎾 You’re not just an amazing brother, but a born winner.  
Happy Birthday, Champ! 🎉
    """
    typewriter_effect(birthday_message)
