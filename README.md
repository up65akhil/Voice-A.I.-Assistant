# Voice A.I. Assistant 🎙️

A hands-free, voice-activated personal desktop assistant built with Python named Nexus AI Assistant. This assistant leverages the power of Google's **Gemini 2.5 Flash** for intelligent conversation and utilizes the native Windows **SAPI (Speech API)** for offline, zero-cost voice feedback.

## ✨ Features

* **Conversational AI:** Powered by Google Gemini 2.5 Flash for rapid, context-aware responses and intelligent reasoning.
* **100% Free Voice Engine:** Uses the built-in Windows SAPI voice (`pywin32`), removing any dependency on external paid text-to-speech APIs.
* **Smart Web Automation:** Voice-controlled searching across Google, Wikipedia, and YouTube.
* **Local App Launcher:** Seamlessly opens desktop applications like WhatsApp and Telegram directly via voice commands.
* **Automated Environment Setup:** Intelligently prompts for the Gemini API key on the first run and securely saves it locally to a `.env` file.
* **Response Logging:** Automatically saves detailed AI text responses to a local file (`AI_Response.txt`) and opens it for easy viewing.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Engine:** `google-genai`
* **Voice Output Engine:** `pywin32` (Windows SAPI)
* **Speech Recognition Input:** `SpeechRecognition`
* **Environment Management:** `python-dotenv`

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/up65akhil/Voice-AI-Assistant.git](https://github.com/up65akhil/Voice-AI-Assistant.git)
cd Voice-AI-Assistant
```
### 2. Install Dependencies
Make sure you have Python installed, then install the required libraries:
```bash
pip install google-genai python-dotenv SpeechRecognition pywin32
```
### 3. API Key Setup
You only need a single free API key to run this assistant:
Google Gemini API Key: Get it here from Google AI Studio
You do not need to create a .env file manually. Just run the script, and the assistant will automatically ask you to paste your key on the first boot.

### 💻 Usage
Run the main script from your command prompt or terminal:
```bash
python main.py
Example Voice Commands:

"Open YouTube" (or Wikipedia, Google, Instagram, Mail, LinkedIn, Gemini)

"Search on Google" -> The assistant will ask you what you want to search for.

"Open Telegram" or "Open WhatsApp"

"Using artificial intelligence [your question]" -> The assistant will look up your request using Gemini, save it to a text file, and read the summary out loud.

"Exit Nexus" or "Stop Listening" -> Safely terminates the program.
```

### 📦 Building a Standalone Executable
To run your Voice A.I. Assistant without opening a terminal or needing Python installed on the host machine, compile it into a single .exe file using PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile main.py
Your compiled standalone application will be generated inside the dist/ folder as main.exe.
```
### 👨‍💻 Author
Akhil Singh

GitHub: @up65akhil
