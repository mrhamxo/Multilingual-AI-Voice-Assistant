import os
import uuid
import requests
from dotenv import load_dotenv
from gtts import gTTS
import speech_recognition as sr

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq-compatible API endpoint
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# --------------------------
#  Voice Input using Microphone
# --------------------------
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text using Google's free API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

# --------------------------
#  Generate LLM Response via Groq API
# --------------------------
def llm_model(user_text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",  # Auth header with API key
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                "Reply like a human in a conversation. Keep it short and friendly. "
                "Do not explain your thoughts. No tags like <think>, <reason>, or any system-like responses. "
                "Just return plain text, like a person talking."
                )
            },
            {"role": "user", "content": user_text}
        ],
        "temperature": 0.8
    }

    try:
        # Send POST request to Groq API
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        # Extract and return the generated message content
        return result["choices"][0]["message"]["content"].strip()

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return "Unexpected response format from Groq API."

# --------------------------
#  Convert Text to Speech (Multilingual)
# --------------------------
def text_to_speech(text, language="en"):
    # Generate TTS audio using gTTS
    tts = gTTS(text=text, lang=language)
    
    # Generate unique file name for each output
    file_name = f"output_{uuid.uuid4().hex[:8]}.mp3"
    file_path = os.path.join("output", file_name)

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # Save audio to file
    tts.save(file_path)

    return file_path  # Return path to audio file
