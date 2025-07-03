import streamlit as st
from src.helper import voice_input, text_to_speech, llm_model

# Page Configuration
st.set_page_config(page_title="Multilingual AI Voice Assistant", layout="wide")

# Initialize Session State for Chat History
if "history" not in st.session_state:
    st.session_state.history = []

# App Header
st.markdown("## Multilingual AI Voice Assistant")

# Main Layout: Two Columns
col1, col2 = st.columns([1, 2])

# Start Listening Button
with col1:
    # Language Selection for Output Audio
    language = st.selectbox(
        "Select Output Language for Speech",
        options=["en", "ur", "hi", "fr", "es"],
        index=0,
        help="Choose language for voice output"
    )

    if st.button("Start Listening"):
        with st.spinner("Listening and processing..."):
            user_text = voice_input()                         # Speech to text
            response = llm_model(user_text)                   # LLM response
            output_path = text_to_speech(response, language)  # Text to speech

            # Save conversation to history
            st.session_state.history.append({
                "input": user_text,
                "response": response,
                "audio_path": output_path
            })

# Chat History and Audio Player
with col2:
    if st.session_state.history:
        st.markdown("### Chat History")

        for idx, interaction in enumerate(reversed(st.session_state.history), 1):
            with st.expander(f"Interaction #{len(st.session_state.history)-idx+1}"):
                st.markdown(f"**You said:** {interaction['input']}")
                st.text_area("AI Response", value=interaction["response"], height=150)

                # Load and play audio
                with open(interaction["audio_path"], "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")

                    # Download button
                    st.download_button(
                        label="Download Response",
                        data=audio_bytes,
                        file_name=f"response_{idx}.mp3",
                        mime="audio/mp3"
                    )

# Clear History Button
#st.markdown("---")
if st.button("Clear All"):
    st.session_state.history = []
    st.rerun()

# Footer
st.markdown("---")
st.markdown("Built by **Muhammad Hamza** — Powered by **Groq + gTTS + Streamlit**")