import speech_recognition as sr
import google.generativeai as geanai
from dotenv import load_dotenv
import os
from gtts import gTTS
import streamlit as st

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

geanai.configure(api_key=GOOGLE_API_KEY)
model = geanai.GenerativeModel('models/gemini-pro')

def voice_input():
    text = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try: 
        if audio != None:
            print("audio recived")
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
         st.text("Speech Recognition could not understand audio")
         return None 
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        return None
    return text

def text_to_speech(text):
    gTTS(text=text, lang="en", slow=False).save("audio.mp3")

def llm_model_object(user_input):
    # model = "models/gemini-pro"
    if user_input == "":
        return "Please provide some input"
    
    
    
    response = model.generate_content("Provide the out for this question in the human format, the slang should be in the form of human and it should be polite. The answer should be short and sweet. The question is "" " +user_input+" " )
    print(response.text)
    return response.text
