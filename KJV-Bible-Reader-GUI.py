#!/usr/bin/python3
# Coded By Adrijan P.
# Sponsored By Daniel John G.

import json
from json import (load as jsonload, dump as jsondump)
from os import path
import PySimpleGUI as sg
import pyperclip

def kjv():
    with open('KJV.txt', 'r') as file:
        return file.read()

def ver(bible):
    return bible.split('\n')


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])
    menu_def = [['&Menu', ['&Copy', 'Settings', 'E&xit']],
                ['&Help', '&About...']]

    right_click_menu = ['Unused', ['&Copy','Settings', 'E&xit']]

    layout_l =[[sg.Text('Enter the name of the book: ')],
               [sg.InputText(size=50, key='-BOOK-')],
               [sg.Text('Enter the chapter number: ')],
               [sg.InputText(size=50, key='-CHAPTER-')]]

    layout_r = [[sg.Text('Enter the verse number (leave empty for whole chapter): ')],
                [sg.InputText(size=50, key='-VERSES-')],
                [sg.Text('')],
                [sg.Text('')]]

    layout = [[sg.Image('img/jesussaves.png', size=(720,100))],
              [sg.Output(size=(100, 20), key='out')],
              [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)],
              [sg.Button('Search', bind_return_key=True), sg.Button('Exit')],
              [sg.Menu(menu_def)]]

    return sg.Window('Jesus Saves - Bible Search',
                     layout,
                     right_click_menu=right_click_menu,
                     location=(290,50)).finalize()




def main():
    bible =  kjv()
    verses = ver(bible)
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    while True:
        if window is None:
            window = create_main_window(settings)
            
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Copy':
            selected_text = window['out'].get()
            window['out'].update('')
            pyperclip.copy(selected_text)
            print('Copied:')
            
            

            
        elif event == 'About...':
            sg.popup('About:', 'Jesus Saves', 'Version 1.1',)
        
        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
        try:
            book = values['-BOOK-'].title()
            window['out'].update('')
            if not book:
                print("Please enter a book: "+'\n')
                continue
            if book not in bible:  # check if book is in the Bible text
                print(f"{book} not found. Please check the spelling and try again."+'\n')
                continue  # ask user to try again if book is not found

            chapter = values['-CHAPTER-']
            if not chapter:
                print("Please enter a chapter number: "+'\n')
                continue
            num_chapters = len({v.split(':')[0] for v in verses if book in v})
            if int(chapter) > num_chapters:
                print(f"Invalid chapter number. {book} has {num_chapters} chapters. Please enter a number between 1 and {num_chapters}."+'\n')
                continue  # ask user to try again if chapter number is invalid

            verse = values['-VERSES-']
            if verse:
                chapter_verses = [v for v in verses if book + ' ' + chapter + ':' in v]
                num_verses = len(chapter_verses)
                if int(verse) > num_verses:
                    print(f"{book} {chapter}:{verse} not found. This chapter only has {num_verses} verses."+'\n')
                    continue

            if not verse:
                for v in verses:
                    if book + ' ' + chapter + ':' in v:
                        print(v+'\n')

            else:
                for v in verses:
                    if book + ' ' + chapter + ':' + verse in v:
                        print(v+'\n')
                        break

        except Exception as e:
            sg.popup_error(str(e))


    window.Close()
    
if __name__ == "__main__":
    main()
