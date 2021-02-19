import speech_recognition as sr # to understand whatever the humans speak and converts the speech to text.
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files  
from time import ctime # to get time details
import webbrowser # to open browser
from selenium import webdriver
from datetime import datetime  #it works on date and time
from datetime import date  #it works on date and time
import pyjokes # to drop a random joke 
import ctypes
import time #helps us to display time
import winsound
from pygame import mixer 
from pygame.locals import *
import random
from selenium import webdriver


num = 1

# function used to play the text. 
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PepSa : ", output) 
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 

#funcyion to get the audio of user
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You said: ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return 0 

# function used to process the input
# to perform the specified query .
def process_text(input): 
    try: 
        
        if "functionality" in input:
            commands = '''To open youtube, say search or play youtube  
            To open chrome, say search google 
            To open wikipedia, say search wikipedia
            To lauch applications like chrome,excel,word, say open
            To know about me, say define yourself
            To know about my CREATORS, say who created you 
            To study, say what topic we are going to study today '''
            
            ans = """I can do lots of things, for example you can ask 
            me time, date, some specific questions, I can open websites
            for you, launch application and more. See the list of commands-"""
            
            assistant_speaks(ans)
            assistant_speaks(commands) 
            return
        
        elif 'search' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
        
        elif 'open' in input: 
            open_application(input.lower()) 
            return
        
        elif 'close' in input: 
            close_application(input.lower()) 
            return 
        
        elif 'music' in input.lower(): 
            playMusic() 
            return        

        elif "who are you" in input or "define yourself" in input: 
            speak = '''Hello, I am Pepsa. Your personal Assistant. 
            I am here to make your life easier. You can command me 
            to perform various tasks such as searching webs or 
            opening applications or answering your queries, Et cetera'''
            assistant_speaks(speak) 
            return

        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by Himanshu, Ankita and Akrity."
            assistant_speaks(speak) 
            return

        elif "college" in input.lower(): 
            speak = '''Indian Institute of Information Technology, 
            Allahabad (IIIT-Allahabad) is a public university located 
            in Allahabad (Jhalwa, Allahabad), in Uttar Pradesh''' 
            assistant_speaks(speak) 
            return

        elif "what topic" in input: # just 
            speak = '''We will study Programming Practices.
            Which topic do you want to study??'''
            assistant_speaks(speak) 
            text = get_audio().lower() 
            open_application(text.lower())
            return    

        elif "branch" in input.lower(): # just 
            speak = " " "You study in Information Technology" " "
            assistant_speaks(speak) 
            return

        elif 'created' in input:
            assistant_speaks("I am created to demostrate the Programming Practices studied ")   
            return

        elif "date" in input:
            today = date.today()
            assistant_speaks(today)
            return

        elif "time" in input:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")   
            assistant_speaks(current_time)
            return

        elif 'joke' in input: 
            assistant_speaks(pyjokes.get_joke())    
            return

        else: 
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio()
            input="search"+input 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    
    except : 

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        input="search"+input
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input) 

