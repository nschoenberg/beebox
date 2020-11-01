# Request module must be installed.
# Run pip install requests if necessary.
import requests
from datetime import datetime
import weather

speech_service_url = "https://westeurope.tts.speech.microsoft.com/cognitiveservices/v1"
subscription_key = ""
voice_template = '<speak version="1.0" xml:lang="de-DE"><voice xml:lang="de-DE" xml:gender="Female" name="de-DE-KatjaNeural">{}</voice></speak>'
headers = {
    "Ocp-Apim-Subscription-Key": "",
    "Content-Type" : "application/ssml+xml",
    "X-Microsoft-OutputFormat" : "audio-16khz-64kbitrate-mono-mp3",
    "User-Agent" : "curl"
}

def to_file(text):
    global subscription_key
    if not subscription_key:
        print("Trying to read azure cognitive services subscribtion key from file")
        with open('./beebox/speek_secret', 'r') as secret_file:
            subscription_key = secret_file.read()
            headers["Ocp-Apim-Subscription-Key"] = subscription_key

    if (text.find("%time%") != -1):
        text = text.replace("%time%", get_time())
    
    if (text.find("%weather_info%") != -1):
        text = text.replace("%weather_info%", weather.get_description())
    
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    # print(text)
    response = requests.post(speech_service_url, headers=headers,data=voice_template.format(text))
    if (response.status_code == 200):
        with open("/var/lib/mpd/music/speech.wav", "wb") as fd:
            fd.write(response.content)
    else:
        print(response.status_code)
        print(response.reason)


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time