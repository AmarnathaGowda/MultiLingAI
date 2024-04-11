from setuptools import setup,find_packages

setup(
    name='Multilingual assistant',
    version='0.1.0',
    description='A project template for multilingual assistant',
    author='Amarnatha Gowda',
    author_email='amarnathagowdat@gmail.com',
    packages=find_packages(),
    license='MIT',
    install_requires=['SpeechRecognition','pipwin','pyaudio','gTTS','google-generativeai','pyhton-package','streamlit']
)