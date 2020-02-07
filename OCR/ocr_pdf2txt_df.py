# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:08:15 2020

@author: renatons
"""
# O codigo le um arquivo pdf e a partir dele gera uma imagem .jpg para cada pagina, um arquivo de texto .txt com todo o conteudo do pdf e um dataframe
 
#%%
import pandas as pd
from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os 
from datetime import date

#%% Declaracao dos diretorios e nome do arquivo pdf a ser convertido
nome_arq = 'Monografia_1_Colocado.pdf'
pdf_entrada = r'C:\Users\RenatoNS\Desktop\workspace\OCR\pdf_teste/'+ nome_arq
dir_saida = r'C:\Users\RenatoNS\Desktop\workspace\OCR\saida'

#%% Alteracao dos diretorios de trabalho
dir_atual = os.getcwd()
os.chdir(dir_saida)
  
#%% Conversao do pdf em imagem
paginas = convert_from_path(pdf_entrada, 500) 
  
image_counter = 1
  
for pagina in paginas: 
    filename = "pagina_"+str(image_counter)+".jpg"
    pagina.save(filename, 'JPEG') 
    image_counter = image_counter + 1
  
limite = image_counter-1
  
#%% Definicao do dataframe
df = pd.DataFrame(columns=['Nome', 'Data', 'Pagina', 'Conteudo'])

#%% Criacao do arquivo txt de saida
arq_saida = nome_arq+".txt"

arq_txt = open(arq_saida, "a")

#%% Data de conversao do arquivo
data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

#%%  Conversao das imagens em txt e preenchimento do dataframe
for i in range(1, limite + 1): 
    filename = "pagina_"+str(i)+".jpg"
    texto = str(((pytesseract.image_to_string(Image.open(filename)))))
    texto = texto.replace('-\n', '')     
    arq_txt.write(texto)
    df.loc[i-1, 'Nome'] = arq_saida
    df.loc[i-1, 'Data'] = data_em_texto
    df.loc[i-1, 'Pagina'] = i
    df.loc[i-1, 'Conteudo'] = str(texto)


arq_txt.close()

os.chdir(dir_atual)

#%% Salvar o dataframe em um csv
#df[['Nome', 'Data', 'Pagina', 'Conteudo']].to_csv(r'C:\Users\RenatoNS\Desktop\workspace\OCR\saida', sep=';', encoding="utf-8-sig")


