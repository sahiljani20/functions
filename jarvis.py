# import pyttsx3
# import webbrowser
# import smtplib
# import random
# import speech_recognition as sr
# import wikipedia
# import datetime
# import wolframalpha
# import os
# import sys



# engine = pyttsx3.init('sapi5')



# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[len(voices)-1].id)

# def speak(audio):
#     print('Computer: ' + audio)
#     engine.say(audio)
#     engine.runAndWait()

# def greetMe():
#     currentH = int(datetime.datetime.now().hour)
#     if currentH >= 0 and currentH < 12:
#         speak('Good Morning!')

#     if currentH >= 12 and currentH < 18:
#         speak('Good Afternoon!')

#     if currentH >= 18 and currentH !=0:
#         speak('Good Evening!')

# greetMe()

# speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
# speak('How may I help you?')


# # def myCommand():
   
# #     r = sr.Recognizer()                                                                                   
# #     with sr.Microphone() as source:                                                                       
# #         print("Listening...")
# #         r.pause_threshold =  1
# #         audio = r.listen(source)
# #     try:
# #         query = r.recognize_google(audio, language='en-in')
# #         print('User: ' + query + '\n')
        
# #     except sr.UnknownValueError:
# #         speak('Sorry sir! I didn\'t get that! Try typing the command!')
# #         query = str(input('Command: '))

# #     return query
        

# # if __name__ == '__main__':

# #     while True:
    
# #         query = myCommand();
# #         query = query.lower()
        
# #         if 'open youtube' in query:
# #             speak('okay')
# #             webbrowser.open('www.youtube.com')

# #         elif 'open google' in query:
# #             speak('okay')
# #             webbrowser.open('www.google.co.in')

# #         elif 'open gmail' in query:
# #             speak('okay')
# #             webbrowser.open('www.gmail.com')

# #         elif "what\'s up" in query or 'how are you' in query:
# #             stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
# #             speak(random.choice(stMsgs))

# #         elif 'email' in query:
# #             speak('Who is the recipient? ')
# #             recipient = myCommand()

# #             if 'me' in recipient:
# #                 try:
# #                     speak('What should I say? ')
# #                     content = myCommand()
        
# #                     server = smtplib.SMTP('smtp.gmail.com', 587)
# #                     server.ehlo()
# #                     server.starttls()
# #                     server.login("Your_Username", 'Your_Password')
# #                     server.sendmail('Your_Username', "Recipient_Username", content)
# #                     server.close()
# #                     speak('Email sent!')

# #                 except:
# #                     speak('Sorry Sir! I am unable to send your message at this moment!')


# #         elif 'nothing' in query or 'abort' in query or 'stop' in query:
# #             speak('okay')
# #             speak('Bye Sir, have a good day.')
# #             sys.exit()
           
# #         elif 'hello' in query:
# #             speak('Hello Sir')

# #         elif 'bye' in query:
# #             speak('Bye Sir, have a good day.')
# #             sys.exit()
                                    
# #         elif 'play music' in query:
# #             music_folder = Your_music_folder_path
# #             music = [music1, music2, music3, music4, music5]
# #             random_music = music_folder + random.choice(music) + '.mp3'
# #             os.system(random_music)
                  
# #             speak('Okay, here is your music! Enjoy!')
            

# #         else:
# #                 webbrowser.open('www.google.com')
        
# #         speak('Next Command! Sir!')
        


# import pyttsx

# engine = pyttsx.init()
# engine.say('Good morning.')
# engine.runAndWait()



# import speech_recognition as sr
# import webbrowser as wb
# import speak

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print ('Say Something!')
#     audio = r.listen(source)
#     print ('Done!')
 
# try:
#     text = r.recognize_google(audio)
#     print('Google thinks you said:\n' + text)
#     lang = 'en'

#     speak.tts(text, lang)

#     f_text = 'https://www.google.co.in/search?q=' + text
#     wb.get(chrome_path).open(f_text)
 
# except Exception as e:
#     print (e)





import speech_recognition as sr
from time import ctime
import time
import os,sys
from gtts import gTTS
import datetime

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        tts = gTTS(text='Good Morning!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    if currentH >= 12 and currentH < 18:
        tts = gTTS(text='Good Afternoon!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    if currentH >= 18 and currentH !=0:
        tts = gTTS(text='Good Evening!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

greetMe()


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=4)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio , language="en")
        print("You said: " + data)
        speak("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    if "hello" in data:
        data = data.split(" ")
        data2 = str(data[1])
        os.system("chromium-browser 'https://www.google.co.in/search?q='"+ data2  )
 
    if 'bye bye' in data or 'nothing' in data or 'abort' in data or 'stop' in data:
            speak('Bye Sir, have a good day.')
            sys.exit()       


# initialization
time.sleep(2)
speak("Hi Frank, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)



# import speech_recognition as sr

# # Record Audio
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# # Speech recognition using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
