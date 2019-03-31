# pylint: disable=W0614
from tkinter import *
import fileinput
from plyer import notification
import datetime

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()

    def init_window(self):
        global noteToAdd, deleteNum, dateToAdd, timeToAdd
        self.master.title("GUI")

        self.grid(row=0, column=0)

        f1 = Frame(width=300, height=300)

        f1.grid(row=0, column=0, sticky=N)

        addNoteButton = Button(f1, text="Add note", command=lambda: self.add_note())

        addNoteButton.grid(row=0, column=0)

        addNoteText = Label(f1, text="Note")

        addNoteText.grid(row=0, column=1)

        viewNotes = Button(f1, text="View Notes", command=self.view_notes)
        
        viewNotes.grid(row=1, column=0)
        
        deleteNote = Button(f1, text="Delete note", command=lambda: self.delete_note())

        deleteNote.grid(row=2, column=0)
        
        quitButton = Button(f1, text="Quit", command=self.client_exit)
        
        quitButton.grid(row=3, column=0)
        
        noteToAdd = StringVar()

        add = Entry(f1, textvariable=noteToAdd)

        add.grid(row=0, column=2)

        addNoteDate = Label(f1, text="Date")

        addNoteDate.grid(row=0, column=3)

        dateToAdd = StringVar()

        date = Entry(f1, textvariable=dateToAdd)

        date.grid(row=0, column=4)

        addNoteTime = Label(f1, text="Time")

        addNoteTime.grid(row=0, column=5)

        timeToAdd = StringVar()

        time = Entry(f1, textvariable=timeToAdd)

        time.grid(row=0, column=6)

        deleteNum = StringVar()

        delete = Entry(f1, textvariable=deleteNum)

        delete.grid(row=2, column=2)

    def client_exit(self):
        exit()

    def add_note(self):
        string = noteToAdd.get()
        time = timeToAdd.get()
        date = dateToAdd.get()
        f = open("notes.txt", "a+")
        f.write(string)
        f.write(", ")
        f.write(date)
        f.write(", ")
        f.write(time)
        f.write("\n")
        f.close()
        notification.notify(
            title='Here is the title',
            message='Here is the message',
            app_name='Here is the application name',
        )

    def view_notes(self):
        f = open("notes.txt", "r")
        if f.mode == 'r':
            contents = f.read()
            f2 = Frame(root, width=300, height=300)
            f2.grid(row=0, column=1)
            w = Text(f2)
            w.grid(row=10)
            w.insert(END,contents)

    def delete_note(self):
        f = open("notes.txt", "r")
        integer = deleteNum.get()
        deleteNote = int(integer) - 1
        data = list(f)
        data[deleteNote] = ""
        open('notes.txt', 'w').close()
        f = open("notes.txt", "w")
        for i in data :
            f.write(i)
    
    

root = Tk()
root.geometry("1920x1080")
app = Window(root)
root.mainloop()