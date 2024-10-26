import boto3
import os
import glob

def do_translate(input, lang):
    delete_existing_audio_files()
    translate = boto3.client(service_name='translate', region_name='ca-central-1', use_ssl=True)
    result = translate.translate_text(Text=input, SourceLanguageCode="en", TargetLanguageCode=lang)
    return result.get('TranslatedText')


# New function to convert translated text to speech
def text_to_speech(text, output_file):
    polly_client = boto3.client("polly", region_name="ca-central-1")
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"  # Adjust as desired
    )
    with open(output_file, "wb") as file:
        file.write(response["AudioStream"].read())

def delete_existing_audio_files():
    # Delete all mp3 files in the static directory
    files = glob.glob("static/*.mp3")
    for file_path in files:
        os.remove(file_path)