from Tkinter import *
import tkMessageBox

def donothing():
   filewin = Toplevel(app)
   button = Button(filewin, text="Do nothing button", command=lambda: filewin.destroy())
   button.pack()

def messagebox():
   tkMessageBox.showinfo("Say Hello", "Hello World")

def askbox():
   print tkMessageBox.askyesno("Question", "Are you a boy?")

app = Tk()

def main():
   menubar = Menu(app)
   filemenu = Menu(menubar, tearoff=1)
   filemenu.add_command(label="showinfo", command=messagebox)
   filemenu.add_command(label="askbox", command=askbox)
   filemenu.add_separator()
   filemenu.add_command(label="Exit", command=app.destroy)
   menubar.add_cascade(label="File", menu=filemenu)

   
   editmenu = Menu(menubar, tearoff=0)
   editmenu.add_command(label="Undo", command=donothing)
   editmenu.add_separator()
   editmenu.add_command(label="Cut", command=donothing)
   editmenu.add_command(label="Copy", command=donothing)
   editmenu.add_command(label="Paste", command=donothing)
   editmenu.add_command(label="Delete", command=donothing)
   editmenu.add_command(label="Select All", command=donothing)
   menubar.add_cascade(label="Edit", menu=editmenu)
   

   app.config(menu=menubar)
   app.mainloop()

if __name__ == '__main__':
   main()
