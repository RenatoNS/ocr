# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:10:06 2020

@author: renatons
"""
#%%
import pandas as pd
from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os 
from datetime import date

#%%
pdf_entrada = r'C:\Users\RenatoNS\Desktop\workspace\OCR\pdf_teste\pdf_30pgs.pdf'
dir_saida = r'C:\Users\RenatoNS\Desktop\workspace\OCR\saida'

#%%
dir_atual = os.getcwd()
os.chdir(dir_saida)
  
#%%  
paginas = convert_from_path(pdf_entrada, 500) 
  
image_counter = 1
  
for pagina in paginas: 
    filename = "pagina_"+str(image_counter)+".jpg"
    pagina.save(filename, 'JPEG') 
    image_counter = image_counter + 1
  
limite = image_counter-1
  
#%%
arq_saida = "saida_texto.txt"

arq_txt = open(arq_saida, "a")

#%%  
for i in range(1, limite + 1): 
    filename = "pagina_"+str(i)+".jpg"

    texto = str(((pytesseract.image_to_string(Image.open(filename))))) 

    texto = texto.replace('-\n', '')     
  
    arq_txt.write(texto) 
  
arq_txt.close()

