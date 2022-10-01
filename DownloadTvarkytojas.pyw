import os
import shutil
import time

while True:
    sourcepath='C:/Users/Lukas/Downloads/'
    sourcefiles = os.listdir(sourcepath)
    destinationpathFoto = 'C:/Users/Lukas/Downloads/Foto'
    destinationpathDoc = 'C:/Users/Lukas/Downloads/Docx'
    destinationpathPdf = 'C:/Users/Lukas/Downloads/PDF'
    destinationpathExe = 'C:/Users/Lukas/Downloads/exe'
    destinationpathRar = 'C:/Users/Lukas/Downloads/Rar'
    destinationpathTxt = 'C:/Users/Lukas/Downloads/Txt'
    destinationpathMp = 'C:/Users/Lukas/Downloads/mp3'
    destinationpathOther = 'C:/Users/Lukas/Downloads/Other'
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
        print("+++")
    time.sleep(5)
    print("---")

