# Test Driver Program


# import modules
from TV import TV
import PySimpleGUI as sg


# Define TestTV
def TestTV():

    # Create two objects
    tv1 = TV()
    tv2 = TV()

    # turn on tv1 and set its channel t0 30 and volume to 3
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    # Turn on tv2 and sets its channel to 3 and volume to 2
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
