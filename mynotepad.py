import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)

    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scroll Bar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")

        except:
            pass

        # set widow size ( default is 300 x 300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']

        except KeyError:
            pass

        # set the window text
        self.__root.title("Untitled - Notepad")

        # centering the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left - align

        left = (screenWidth / 2) - (self.__thisWidth/2)

        # for right - align

        top = (screenHeight/2) - (self.__thisHeight/2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # to make textArea auto-resizable

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Adding controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

    # <-----------------------File Menu starts----------------------->

        # To open new file
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)

        # to open an aready existing file
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)

        # To save current File
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

        # to add separator in between commands
        self.__thisFileMenu.add_separator()

        # to  exit the application
        self.__thisFileMenu.add_command(
            label="Exit", command=self.__quitApplication)

        # now at end , cascading the file menu with its functionality in menu bar
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

    # <-----------------------File Menu Ends Here----------------------->

    # <-----------------------Edit Menu starts----------------------->

        # adding feature of CUT
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)

        # adding feature of COPY
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)

        # adding feature of paste
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)

        # to add edit menu and its functionality in menu bar
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

    # <-----------------------Edit Menu Ends Here----------------------->

    # <-----------------------Help Menu Starts Here----------------------->

        self.__thisHelpMenu.add_command(label="About", command=self.__about)

        # adding this help menu and its functionality in menu bar

        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

    # <----------------------- Help Menu Ends Here----------------------->

        # final touches:-
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # automatic adjustment of scrollbar according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    # <----------------------- commands' functionality starts her----------------------->

    # <-----------------------File Menu commands starts----------------------->

    def __newFile(self):
        self.__root.title("untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt", filetypes=[
                                      ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None

        else:
            # try to open the file
            # set the window title

            self.__root.titel(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __saveFile(self):

        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                            ("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None

            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __quitApplication(self):
        self.__root.destroy()
        # exits the application

    # <-----------------------File Menu Ends Here----------------------->

    # <----------------------- Edit Menu Sarts Here----------------------->

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    # <----------------------- Edit Menu Ends Here----------------------->

    # <----------------------- Help Menu Sarts Here----------------------->

    def __about(self):
        showinfo("Notepad", "Aditya Tiwari \n Final Year Python Project")

    # <----------------------- Help Menu Ends Here---------- ------------->

    def run(self):
        # run main application

        self.__root.mainloop()


# Run main application

notepad = Notepad(width=600, height=400)
notepad.run()
