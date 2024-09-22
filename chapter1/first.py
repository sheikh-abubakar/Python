print("hello")

# Module is a file containg the code written by somebody elsewhich can be imported andused in  ou code

# pip is is tha package manger by python. use pip to install module

# use ipmort keyword to add module
"""
so 
thank you
"""

import pyjokes

joke = pyjokes.get_joke()

print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()