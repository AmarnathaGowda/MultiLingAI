# Multilingual Assistant 
MULTILINGUAL AI VOICE ASSISTANT

Multilingual AI Voice Assistant. This tool is designed to understand and respond in multiple languages, making technology more accessible and connecting people across different cultures.

### Techstack Used:

- Python: For the backbone of the application, ensuring smooth and efficient processing.
- SpeechRecognition & PyAudio: For real-time voice data capture and processing, making the assistant      responsive and interactive.
- Google Generative AI & gTTS (Google Text-to-Speech): These powerful APIs empower the assistant to understand complex queries and speak in a clear, human-like voice in various languages.
- Streamlit: This awesome framework helped me build and share the application with a user-friendly web interface.

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/AmarnathaGowda/MultiLingAI.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

Link to create API key : https://aistudio.google.com/app/apikey

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up localhost:
```






