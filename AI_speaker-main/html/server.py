from flask import *


app = Flask(__name__)

import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound



#음성 인식(듣기, STT)
def listen(recognizer, audio):
    try:
        global questioner
        text = recognizer.recognize_google(audio, language='ko')
        tioner = '[질 문 자] : '+ text
        questioner = tioner
        print(tioner)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패!')
    except sr.RequestError as e:
        print('요청 실패! : {0}'.format(e))

#대답
def answer(input_text):
    answer_text = ''
    
    global answer
    
    if '안녕' in input_text:
        answer_text = '안녕하세요!'
        answer = answer_text
    elif '날씨' in input_text:
        answer_text = '오늘 부산의 기온은 20도 입니다!'
        answer = answer_text
    elif '환율' in input_text:
        answer_text = '원 달러의 환율은 1400원 입니다!'
        answer = answer_text
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
        answer = answer_text
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요!'
        answer = answer_text
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한번 말씀해주시겠어요?'
        answer = answer_text
    speak(answer_text)


#소리내서 읽기(TTS)
def speak(text):
    global prints
    prints = '[인공지능] : ' + text
    print(prints)
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

# while True:
#     time.sleep(0.1)


@app.route('/', methods=['GET','POST'])
def index():
    # if prints in text:

    printss = prints
    # else:
    #     pass
    # if qquestioner in text: 
    qquestioner = questioner
    # else:
    #     pass
    return render_template('html.html', AI=printss, questioners = qquestioner)

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, debug=True)