import os
import subprocess as s
from PyPDF4 import PdfFileMerger

print('''PDF merger for Microsoft(R) Windows™
(C)Aniket Maity
All Rights Reserved

This PDF merger will merge the given pdf files

Note: Make sure to name the PDF files properly so as to merge them in the correct order.
''')
input("Press Enter to Continue")

num=0
dirc=os.getcwd()+"\\pdfmerge"      #merger folder

#check for existence and modify
while True:
    try:
        os.mkdir(dirc)
        break
    except FileExistsError:
        dirc+=str(num)
        num+=1

#open and wait for user
s.Popen('Explorer "{}"'.format(dirc))
input("\n\nPut the video files in the folder and press enter to continue")
name=input("Enter name for merged pdf: ")
if len(name)==0:
    name='merged'

list=os.listdir(dirc)
list.sort()             #sort files

merger=PdfFileMerger()

for i in list:
    try:
        merger.append("{}\\{}".format(dirc,i))
    except:
        pass

merger.write("{}\\{}.pdf".format(dirc,name))
merger.close()

print("\n\nAll files merged. You may close this application now.")
while True:
    pass