# function used to seach the 
# user queries on web. 
def search_web(input): 
    browser = webdriver.Firefox()
    if 'wikipedia' in input.lower(): 

        assistant_speaks("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        url = f"https://en.wikipedia.org/wiki/" + '_'.join(query)
        browser.get(url)
        return

    elif 'youtube' in input.lower(): 
  
        assistant_speaks("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        url = f"https://www.youtube.com/results?search_query={query}"
        browser.get(url)
        return 
    
    elif 'google' in input: 
        
        assistant_speaks("Opening in google") 
        indx = input.lower().split().index('google') 
        query = input.split()[indx + 1:] 
        url = f"https://google.com/search?q={query}"
        browser.get(url) 
        return

    else: 
        indx = input.lower().split().index('search') 
        query = input.split()[indx + 1:] 
        url = f"https://google.com/search?q={query}"
        browser.get(url) 
        assistant_speaks("This is what I found for you")  
        return


# function used to open application 
# present inside the system. 
def open_application(input): 

    if "chrome" in input: 
        assistant_speaks("Opening Google Chrome") 
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        return

    elif "edge" in input : 
        assistant_speaks("Opening Microsoft Edge") 
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        return
    
    
     
    
    elif "word" in input: 
        assistant_speaks("Opening Microsoft Word") 
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\MICROSOFT WORD 2010.lnk")
        return

    elif "powerpoint" in input: 
        assistant_speaks("Opening Microsoft PowerPoint") 
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\MICROSOFT POWERPOINT 2010.lnk")
        return
    
    elif "tutorial" in input.lower():
        assistant_speaks("Opening PPR Tutorial") 
        if "shell" in input.lower() or "script" in input.lower():
            os.system(r"C:\Users\New\shell.pdf")
            return
        if "data" in input.lower():
            os.system(r"C:\Users\New\data.pdf")
            return
        if "oops" in input.lower():
            os.system(r"C:\Users\New\oops.pdf")  
            return  
       
    elif "assignment" in input:
        assistant_speaks("Opening PPR Assignment") 
        if "shell" in input.lower():
            os.system(r"C:\Users\New\shell_assignment.pdf")
        if "data" in input.lower():
            os.system(r"C:\Users\New\array_assignment.pdf")
        if "tree" in input.lower():
            os.system(r"C:\Users\New\tree_assignment.pdf")    
        return

    
    else: 
        assistant_speaks("Application not available") 
        return

# function used to close application 
# present inside the system. 
def close_application(input): 

    if "chrome" in input: 
        assistant_speaks("Closing Google Chrome") 
        os.system("taskkill /f /im chrome.exe")
        return

    elif "firefox" in input or "mozilla" in input: 
        assistant_speaks("Closing Mozilla Firefox") 
        os.system("taskkill /f /im firefox.exe")
        return

    elif "word" in input: 
        assistant_speaks("Closing Microsoft Word") 
        os.system("taskkill /f /im winword.exe")
        return
    
    elif "edge" in input: 
        assistant_speaks("Closing Microsoft Edge") 
        os.system("taskkill /f /im msedge.exe")
        return    
    else: 
        assistant_speaks("Application not found/opened") 
        return

# function used to extract the hour  
# and greet the user appropriately.
def wishMe(): 
    hour = int(datetime.now().hour) 
    if hour>= 0 and hour<12: 
        assistant_speaks("Good Morning  !") 
   
    elif hour>= 12 and hour<18: 
        assistant_speaks("Good Afternoon  !")    
   
    else: 
        assistant_speaks("Good Evening  ") 
    assistant_speaks("I am Pepsa, your Assistant")  

# function used to select the random song  
# from the list and .
def playMusic():
    L = [r'C:\Users\New\Woh Chaand Kahan Se Laogi.mp3', 
        r'C:\Users\New\First Kiss - Yo Yo Honey Singh.mp3', 
        r'C:\Users\New\Rona Likha Tha - Ramji Gulati.mp3',
        r'C:\Users\New\Shona Shona - Tony Kakkar.mp3',
        r'C:\Users\New\Tanhaai - Tulsi Kumar.mp3'
        ]
    #S = random.randint(0, len(L))
    mixer.init()
    mixer.music.set_volume(0.50)
    filename = random.choice(L)
    mixer.music.load( filename )
    mixer.music.play( )

    # infinite loop 
    while True: 
       print("Press 'p' to pause, 'r' to resume") 
       print("Press 'e' to exit the program") 
       query = input("  ") 
       if query == 'p': 
  
          # Pausing the music 
          mixer.music.pause()      
       elif query == 'r': 
  
          # Resuming the music 
          mixer.music.unpause() 
       elif query == 'e': 
  
          # Stop the mixer 
          mixer.music.stop() 
          break


  
# Driver Code 
if __name__ == "__main__": 
    ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon.jpg", 0)
    music_dir = r"C:\Users\Nikhil Kumar\Downloads\never.mp3"
    winsound.PlaySound("music_dir", winsound.SND_ASYNC | winsound.SND_ALIAS )
    #random = os.startfile(music_dir)
    assistant_speaks("What's your name, Human?") 
    name ='Human'
    name = get_audio() 
    assistant_speaks("Hello, " + name + '.') 
    wishMe()
    
      
    while(1): 
        input("Press Enter to continue...")
        assistant_speaks("What can i do for you?") 
        text = get_audio().lower() 
  
        if text == 0: 
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "stop" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            music_dir = r"C:\Users\Nikhil Kumar\Downloads\never.mp3"
            winsound.PlaySound("music_dir", winsound.SND_ASYNC | winsound.SND_ALIAS )
            ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Desktop\Akrity\bg.jpg", 0)
            break
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon1.jpg", 0)
        time.sleep(1.0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon2.jpg", 0)
        time.sleep(1.0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon3.jpg", 0)
        time.sleep(1.0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon4.jpg", 0)
        time.sleep(1.0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon5.jpg", 0)
        time.sleep(1.0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,r"C:\Users\Nikhil Kumar\Downloads\neon6.jpg", 0)
        time.sleep(1.0)
        
           
  
        # calling process text to process the query 
        process_text(text) 
        