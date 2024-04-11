import PySimpleGUI as sg
from requests_func import request
from pdfhandler import load_pdf

def create_gui():
    # Define the layout
    layout = [
        [sg.Text('Request for Proposals'), sg.InputText(key='rfp'), sg.FileBrowse()],
        [sg.Text('Proposal'), sg.InputText(key='proposal'), sg.FileBrowse()],
        [sg.Text('System'), sg.InputText(key='system')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Urban Planner', layout)

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            # Load PDF for city plan and proposal
            plan_page_count, request_text = load_pdf(values['rfp'])
            proposal_page_count, proposal_text = load_pdf(values['proposal'])

            # Make a request to the OpenAI API
            response = request('gpt-3.5-turbo',
                               values['system'],
                               request_text,
                               proposal_text)

            # Show the response in a popup
            sg.popup(response)

    window.close()