import boto3


def do_translate(input, lang):
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    result = translate.translate_text(Text=input, SourceLanguageCode="en", TargetLanguageCode=lang)
    return result.get('TranslatedText')


# a = "Hello World"
# translated_text = do_translate(a)
# print(translated_text)
