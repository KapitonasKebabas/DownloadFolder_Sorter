import os
import shutil
import time
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Trojan")

def start():
    sourcepath= filepath
    sourcefiles = os.listdir(sourcepath)
    destinationpathFoto = filepath + '/Foto'
    destinationpathDoc = filepath + '/Docx'
    destinationpathPdf = filepath + '/PDF'
    destinationpathExe = filepath + '/exe'
    destinationpathRar = filepath + '/Rar'
    destinationpathTxt = filepath + '/Txt'
    destinationpathMp = filepath + '/mp3'
    destinationpathOther = filepath + '/Other'
    for file in sourcefiles:
        a=0
        if file.endswith('.png') or file.endswith('.jpg'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathFoto,file))
            a=1
        if file.endswith('.docx'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathDoc,file))
            a=1
        if file.endswith('.pdf'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathPdf,file))
            a=1
        if file.endswith('.exe'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathExe,file))
            a=1
        if file.endswith('.rar'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathRar,file))
            a=1
        if file.endswith('.txt'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathTxt,file))
            a=1
        if file.endswith('.mp3'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathMp,file))
            a=1
        if file != "Foto" and file != "Docx" and file != "PDF" and file != "exe" and file != "Rar" and file != "Txt" and file != "mp3" and file != "Other" and a == 0:
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpathOther,file))
    time.sleep(5)

def selectFileDef():
    global filepath
    filepath = filedialog.askdirectory(initialdir=os.getcwd(), title="Select a folder")
    userButton['state'] = ACTIVE
    print(str(filepath))
    return str(filepath)

fileButton = Button(root, text="Select a File", command=selectFileDef)
fileButton.grid(row=3,column=0)

userButton = Button(root, text="Submit", command=start, state=DISABLED)
userButton.grid(row=7,column=0)

root.mainloop()