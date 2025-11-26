import streamlit as st
from streamlit_mic_recorder import mic_recorder
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Interview VoiceBot", layout="centered")

# ---------------- UI ----------------
st.markdown("""
    <h1 style="text-align:center;color:#4A90E2;">🎤 AI Interview VoiceBot</h1>
    <p style="text-align:center;font-size:18px;">
        Press <strong>Start Speaking</strong>, Question naturally, then press <strong>Stop</strong>.
    </p>
""", unsafe_allow_html=True)

st.write("---")

# ---------------- MIC WITH MANUAL STOP ----------------
audio = mic_recorder(
    start_prompt="🎙️ Start Speaking",
    stop_prompt="🛑 Stop Recording",
    just_once=False,
    use_container_width=True,
    key="voice"
)

# ---------------- PROCESS AUDIO ----------------
if audio:
    st.success("Processing your answer...")

    wav_file = "input.wav"
    with open(wav_file, "wb") as f:
        f.write(audio["bytes"])

    # STEP 1 — Transcribe
    with open(wav_file, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=f,
            model="whisper-1"
        )

    user_text = transcription.text

    st.subheader("🗣️ You said:")
    st.info(user_text)

    # STEP 2 — Human-like Interview Response
    prompt = f"""
    You are acting as a real human candidate named **Ranjan Yadav**. 
    Use ONLY the following real background details—NO fabricated stories, NO imaginary companies.

    Here is your actual profile:

    - B.Tech CSE graduate in 2025 from Kurukshetra University.
    - Strong in Python, SQL, Machine Learning, Generative AI.
    - Skilled with PyTorch, TensorFlow, Scikit-learn, LangChain, FastAPI, RAG pipelines.
    - Experience: Junior Data Analyst Intern — data cleaning (Pandas), Power BI dashboards, SQL query optimization (+10% efficiency).
    - Projects:
    * Age & Gender Prediction (CNN — PyTorch, ResNet, Streamlit)
    * AI Medical Agent (LangGraph, Groq, RAG—95%+ retrieval accuracy)
    - Technical tools: Python, Machine Learning, Generative AI, Docker, Streamlit, GitHub, MongoDB, SQL Server.
    - Achievements: 5-star SQL (HackerRank), solved 100+ DSA problems.
    - Personality: fast learner, analytical, practical, structured thinker.

    Rules:
    - Answer in a natural human tone.
    - Keep answers short and crisp unless the question demands depth.
    - Never fabricate details outside the resume.
    - Sound confident, clear, and conversational.

    User asked: {user_text}
    """


    chat_resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = chat_resp.choices[0].message.content

    st.subheader("🤖 Human-like Response:")
    st.success(answer)

    # STEP 3 — Text → Speech
    tts = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=answer
    )

    mp3_path = "response.mp3"
    with open(mp3_path, "wb") as f:
        f.write(tts.read())

    st.subheader("🔊 Voice Output:")
    st.audio(mp3_path)
