from Tkinter import *

def buttonPressed(which):
    print 'Button pressed!' + which

def main():
    app = Tk() # create main window (frame, icon, and close/min/max button)
    app.title('Hello Button') # set title of the main window

    frameTop = Frame(app)
    frameTop.pack(side = TOP, fill=BOTH) # What is fill?  X, Y, and BOTH

    frameBottom = Frame(app)
    frameBottom.pack(side = BOTTOM)

    Buttons = [Button(frameTop, text='Button1', command = lambda: buttonPressed('1')),
        Button(frameTop, text='Button2', command = lambda: buttonPressed('2')),
        Button(frameTop, text='Button3', command = lambda: buttonPressed('3')),
        Button(frameBottom, text='Button4', command = lambda: buttonPressed('4')),
        Button(frameBottom, text='Button5', command = lambda: buttonPressed('5')),
        Button(frameBottom, text='Button6', command = lambda: buttonPressed('6'))]

    for button in Buttons:
        if int(button['text'][-1]) < 4:
            button.pack(fill=BOTH) # fill?
        else:
            button.pack(side=LEFT)

    app.mainloop()

if __name__ == '__main__':
    main()
