#!/usr/bin/python3
# Coded By Adrijan P.
# Sponsored By Daniel John G.

import PySimpleGUIWeb as sg


def kjv():
    with open('KJV.txt', 'r') as file:
        return file.read()

def ver(bible):
    return bible.split('\n')



def create_main_window():
    sg.theme('Black')

    layout_l =[[sg.Text('Enter the name of the book: ')],
               [sg.InputText(size=(35,1), key='-BOOK-')],
               [sg.Text('Enter the chapter number: ')],
               [sg.InputText(size=(35,1), key='-CHAPTER-')]]

    layout_r = [[sg.Text('Enter the verse number (leave empty for whole chapter): ')],
                [sg.InputText(size=(38,1), key='-VERSES-')],
                [sg.Text('')],
                [sg.Text('')]]

    layout = [[sg.Image('img/jesussaves.png', size=(720,100))],
              [sg.Output(size=(735,300), key='out')],
              [sg.Column(layout_l), sg.Column(layout_r)],
              [sg.Button('Search', size=(50,2), bind_return_key=True)]]

    return sg.Window('Jesus Saves - Bible Search',
                     layout,
                     element_justification='c').finalize()




def main():
    bible =  kjv()
    verses = ver(bible)
    window = create_main_window()
    while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            
        
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

