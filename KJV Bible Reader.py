#!/usr/bin/python3
# Coded By Adrijan P.
# Sponsored By Daniel John G.

print('Jesus Christ Saves'+'\n')

def kjv():
    with open('KJV.txt', 'r') as file:
        return file.read()

def ver(bible):
    return bible.split('\n')

def main():
    bible = kjv()
    verses = ver(bible)
    while True:
        book = input('Enter the name of the book: ').title()
        if not book:
            print("Please enter a book: "+'\n')
            continue
        if book not in bible:  # check if book is in the Bible text
            print(f"{book} not found. Please check the spelling and try again."+'\n')
            continue  # ask user to try again if book is not found

        chapter = input('Enter the chapter number: ')
        if not chapter:
            print("Please enter a chapter number: "+'\n')
            continue
        num_chapters = len({v.split(':')[0] for v in verses if book in v})
        if int(chapter) > num_chapters:
            print(f"Invalid chapter number. {book} has {num_chapters} chapters. Please enter a number between 1 and {num_chapters}."+'\n')
            continue  # ask user to try again if chapter number is invalid

        verse = input('Enter the verse number (press enter to print the whole chapter): ')
        if verse:
            chapter_verses = [v for v in verses if book + ' ' + chapter + ':' in v]
            num_verses = len(chapter_verses)
            if int(verse) > num_verses:
                print(f"{book} {chapter}:{verse} not found. This chapter only has {num_verses} verses."+'\n')
                continue

        if not verse:
            for v in verses:
                if book + ' ' + chapter + ':' in v:
                    print('\n'+v+'\n')
        else:
            for v in verses:
                if book + ' ' + chapter + ':' + verse in v:
                    print('\n'+v+'\n')
                    break



main()
