import speech_recognition as sr
import win32com.client
import webbrowser
import os
import urllib.parse
from google import genai
from dotenv import load_dotenv


def setup_api_key():
    load_dotenv()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("\n" + "="*40)
        print("   Nexus AI - FIRST TIME SETUP")
        print("="*40)
        print("To use the AI features, you need a free Gemini API key.")
        print("Get one here: https://aistudio.google.com/app/apikey")
        key = input("Paste your API key here and press Enter: ").strip()
        
        with open(".env", "w") as f:
            f.write(f"GEMINI_API_KEY={key}\n")
        print("Key saved successfully! Starting Jarvis...\n")
    return key

my_secret_key = setup_api_key()
client = genai.Client(api_key=my_secret_key)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = "Hello, I am Nexus A.I. Assistant" 


def generate_ai_response(prompt):
    speaker.Speak("Thinking... please wait a moment.") 
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        ) 
        
        filename = "AI_Response.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Your Request: {prompt}\n")
            file.write("-" * 40 + "\n\n")
            file.write(response.text)
        
        return filename
    except Exception as e:
        print(f"AI Error: {e}")
        speaker.Speak("I encountered an error connecting to the AI.")
        return None

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            return ""
        except Exception as e:
            return ""

if __name__ == "__main__":
    speaker.Speak(s)
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    onedrive_desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

    while True:
        print("\nListening....")
        text = takecommand()
        
        if not text:
            continue
        if "exit Nexus" in text or "stop listening" in text:
            speaker.Speak("Shutting down. Goodbye.")
            break

        if "search on google" in text or "google search" in text:
            speaker.Speak("What should I search for on Google?")
            query = takecommand()
            if query:
                speaker.Speak(f"Searching Google for {query}")
                search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
                webbrowser.open(search_url)
            continue

        if "search on wikipedia" in text or "wikipedia search" in text:
            speaker.Speak("What would you like to know from Wikipedia?")
            query = takecommand()
            if query:
                speaker.Speak(f"Searching Wikipedia for {query}")
                search_url = f"https://en.wikipedia.org/wiki/Special:Search?search={urllib.parse.quote(query)}"
                webbrowser.open(search_url)
            continue

        if "search on youtube" in text or "youtube search" in text:
            speaker.Speak("What should I search for on YouTube?")
            query = takecommand()
            if query:
                speaker.Speak(f"Searching YouTube for {query}")
                search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
                webbrowser.open(search_url)
            continue

        sites = [
            ['youtube', 'https://youtube.com'],['wikipedia', 'https://wikipedia.com'],['google', 'https://google.com'],['instagram', 'https://instagram.com'],['Gmail','https://mail.google.com/mail/'],['linkedin','https://www.linkedin.com/in/'],['Gemini','https://gemini.google.com/app?hl=en-IN']
        ]
        
        matched_site = False
        for site, url in sites:
            if f"open {site}" in text:
                speaker.Speak(f"Opening {site}")
                webbrowser.open(url)
                matched_site = True
                break
        if matched_site:
            continue

        apps = ['telegram', 'whatsapp']
        matched_app = False
        for app in apps:
            if f"open {app}" in text:
                speaker.Speak(f"Opening {app}")
                
                standard_shortcut = os.path.join(desktop_path, f"{app.title()} Desktop.lnk") if app == 'telegram' else os.path.join(desktop_path, f"{app.title()}.lnk")
                onedrive_shortcut = os.path.join(onedrive_desktop_path, f"{app.title()} Desktop.lnk") if app == 'telegram' else os.path.join(onedrive_desktop_path, f"{app.title()}.lnk")
                
                if os.path.exists(standard_shortcut):
                    os.startfile(standard_shortcut)
                elif os.path.exists(onedrive_shortcut):
                    os.startfile(onedrive_shortcut)
                else:
                    speaker.Speak(f"Could not find a desktop shortcut for {app}. Opening in browser instead.")
                    webbrowser.open(f"https://web.{app}.org" if app == 'telegram' else f"https://web.{app}.com")
                matched_app = True
                break
        if matched_app:
            continue

        if "using artificial intelligence" in text:
            clean_prompt = text.replace("using artificial intelligence", "").strip()
            if clean_prompt:
                saved_file = generate_ai_response(prompt=clean_prompt)
                if saved_file:
                    speaker.Speak("Done. Opening the response now.")
                    os.startfile(saved_file)
            else:
                speaker.Speak("What would you like me to ask the AI?")
            continue