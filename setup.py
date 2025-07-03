from setuptools import find_packages, setup

setup(
    name = "multilingual AI Voice Assistant",
    version= "0.0.0",
    author="Muhammad Hamza",
    author_email="mr.hamxa942@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)
