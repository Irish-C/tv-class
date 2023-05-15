# Test Driver Program
# 

# import modules
from TV import TV
import PySimpleGUI as sg


# Define TestTV
def TestTV():
    # Insert theme
    sg.theme('LightBlue')

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

    # Place two objects into TestTV layout
    TestTV_layout = [
        [sg.Text('TEST TV', font=('8514oem', 16))],
        [sg.Frame('', [[sg.Text(f"TV1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}.", size=(35,1), font=('Elephant',12))]], border_width=3)],
        [sg.Frame('', [[sg.Text(f"TV2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}.", size=(35,1), font=('Elephant',12))]], border_width=3)]
    ]

    # Create TestTV window
    TestTV_window = sg.Window('Test Driver Program', TestTV_layout, size=(400, 150))
    
    # Read and close window
    TestTV_window.read()
    TestTV_window.close()

if __name__ == '__main__':
    TestTV()