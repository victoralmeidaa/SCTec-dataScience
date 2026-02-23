from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.ogol.com.br/equipe/paysandu/8920'
html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

linhas = bs.find_all('div',{'class': 'staff'})


# for linha in linhas:
#     print(linha.text)

numero, nome, idade = [], [], []

for linha in linhas:
    children = linha.find_all('div')
    numero.append(children[0].text.strip()) # buscando numero na DIV[0]
    nome.append(children[3].text.strip())   # buscando nome na DIV[3]
    text_idade = children[2].text.strip()   # buscando idade na DIV[2] // DIV[2] esta retornando nome+idade

    idade_extraida = re.search(r'\d+', text_idade)  # extraindo apenas valor numerico da DIV[2] "REGEX"
    idade.append(idade_extraida.group() if idade_extraida else nome)    # add apenas se a linha a cima retornar um valor numerico

df = pd.DataFrame({'numero':numero, 'nome':nome, 'idade':idade})

print(df.head(32))
# buscando no site Ogol // Informacoes jogadores Paysandu 2026
