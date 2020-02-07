# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:10:06 2020

@author: renatons
"""

from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
  
PDF_file = r'C:\Users\RenatoNS\Desktop\teste_ocr\teste_pdf.pdf'
  
  
# Armazena as paginas do pdf na variavel pages
pages = convert_from_path(PDF_file, 500) 
  
# Contador para cada página armazenada 
image_counter = 1
  
# Iterate through all the pages stored above 
for page in pages: 
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1
  

# Variavel que armazena o total do número de páginas 
filelimit = image_counter-1
  
# Cria o arquivo texto para escrever a saída do código 
outfile = "saida_texto.txt"
  
f = open(outfile, "a") 
  
# Iterar de 1 até o total do número de páginas
for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"

    text = str(((pytesseract.image_to_string(Image.open(filename))))) 

    text = text.replace('-\n', '')     
  
    f.write(text) 
  
f.close() 
