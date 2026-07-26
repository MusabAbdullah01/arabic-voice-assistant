# 🎙️ Real-time Arabic Voice Assistant with Speech-to-Text & Text-to-Speech

A full-stack, local Arabic Voice Assistant pipeline built with Python. This project converts localized spoken Arabic audio into text, processes the context using Cohere's Large Language Model (LLM), and returns an audio response in natural Arabic speech.

---

## 🚀 Key Features

* **Local Speech-to-Text (STT):** Powered by **OpenAI's Whisper** model, enabling offline, highly accurate Arabic speech transcription.
* **Custom Vocabulary Prompting:** Uses custom initial prompts to accurately transcribe specific proper nouns and technical terms (e.g., "Engineer Musab").
* **RTL Arabic Display Fix:** Integrated `arabic_reshaper` and `python-bidi` to fix disconnected and reversed Arabic text issues inside standard terminals/consoles.
* **Intelligent LLM Responses:** Integrates with Cohere's API (`command-r7b-arabic-02-2025`) configured with dynamic system personas.
* **Arabic Text-to-Speech (TTS):** Leverages `gTTS` and `pygame` for smooth, high-quality Arabic audio synthesis and playback.

---

## 🛠️ Architecture Pipeline

1. **Audio Input:** Accepts localized `.wav` audio files.
2. **Transcription:** Transcribes the input audio locally using Whisper (`small` model).
3. **LLM Processing:** Passes the transcribed prompt along with system context (`SystemMessage`) to Cohere LLM.
4. **Terminal Output:** Reshapes and displays both input prompt and AI response correctly in the terminal.
5. **Speech Generation:** Converts the generated text response into an MP3 file via `gTTS` and plays it back asynchronously using `pygame`.

---

## 🧰 Tech Stack & Prerequisites

* **Language:** Python 3.10+
* **Speech Recognition:** `openai-whisper`
* **Text-to-Speech & Audio:** `gTTS`, `pygame`, `pydub`
* **LLM Orchestration:** `langchain-cohere`
* **Text Processing:** `arabic-reshaper`, `python-bidi`

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MusabAbdullah01/arabic-voice-assistant.git](https://github.com/MusabAbdullah01/arabic-voice-assistant.git)
   cd arabic-voice-assistant
   ```

2. **Install required dependencies:**
   ```bash
   pip install openai-whisper gTTS pygame langchain-cohere arabic-reshaper python-bidi pydub SpeechRecognition
   ```

3. **Set up Environment Variables:**
   Add your Cohere API key to your environment variables or direct runtime config:
   ```bash
   export COHERE_API_KEY="your_cohere_api_key_here"
   ```

---

## 🖥️ Usage

Run the main application script:

```bash
python app.py
```

### Example Terminal Output:
```text
Transcribing audio file locally with Whisper...

>>> Transcribed Text: السلام عليكم ورحمة الله وبركاته أنا المهندس مصعب عبدالله
<<< Bot: وعليكم السلام ورحمة الله وبركاته! مرحبا مصعب، أنا لينا...

Playing spoken response...
```

---

## 👨‍💻 Author

**Mosaab Abdullah**
* GitHub: [@MusabAbdullah01](https://github.com/MusabAbdullah01)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
