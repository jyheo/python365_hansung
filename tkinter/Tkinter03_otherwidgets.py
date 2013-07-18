from Tkinter import *



def main():
    app = Tk() # create main window (frame, icon, and close/min/max button)
    app.title('Hello Button') # set title of the main window

    def buttonPressed(which):
        if which == '2':
            print 'Checkbutton pressed: ' + str(var.get())
        elif which == '1':
            print 'Input: ' + textvar.get()
        elif which == 'list':
            print 'List selected ', listbox.curselection()
        else:
            print 'Button pressed!' + which

    # label, entry, checkbutton, 
    var = IntVar()
    textvar = StringVar()
    widgets = [
        Label(app, text="Input Anything:"),
        Entry(app, textvariable=textvar),
        Button(app, text='Button1', command = lambda: buttonPressed('1')),
        Checkbutton(app, text='Checkbutton2', variable=var, command = lambda: buttonPressed('2'))]

    for wdg in widgets:
        wdg.pack()

    textvar.set("Type Here!")

    # list box creation
    listbox = Listbox(app)
    for item in ['Python', 'Tkinter', 'wxPython', 'twisted', 'Web2Py']:
        listbox.insert(END, item)
    listbox.pack()

    Button(app, text="List Select", command = lambda: buttonPressed('list')).pack()

    # image label
    photo = PhotoImage(file='python.gif')
    Label(image=photo).pack()

    app.mainloop()

if __name__ == '__main__':
    main()
