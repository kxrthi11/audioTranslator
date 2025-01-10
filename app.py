import gradio as gr
import speech_recognition as sr
from deep_translator import GoogleTranslator

# Function to transcribe audio to text
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        return f"Error transcribing audio: {e}"

# Function to translate text
def translate_text(text, target_language):
    try:
        return GoogleTranslator(source='auto', target=target_language).translate(text)
    except Exception as e:
        return f"Error translating text: {e}"

# Combined function for Gradio
def audio_to_translation(audio_file, target_language):
    text = transcribe_audio(audio_file)
    if "Error" in text:
        return text
    translation = translate_text(text, target_language)
    return translation

# Gradio Interface
def interface():
    inputs = [
        gr.Audio(type="filepath", label="Record or Upload Audio"),
        gr.Textbox(value="en", label="Target Language (e.g., 'fr' for French, 'es' for Spanish)"),
    ]
    outputs = gr.Textbox(label="Translated Text")

    return gr.Interface(
        fn=audio_to_translation,
        inputs=inputs,
        outputs=outputs,
        title="Audio Translator",
        description="Record or upload audio, then translate the transcribed text into a target language."
    )

if __name__ == "__main__":
    interface().launch()
