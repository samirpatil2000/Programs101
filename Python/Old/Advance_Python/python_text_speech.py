import pyttsx3
engine = pyttsx3.init()
engine.say('Hey This is Samir')
engine.say('You Fucking asshole')
engine.runAndWait()

voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
engine.setProperty('voice', voice_id)
engine.say("Hii this is samir patil")
engine.runAndWait()


