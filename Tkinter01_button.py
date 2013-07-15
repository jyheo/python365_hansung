from Tkinter import Tk, Button

def buttonPressed():
    print 'Button pressed!'

def main():
    app = Tk() # create main window (frame, icon, and close/min/max button)
    app.title('Hello Button') # set title of the main window

    B = Button(app, text='Button', command = buttonPressed)
    # w = Button ( master, option=value, ... )
    # master: This represents the parent window.
    
    B.pack() # what's this? grid(), place()

    app.mainloop()

if __name__ == '__main__':
    main()
