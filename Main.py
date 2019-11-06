import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import tkinter.messagebox
import BiodataToolkit as bdtk

inputFile = ''
outputFilename = ''
outputRoute = ''


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

def defOutName():
    global outputFilename
    outputFilename=simpledialog.askstring('Digita el nombre del archivo de salida','Outputfilename')
    print(outputFilename)

def defOutRoute():
    global outputRoute
    outputRoute=filedialog.askdirectory(title='Selecciona la carpeta de Salida')
    print(outputRoute)
    defOutName()

def abrirArchivo():
    global inputFile
    inputFile = filedialog.askopenfilename(title='Selecciona el archivo de entrada.',filetypes=[('GenBank file','*.gb')])
    print(inputFile)
    defOutRoute()

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menuBar, tearoff=0)
filemenu.add_command(label="Abrir", command=abrirArchivo)
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

#Run Button def
btn = tk.Button(root, text='RUN',height=2, width=20, command=test_function)
btn.pack()
btn.place(x=200, y=310)



root.mainloop()