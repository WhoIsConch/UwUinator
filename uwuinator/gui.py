# from .uwuinator import UwUinator
import PySimpleGUI as sg
import os

sg.theme('DarkBlue')

layout = [
    [
        sg.Text("Directory to Fill"),
        sg.FolderBrowse(key="path")
    ],
    [
        sg.Text("File to Copy"),
        sg.FileBrowse(key="file")
    ],
    [
        sg.Text("Amount of storage to UwUinate (in mb)"),
        sg.InputText(key='amount')
    ],
    [
        sg.Column(
            justification='center',
            layout=[[
                sg.Button('UwUinate!', key='start')
            ]],
        )
    ]
]

window = sg.Window('UwUinator', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'start':
        trigger = True
        if values["amount"]:
            try:
                values["amount"] = int(values["amount"])
            except ValueError:
                sg.Popup("Amount of storage must be empty or an integer!")
                trigger = False
        
        if trigger:
            window['start'].update(disabled=True)
            window['amount'].update(disabled=True)
            window['file'].update(disabled=True)
            window['path'].update(disabled=True)

window.close()