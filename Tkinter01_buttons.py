from Tkinter import *

def buttonPressed(which):
    print 'Button pressed!' + which

def main():
    app = Tk() # create main window (frame, icon, and close/min/max button)
    app.title('Hello Button') # set title of the main window

    B = Button(app, text='Button1', command = lambda: buttonPressed('1'))
    # lambda?
    
    B.pack(side=LEFT) # what's this? grid(), place()

    B2 = Button(app, text='Button2', command = lambda: buttonPressed('2'))
    B3 = Button(app, text='Button3', command = lambda: buttonPressed('3'))

    B2.pack(side=LEFT)
    B3.pack(side=LEFT)

    app.mainloop()

if __name__ == '__main__':
    main()
