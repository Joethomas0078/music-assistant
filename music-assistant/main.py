from email.mime import audio
import pygame
import pyttsx3
import speech_recognition as sr
import os
import sys

pygame.mixer.init()
#path of program and songs
path = "C:\\Users\\joeth\\OneDrive\\Attachments\\new\\proj\\pythonproj\\music-assistant\\"
songs = os.listdir(path)

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#voices[1] for female voice
#voices[0] for female voice
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 150)

engine.say("Hello sir, what i can play for you?")
engine.runAndWait()

while True:
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')

    except:
        pass # empty

    
    if "play" in query:
        if "play my favorite" in query:
           print("\nPlaying your favorite music sir\n")
           engine.say("Playing your favorite music sir")
           engine.runAndWait()
           pygame.mixer.music.load("kathal.mp3")
           pygame.mixer.music.play()

        else:
            for i in songs:
                if query[5:].lower() in i.lower():
                    print("\nPlaying, "+ query[5:])
                    print()
                    print("\nPlaying, "+ query[5:])
                    engine.runAndWait()
                    pygame.mixer.music.load(i)
                    pygame.mixer.music.play()
                    break

    elif "stop" in query:
        pygame.mixer.music.stop()
        engine.say("Music stopped")
        engine.runAndWait()
    
    elif "unpause" in query:
        pygame.mixer.music.unpause()
        engine.say("Music unpaused")
        engine.runAndWait()
        
    
    elif "pause" in query:
        pygame.mixer.music.pause()
        engine.say("Music paused")
        engine.runAndWait()
        
    
    elif "shutdown" in query:
        pygame.mixer.music.stop()
        engine.say("shutting down, Goodbye sir")
        engine.runAndWait()
        sys.exit()