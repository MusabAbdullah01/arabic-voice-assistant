import os
import time
import threading
import nltk

try:
    nltk.pause()
except Exception:
    pass

import whisper
import arabic_reshaper
from bidi.algorithm import get_display
from gtts import gTTS
import pygame
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage

def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def play_arabic_audio(text):
    try:
        tts = gTTS(text=text, lang='ar')
        audio_file = "temp_response.mp3"
        tts.save(audio_file)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()
        if os.path.exists(audio_file):
            os.remove(audio_file)
    except Exception as e:
        print(f"Error playing audio: {e}")

def process_audio_file(audio_path):
    if not os.path.exists(audio_path):
        print(f"Error: File '{audio_path}' not found!")
        return

    print("Transcribing audio file locally with Whisper...")
    try:
        model = whisper.load_model("small")
        result = model.transcribe(
            audio_path, 
            language="ar", 
            fp16=False,
            initial_prompt="المهندس مصعب عبدالله"
        )
        text = result["text"].strip()
        
        print(f"\n>>> Transcribed Text: {fix_arabic(text)}")
        
        response = llm.invoke(messages + [HumanMessage(content=text)])
        ai_reply = response.content
        
        print(f"<<< Bot: {fix_arabic(ai_reply)}\n")
        
        print("Playing spoken response...")
        play_arabic_audio(ai_reply)

    except Exception as e:
        print(f"Error processing audio: {e}")

if __name__ == "__main__":
    cohere_api_key = os.getenv("COHERE_API_KEY", "pdSVcptCGkjwmOAFtQB7Nlcv5zMjTIC7EGGY0zcF")
    llm = ChatCohere(
        model="command-r7b-arabic-02-2025", 
        cohere_api_key=cohere_api_key
    )

    scenario = "You are Lina, a 31 year old single woman and a journalist on vacation."
    messages = [SystemMessage(content=scenario)]

    audio_file_path = r"C:\Users\imm93b\Downloads\test_speech.wav"
    process_audio_file(audio_file_path)