from Tkinter import *

def main():
    m1 = PanedWindow(bd=1, bg='white')
    m1.pack(fill=BOTH, expand=1)

    left = Label(m1, text="left pane")
    m1.add(left)

    m2 = PanedWindow(m1, orient=VERTICAL, bd=1, bg='white')
    m1.add(m2)

    top = Label(m2, text="top pane")
    m2.add(top)

    bottom = Label(m2, text="bottom pane")
    m2.add(bottom)

    mainloop()

if __name__ == '__main__':
    main()
