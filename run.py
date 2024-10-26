from flask import Flask, request, render_template
import os
from translate import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index_a.html")

@app.route('/', methods=['POST', 'GET'])
def main():
    audio_url = ""
    if request.method=='POST':
        input=request.form.get("input_text")
        selected_lang=request.form.get("language",None)
        if selected_lang is not None:
            lang=selected_lang
            translate=do_translate(input, lang)
        # Delete previous mp3 files
        #delete_existing_audio_files()
        # Generate audio file path
        audio_file = "static/output.mp3"

        # Generate speech audio from translated text
        text_to_speech(translate, audio_file)
        audio_url = f"/{audio_file}"  # URL for the audio file to access from HTML

        return render_template("index_a.html", input=input, lang=selected_lang, translate=translate, audio_url=audio_url)


if __name__ == '__main__':
    app.run()
    app.debug(True)