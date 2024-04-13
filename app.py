import streamlit as st
from src.helper import voice_input,llm_model_object, text_to_speech
import base64


def main():
    st.title("Multilingual AI Voice Assistant ")
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            print('Input text :'+ text)
            st.text("Speech Recognition thinks you said: " + text)
            print("Speech Recognition thinks you said: " + text)
            response = llm_model_object(text)
            text_to_speech(response)


            audio_file = open("audio.mp3","rb")
            audio_bytes = audio_file.read()

            st.text_area(response)
            st.audio(audio_bytes,)
            # st.download_button(label="Download audio", data=audio_bytes, file_name="audio.mp3", mime="audio/mp3")

if __name__ == "__main__":
    main()