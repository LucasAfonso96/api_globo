# -*- coding: UTF-8 -*-
import pandas as pd
import csv
import json
import numpy as np
from flask import Flask, jsonify
import os

# Iniciando Variaveis e o app do Flask
app = Flask(__name__)
cont = 1
array1 = []
array2 = []
aux = []
cont2 = 0
dict = {}
item = []

@app.route('/')
def homepage():
    # Fazendo um loop while para abrir os arquivos txt
    while cont<10:
    
        # Abrindo arquivos txt e colocando as linhas em um array auxiliar
        with open(f'arquivo_0{cont}.txt') as read_file:
            cont = cont + 1 
            lines = read_file.readlines()
            array2.append(lines)
        
        # Manipulando e acessando corretamente os valores das linhas dos arquivos
        for j in range(len(array2)):
            array1 = array2[j]
        
        # Removendo as duas primeiras linhas com o cabeçalho e os hifens
        array1.pop(0)
        array1.pop(0)

        # Logica para remover espaços em branco(sem afetar os espaços das palavras por exempo --> "batata cozida")
        for i in array1:
            mystring = i.strip()  
            while '  ' in mystring:
                mystring = mystring.replace('  ', ',')
            while ',,' in mystring:
                mystring = mystring.replace(',,', ',')
            while ', ' in mystring:
                mystring = mystring.replace(', ', ',')
            # Dando um append em um array auxiliar com as linhas ja formatadas corretamente
            aux.append(mystring)


    # Por ultimo, gerando um dicionario para cada linha da lista gerada
    print(aux)
    for row in aux: 
        cont2=cont2+1
        item = row.split(',')
        dict[f'item{cont2}'] = item

    # Retornando um json com o dicionario gerado!
    return json.dumps(dict)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)