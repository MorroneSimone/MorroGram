import PySimpleGUI as sg
import cv2 
import telegram
import time

layout1=[[sg.Button('Invia',key='invio'),sg.FileBrowse('Scegli Immagine',target='img',file_types=(("JPEG","*.JPG"),("PNG","*.png")),key='img')]]  
layout=[    [sg.Text('Invia il tuo messaggio:',font=('Sans-Serif',10,'bold'))],
            [sg.Multiline(default_text='Digita qui il tuo messaggio...',size=(60,5),no_scrollbar=True,)],
            [sg.Input('img',key='img', enable_events=True,visible=False)],
            [sg.Column(layout1,expand_x=True, element_justification='center')] ]
#user_id="Inserisci user id"
#token="Inserisci Token"
bot= telegram.Bot(token=token)
path='img'
window=sg.Window('TelePonti', layout)
def telegram(values):
    try:
        bot.send_message(chat_id=user_id, text=values)
        sg.popup_quick_message('Messaggio inviato...')
    except Exception as ex:
        sg.Popup('Testo mancante...',title='error')
    time.sleep(0.250)

def sendimg(path):
    try:
        bot.send_photo(photo=open(path, 'rb'),chat_id=user_id)
        sg.popup_quick_message('Immagina inviata...')
        window['img'].update("")
    except Exception as ex:
        sg.Popup('Immagine mancante...',title='error')      
    time.sleep(0.250)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    path=values['img']
    if event=='invio':
        telegram(values[0])
    if event=='img':
        sendimg(path)
window.close()