# 🎙️ Multilingual AI Voice Assistant

A real-time voice-based assistant that listens to your speech, understands your question using an advanced LLM (via Groq API), and responds with a natural-sounding voice and supporting multiple languages.

## 🚀 Features

- 🎧 **Voice Input** using microphone
- 🤖 **LLM Responses** using Groq API (`llama-3.3-70b-versatile`)
- 🔊 **Text-to-Speech (TTS)** using `gTTS` in multiple languages (English, Urdu, Hindi, French, Spanish)
- 🧠 **Conversational History** with playback and download
- 🌐 Built with **Streamlit** for a clean, interactive UI

## 📦 Tech Stack

| Component        | Technology             |
|------------------|-------------------------|
| LLM Backend      | Groq API (DeepSeek, Mixtral, LLaMA3) |
| Voice Recognition| `speech_recognition` (Google Speech API) |
| Text-to-Speech   | `gTTS` (Google Text-to-Speech) |
| Web UI           | Streamlit              |
| Env Management   | Python `dotenv`        |

## 📁 Project Structure

```

📦 voice-assistant/
│
├── .env                     # API key for Groq
├── app.py                  # Streamlit frontend
├── requirements.txt        # Python dependencies
├── output/                 # Saved audio responses
├── research/               # Saved trails.ipynb
  └── trails.ipynb          # Experiments  
└── src/
  └── helper.py           # Core logic (voice, LLM, TTS)

````

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
````

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv myenv
source myenv/bin/activate      # Linux/macOS
myenv\Scripts\activate         # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Groq API Key

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=sk-your-key-here
```

### 5. Run the App

```bash
streamlit run app.py
```

## 🌍 Supported Languages

You can select the output language for speech in:

* English (`en`)
* Urdu (`ur`)
* Hindi (`hi`)
* French (`fr`)
* Spanish (`es`)

## 🖼️ Demo Screenshot

![Image](https://github.com/user-attachments/assets/5ee0b13b-9a1f-4b9a-937a-f2ccf4bf0271)

## 👨‍💻 Author

**Muhammad Hamza**
🔗 [LinkedIn](https://linkedin.com/in/muhammad-hamza-khattak/) | 🔗 [GitHub](https://github.com/mrhamxo)

## 🛡️ License

MIT License – free to use and modify.
