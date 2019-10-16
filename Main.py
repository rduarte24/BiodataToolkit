import tkinter as tk
import tkinter.messagebox
import BiodataToolkit as bdtk

root=tk.Tk()
#Here it goes the window title
root.title('BiodataToolkit')
#Here it goes the window size
width=600
height=480
#Centering the window
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x_coordinate= (screen_width/2) - (width/2)
y_coordinate= (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width,height,x_coordinate,y_coordinate))
#Fixing size
root.resizable(0,0)

#This was supposed to insert an icon in the windows title
#root.iconbitmap(r'Media/bioinformatics.png')

#logo = tk.PhotoImage(file='/Users/rduarte/Documents/Projects/GCL/Biodata Toolkit GUI/logo.ico')
#root.tk.call('wm', 'iconphoto', root._w, logo)


#Code to add widgets goes HERE !
menuBar=tk.Menu(root)
root.config(menu=menuBar)

#Functions asociated to the next menu section
def test_function():
    print('this is the test')
# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menuBar, tearoff=0)
filemenu.add_command(label="Open", command=test_function())
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=filemenu)

#Functions asociated to the next menu section
# Menu Definition
editmenu = tk.Menu(menuBar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
menuBar.add_cascade(label="Edit", menu=editmenu)

#Functions asociated to the next menu section
def about_us():
    tkinter.messagebox.showinfo('BiodataToolkit','Laboratorio de Genómica de Celomados - BivL2ab')
#Menu definition
helpmenu = tk.Menu(menuBar, tearoff=0)
helpmenu.add_command(label="About", command=about_us)
menuBar.add_cascade(label="Help", menu=helpmenu)

#Backgroud definition
photo = tk.PhotoImage(file='Media/Background_es.png')
labelphoto = tk.Label(root,image=photo)
labelphoto.pack()  




root.mainloop()