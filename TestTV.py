# Test Driver Program


# import modules
from TV import TV
import PySimpleGUI as sg

# Create TestTV window's content
sg.theme('DarkTeal4')

TestTV_layout = [
    [sg.Text('TV1', justification='center')],
    [sg.Text('Change channel'),sg.InputText(key='channel_1', size=(2,1)), sg.Text('Adjust volume'), sg.InputText(key='vol_1', size=(2,1))],
    [sg.Text('TV2', justification='center')],
    [sg.Text('Change channel'),sg.InputText(key='channel_2', size=(2,1)), sg.Text('Adjust volume'), sg.InputText(key='vol_2', size=(2,1))],
    [sg.Text('')],  #Creates an empty row
    [sg.Button('OK')]

]

# Create TestTV window
TestTV_window = sg.Window('Test Driver Program', TestTV_layout)

event, values = TestTV_window.read()