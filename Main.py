import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import tkinter.messagebox
import BiodataToolkit as bdtk
import Sequence_decoder as seqdeco

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
def call_parser():
    if c1 == c2:
        tkinter.messagebox.showinfo('BiodataToolkit','Error en los parámetros de entrada')
        pass
    try:
        bdtk.parser(inputFile,outputFilename,c1,c2)
    except:
        tkinter.messagebox.showinfo('BiodataToolkit','Error en los parámetros de entrada')
        pass
    #Debug line
    #print('this is the test')

def defOutName():
    global outputFilename
    outputFilename = simpledialog.askstring('Digita el nombre del archivo de salida','Outputfilename')
    outputFilename = outputFilename + '.xlsx'
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
    #defOutRoute()
    defOutName()

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menuBar, tearoff=0)
filemenu.add_command(label="Abrir", command=abrirArchivo)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="Archivo", menu=filemenu)

#Aditional module for future work

#Functions asociated to the next menu section
# Menu Definition
#decodermenu = tk.Menu(menuBar, tearoff=0)
#decodermenu.add_command(label="Cargar sequencia")
#decodermenu.add_command(label="Cargar archivo de secuencias")
#editmenu.add_command(label="Paste")
#menuBar.add_cascade(label="Sequence Decoder", menu=decodermenu)

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
btn = tk.Button(root, text='RUN',height=2, width=20, command=call_parser)
btn.pack()
btn.place(x=200, y=310)

#First one to check if you need the features of the sequences file
c1 = int
check1 = tk.Checkbutton(root, text='All Features (CDS + FASTAS)', variable = c1)
check1.pack()
check1.place(x=10, y=10)

#Second if you need the Codon sequences
c2 = int
check2 = tk.Checkbutton(root, text='Basic Features and Complete Fastas', variable = c2)
check2.pack()
check2.place(x=260, y=10)


root.mainloop()
