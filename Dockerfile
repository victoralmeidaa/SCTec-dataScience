# Usar uma imagem
FROM python:3.12.4-slim

# Definiro diretorio a ser trabalhado dentro docker
WORKDIR /app

# Copiar o requirements para dentro do app
COPY requirements.txt /app/

# Instalação das dependencias
RUN pip install -r requirements.txt

# Copiar o codigo para aplicação
COPY . /app/

# Comando para rodar
CMD [ "python", "modulo05/main.py" ]


