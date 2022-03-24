import pandas as pd
from flask import Flask, jsonify
import csv

app = Flask(__name__)
#tabela = pd.read_csv('teste.csv')
#print(tabela)


                        
f = open('teste.csv')
csv_f = csv.reader(f)
i=0
dict = {}
for row in csv_f:
  i=i+1
  print('I', i )
  dict[f'item{i}'] = row
  print(dict)


@app.route('/')
def homepage():
  return jsonify(dict)

app.run(host='0.0.0.0')