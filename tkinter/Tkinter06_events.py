from Tkinter import *

def main():
    app = Tk()


    def key(event):
        print "pressed", repr(event.char)

    def callback(event):
        frame.focus_set()
        print "clicked at", event.x, event.y

    def enter_callback(event):
        print "dragged at", event.x, event.y

    frame = Frame(app, width=200, height=200)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.bind("<B1-Motion>", enter_callback)
    frame.pack(fill=BOTH, expand=1)

    app.mainloop()

if __name__ == '__main__':
    main()
