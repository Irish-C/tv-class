# Test Driver Program


# import modules
from TV import TV
import PySimpleGUI as sg

# Create TestTV window's content
sg.theme('DarkTeal4')

TestTV_layout = [
    [sg.Text('TV1', justification='center')],
]

# Create TestTV window
TestTV_window = sg.Window('Test Driver Program', TestTV_layout)

event, values = TestTV_window.read()

TestTV_window.close()