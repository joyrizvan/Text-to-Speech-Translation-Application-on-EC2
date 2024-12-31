from flask import Flask, request, render_template
import os
from translate import *
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index_a.html")


@app.route('/', methods=['POST'])
def main():
    audio_url = ""
    if request.method == 'POST':
        input_text = request.form.get("input_text")
        selected_lang = request.form.get("language", None)

        if selected_lang is not None and input_text:
            # Call the translation function
            translated_text = do_translate(input_text, selected_lang)

            # Delete previous mp3 files
            delete_existing_audio_files()

            # Generate audio file path
            timestamp = int(time.time())  # Current timestamp
            audio_file_name = f"output_{timestamp}.mp3"
            audio_file_path = os.path.join("static", audio_file_name)

            # Generate speech audio from translated text
            text_to_speech(translated_text, audio_file_path)

            # URL for the audio file to access from HTML
            audio_url = f"/{audio_file_path}"

            return render_template("index_a.html", input=input_text, lang=selected_lang, translate=translated_text, audio_url=audio_url)

    return render_template("index_a.html")
#Insert the line below to to run on Cloud9    
#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug(True)