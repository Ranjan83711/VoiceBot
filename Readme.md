# 🎤 AI Voice Interview Bot – Streamlit Web App 
[https://voicebot-mkzkawgljjxwpukyu55ezw.streamlit.app/]

A simple and user-friendly voice-based interview assistant built using Python, Streamlit, OpenAI API, and Whisper.
This app lets users speak their answers through the microphone and receive both text and audio feedback in a natural, human-like interview style.

The goal of this project is to create a fully functional, accessible, and interactive voicebot for interview practice — matching the requirements of the 100x Stage-1 Assessment.

🚀 Features

🎙 Voice Input using the microphone

🛑 Manual Start/Stop Recording (clear visible buttons)

✍️ Speech-to-Text using Whisper

🤖 Human-like interview responses using GPT-4o-mini

🔊 Text-to-Speech audio reply

👤 Personalized Response Mode

Bot answers as Ranjan Yadav, based on your real resume

No hallucinations

Short, confident, human tone

🌐 Fully runs in the browser with an intuitive UI

🔐 Uses .env for API keys (safe + clean)

🛠️ Tech Stack

Python 3.13

Streamlit (Web UI)

streamlit-mic-recorder (Microphone input)

OpenAI API

whisper-1 → Speech to Text

gpt-4o-mini → Chat Response

gpt-4o-mini-tts → Text to Speech

dotenv (Environment variables)

📁 Project Structure
voicebot/
│── app.py
│── requirements.txt
│── .env
│── README.md

🔧 Installation and Setup
1️⃣ Clone this repository
git remote add origin https://github.com/Ranjan83711/VoiceBot.git

2️⃣ Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your OpenAI API key

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here

▶️ Running the Application

Start the Streamlit app:

streamlit run app.py


The browser will open automatically at:

http://localhost:8501

🎤 How to Use

Press Start Speaking

Answer the interview question naturally

Press Stop

The app will:

Convert your audio to text

Generate a short, human-like interview answer

Play back the answer through TTS

You can repeat this for any question like:

Tell me about yourself

What is your superpower?

How do you handle challenges?

What are your strengths/weaknesses?

🎯 Personalization (Important Feature)

The bot is fully personalized to behave as Ranjan Yadav, using the information from your actual resume:

B.Tech CSE

Data Analyst Internship

Projects

Skills (Python, SQL, ML, AI, LangChain, RAG, etc.)

Achievements (5-star SQL, 100+ DSA problems)

This allows the bot to answer interview questions in a realistic, accurate, confident tone.

📦 requirements.txt
streamlit
streamlit-mic-recorder
python-dotenv
openai>=1.55.0

🌐 Deployment (Optional)
Deploy to Streamlit Cloud

Go to: https://share.streamlit.io

Connect your GitHub repo

Add your OpenAI API key under Secrets

Deploy

📌 Notes

Whisper transcription + mini-models ensure low cost

The app is built to be simple, clean, and accessible

No coding knowledge needed for users — everything is in the UI

Manual stop button avoids auto-stop issues with browsers

Bot’s tone is intentionally short, warm, and human-like

🙋‍♂️ Developer

Ranjan Yadav

Email: ranjan83711yadav@gmail.com

LinkedIn: https://linkedin.com/in/

GitHub: https://github.com/
