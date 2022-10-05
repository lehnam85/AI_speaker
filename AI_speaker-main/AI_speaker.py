# from urllib import request, response
# from bs4 import BeautifulSoup as bs
# import requests
# USD_KRW_url = 'https://kr.investing.com/currencies/usd-krw'

import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound



#음성 인식(듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[질 문 자] : '+ text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패!')
    except sr.RequestError as e:
        print('요청 실패! : {0}'.format(e))

#대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요! 좋은 아침이네요!'
    elif '날씨' in input_text:
        answer_text = '오늘 부산의 기온은 20도 입니다!'
    elif '환율' in input_text:
        answer_text = '원 달러의 환율은 1400원 입니다!'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요!'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한번 말씀해주시겠어요?'
    speak(answer_text)


#소리내서 읽기(TTS)
def speak(text):
    print('[인공지능] : ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        time.sleep(1)
        os.remove(file_name)



r = sr.Recognizer()
mc = sr.Microphone()
speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(mc, listen)

while True:
    time.sleep(0.1)

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('듣고 있습니다!')
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio, language='ko')
#     print(text)
# except sr.UnknownValueError:
#     print('인식 실패!')
# except sr.RequestError as e:
#     print('요청 실패 : {0}'.format(e))


