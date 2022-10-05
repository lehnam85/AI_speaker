import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있습니다!')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='ko')
    print(text)
except sr.UnknownValueError:
    print('인식 실패!')
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e))