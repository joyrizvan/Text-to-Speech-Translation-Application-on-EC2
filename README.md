# Text to Speech Translation Application on Amazon EC2
## Author - Rizvan Nahif
### Description
This application allows users to enter text on a web interface, which is then translated to a language (Spanish or French) using Amazon Translate and converted to audio using Amazon Polly. 
The translated text is played back as audio directly on the web interface.

# Project Structure
Text-to-Speech-Translation-Application-on-EC2/
    ├───static                                     # This is where the audio files generated gets saved
    ├───templates                                  
    |    ├──index_a.html                           # The HTML for the web page
    |───run.py                                     # This file renders the HTML and runs the server
    |───translate.py                               # This file contains all the functions for translating and converting text to speech

# Execution Steps
- Make sure to edit the ip and the port in run.py
- Run run.py
    
