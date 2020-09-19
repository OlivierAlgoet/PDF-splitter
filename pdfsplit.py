# -*- coding: utf-8 -*-
"""
@author: olalgoet
@summary: Simple pdf splitter
give a command string such as 5x1+3x2+9x1, this will split the pdf in 5 times 1 page, 3 times 2 and 9 times 1
"""

""" online pdf extraction """
import os
from tkinter import filedialog
import tkinter
from PyPDF2 import PdfFileReader,PdfFileWriter
from logger import logger
MAXDIGITS=3
### Initialize number
log=logger()
last_iteration="saved_number"
last_number=log.unpickle(last_iteration)
if not last_number:
    last_number=1

#initialize save directory
new_dir="split_pdf"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
prefix=""
## ask for prefix
while(not prefix):
    choice=input("Sales or purchases Enter < S,P >")
    if choice.lower()=='s':
        prefix="S"
    elif(choice.lower()=="p"):
        prefix="P"
        
## Get start number
number=input("The following pdf will start on number {} , or you can define your own start number".format(last_number))
try:
    last_number=int(number)
except:
    pass

#Get pdf to split
print("Select the pdf you wish to split")
base_path="" #aanpassen!!
while(not base_path):
    root=tkinter.Tk()
    ##zie in windows
    base_path=filedialog.askopenfilename(title = "select pdf",defaultextension=".pdf",filetypes = [("pdf file","*.pdf")])
    root.destroy()

#Get split string
print("Give a command to split te pdfs")
print("Example: splitting a pdf of 20 pages in 5 times 1 sheet") 
print("followed by 3 times 2 sheets and thereafter 9 times 1 is done as following:")
print("command: 5x1+3x2+9x1")
print("Don't forget the + otherwise the example will see 5x13")
split_serie=input("Give the command to split: ")
out=split_serie.split("+")
all_items=[]
for item in out:
    all_items.append(item.split("x"))
pdf_file=open(base_path,"rb")
pdf_reader=PdfFileReader(pdf_file)
start_page=0
for item in all_items:
    item[0]=int(item[0])
    item[1]=int(item[1])
    for i in range(item[0]):
        pdf_writer=PdfFileWriter()
        for j in range(item[1]):
            pdf_writer.addPage(pdf_reader.getPage(start_page))
            start_page+=1
        
        last_number_str=str(last_number)
        length=len(last_number_str)
        appendix=prefix+"0"*(MAXDIGITS-length)+str(last_number)
        final_path=os.path.join(new_dir,appendix +".pdf")
        last_number+=1
        split_file=open(final_path,"wb")
        pdf_writer.write(split_file)
        split_file.close()
log.pickle(last_number,"saved_number") 
   
print("*******closing down program*******")  
    
    
#TODO: page count safety!


    

        

    

    
            
            




