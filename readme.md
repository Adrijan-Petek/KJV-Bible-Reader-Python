[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# KJV Bible Reader GUI

**Programmed in Python | PySimpleGUI**

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/adrijano/KJV-Bible-Reader-GUI/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/adrijano/KJV-Bible-Reader-GUI/graphs/commit-activity)

# If you like it give it a star

[![GitHub stars](https://img.shields.io/github/stars/adrijano/KJV-Bible-Reader-GUI.svg?style=social&label=Star&maxAge=0)](https://github.com/adrijano/KJV-Bible-Reader-GUI)

![KJV-Bible-Reader-GUI](KJV-Bible-reader.png)

# How it works
```
The code is a Python program that allows users to search the King James Version (KJV) of the Bible. It provides a GUI where users can enter the name of the book, the chapter number, and optionally, the verse number, and the program displays the requested Bible passage.

The program reads the KJV text from a text file named 'KJV.txt' and stores it in a variable named 'bible'. The 'ver' function splits the text into verses and returns them as a list.

The program uses PySimpleGUI to create a GUI window. The 'create_main_window' function creates the main window with the necessary layout for user input and output. The 'create_settings_window' function creates a settings window where users can change the GUI theme.

The 'load_settings' and 'save_settings' functions load and save the GUI theme setting from and to a JSON settings file, respectively.

The 'main' function is the main entry point of the program. It contains a loop that continuously listens for user input events. If the user clicks the 'Exit' button or closes the window, the loop exits and the program terminates. If the user clicks the 'Search' button or presses Enter, the program attempts to retrieve the requested Bible passage and display it in the output area. If the user clicks the 'Copy' menu item, the selected text in the output area is copied to the clipboard. If the user clicks the 'About' menu item, a popup window with information about the program is displayed. If the user clicks the 'Settings' menu item, the settings window is displayed where the user can change the GUI theme.

In summary, this program is a simple GUI Bible search tool that allows users to retrieve passages from the KJV of the Bible. It uses PySimpleGUI to create a user-friendly interface and provides some basic functionality such as copying text to the clipboard and changing the GUI theme.

```
# How to use

### Python3+

```
git clone https://github.com/adrijano/KJV-Bible-Reader-GUI.git

cd KJV-Bible-Reader-GUI && pip install -r requirements.txt

python KJV-Bible-Reader-GUI.py
```
### Windows
```
cd dist 
KJV-Bible-Reader-GUI.exe
```
![Adrijan's github stats](https://github-readme-stats.vercel.app/api?username=adrijano&show_icons=true)