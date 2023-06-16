import math
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.kabum.com.br/computadores/notebooks'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', id="listingCount").get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd) / 20)

dic_produtos = {'marca': [], 'preço': [], 'link': []}

for i in range(1, ultima_pagina + 1):
    url_pag = f'https://www.kabum.com.br/computadores/notebooks?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'lxml')
    produtos = soup.find_all('div', class_=re.compile('productCard'))
#Inspecionei o nome do produto, preço e link dos produtos 
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preço = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        link = produto.find('div', class_=re.compile('productLink')).get_text().strip()

        print(marca, preço)

        dic_produtos['marca'].append(marca)
        dic_produtos['preço'].append(preço)
        dic_produtos['link'].append(link)


    #print(url_pag)

#data = pd.read_csv("preço_notebooks.csv")
df = pd.DataFrame(dic_produtos)
#nome_arquivo_excel = 'preço_notebooks_excel.xlsx'
#data.to_excel(nome_arquivo_excel, index=False)
df.to_csv("preço_notebooks.csv", index=False)

