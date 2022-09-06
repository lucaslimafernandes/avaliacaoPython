# Avaliação Python - WebGlobal

Lucas Lima Fernandes

## Instalação

1.  Criar um ambiente virtual (venv)
>python3 -m venv ambiente

2.  Ativar o venv
>source ambiente/bin/activate   #Linux

> source ambiente/Scripts/activate  #Windows

3.  Instalar os pacotes
>python -m pip install --upgrade pip

>pip install -r requirements.txt


## Web Crawler - Spider
Rodar o web crawler
> scrapy runspider web_crawler.py

Retornou 6.733 linhas com urls
Ex.:
https://www.drogaraia.com.br/levotiroxina-sodica-50mcg-merck-do-brasil-genericos-30-comprimidos.html
https://www.drogaraia.com.br/puran-t4-50-mcg-uso-oral-30-comprimidos.html


## Web Scrap
> python web_scrap.py

Retornou as 6.733 linhas 1.767 linhas em 156 seg (2,5 min)
Obs.: 403 Error, Requests blocked

Ex.:
Nome="Água Adicionada de Sais Smartwater com 591ml" Preco=6.45 SKU=53316
Nome="Condicionador Huggies Chá de Camomila com 200ml" Preco=17.99 SKU=52276