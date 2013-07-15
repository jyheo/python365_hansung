from Tkinter import *

def main():
    app = Tk()
    C = Canvas(app, bg="blue", height=250, width=300)

    C.create_oval(10, 100, 80, 180, outline="red", 
        fill="yellow", width=2)

    coord = 10, 10, 200, 150
    C.create_arc(coord, start=0, extent=150, fill="red")

    C.create_rectangle(230, 10, 290, 60, 
            outline="#f11", fill="#1f1", width=2)

    points = [150, 100, 200, 120, 240, 180, 210, 
            200, 150, 150, 100, 200]
    C.create_polygon(points, outline='red', 
            fill='cyan', width=2)

    C.pack()
    app.mainloop()

if __name__ == '__main__':
    main()
