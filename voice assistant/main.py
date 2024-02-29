import speech_recognition as speech_rec
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = speech_rec.Recognizer()
assistant = pyttsx3.init()

def talk(text):
    assistant.say(text)
    assistant.runAndWait()

def input_instruction():
    try:
        with speech_rec.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            instruction = listener.recognize_google(audio)
            instruction = instruction.lower()
            if "stop running" in instruction:
                return "stop"
            elif "ghost" in instruction:
                instruction = instruction.replace('ghost', '').strip()
                print(instruction)
                return instruction
    except Exception as e:
        print(e)

def play_ghost():
    while True:
        instruction = input_instruction()
        if instruction == "stop listening":
            talk("Goodbye have a great day!")
            break
        if instruction is None:
            continue  # Skip processing if instruction is None
        print(instruction)
        if "play" in instruction:
            song = instruction.replace('playing', "").strip()
            talk("playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is '+ current_time)
        elif 'date' in instruction:
            current_date = datetime.datetime.now().strftime('%d  %m %Y')
            talk("Today's date is " + current_date)
        elif 'how are you' in instruction:
            talk("I'm fine, Thank you for asking. How about you?")
        elif 'who built you' in instruction:
            talk('I am Ghost, a virtual assistant developed by Mr. Akindu.')
        elif 'who is' in instruction or 'what is' in instruction:
            query = instruction.replace('who is', " ").replace('what is', " ").strip()
            information = wikipedia.summary(query, sentences=1)
            print(information)
            talk(information)
        else:
            talk('Please repeat the question.')

play_ghost()
