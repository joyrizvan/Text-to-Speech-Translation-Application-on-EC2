from flask import Flask, render_template, request
import os
from translate import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method=='POST':
        input=request.form.get("input_text")
        selected_lang=request.form.get("language",None)
        if selected_lang is not None:
            lang=selected_lang
            translate=do_translate(input, lang)
        return render_template ("index.html", input=input, lang=lang, translate=translate)

#Insert the line below to to run on Cloud9    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug(True)