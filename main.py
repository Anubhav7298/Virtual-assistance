import speech_recognition as sr
import pyttsx3
import webbrowser

r1 = sr.Recognizer()

engine = pyttsx3.init()
engine.say("speak now")
engine.runAndWait()


def fun(url1, text1):
    try:
        engine1 = pyttsx3.init()
        engine1.say(f"searching for {text1}")
        engine1.runAndWait()
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url1)

    except sr.UnknownValueError:
        print("the program could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("speak now")
    audio = r1.listen(source)
    text = r1.recognize_google(audio)


if 'search' in text:
    text = text[7:]
    url = f"https://www.google.com/search?q={text}"
    fun(url, text)

if 'play' in text:
    text = text[5:]
    url = f"https://www.youtube.com/results?search_query={text}"
    fun(url, text)
