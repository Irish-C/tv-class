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

    TestTV_layout = [
        [sg.Frame('TV1'), [
            [sg.Text(f"TV1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")],]],
        [sg.Frame('TV2'), [
            [sg.Text(f"TV2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")],]]
    ]

    # Create TestTV window
    TestTV_window = sg.Window('Test Driver Program', TestTV_layout)
    
    TestTV_window.read()