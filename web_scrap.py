#Lucas Lima Fernandes

from builtins import print

from threading import Thread

import requests
import datetime
from bs4 import BeautifulSoup as bs
import json
from timeit import default_timer as timer

startTIME = timer()
print(f'Iniciou: {startTIME}')


def logText(texto):
    """
    Salva um arquivo de log em txt
    *texto = passar string 
    """

    file_path = f'web_scrap.txt'

    with open(file_path, 'a') as file:
        file.write(f'{texto}\n')
        file.close()


#Contar as linhas do arquivo de leitura do web crawler, útl para multi threading
lines = 0
with open('data_crawler.txt', 'r') as file:
    urls = file.readlines()
    for i in urls:
        lines +=1

print(f'linhas: {lines}')


#
# Função para passar ao Thread#
#

def func_mt(indice):

    for c in range(indice[0], indice[1]):
        try:

            page = requests.get(urls[c])

            #SoupBeautiful para trabalhar com as páginas
            soup = bs(page.content, 'html.parser')

            #Busca pela tag <script> na página
            scripts = soup.find_all('script')
            #Transformar em string
            string_js = str(scripts[0])

            #Limpar para JSON
            init = string_js.find('{')
            end = string_js.find('</script>')

            #trabalhar com json como se fosse um dicionário python
            jdata = json.loads(string_js[init:end])

            #Função para salvar no formato correto em arquivo txt
            logText(f'Nome="{jdata["name"]}" Preco={jdata["offers"]["price"]} SKU={jdata["sku"]}')

        except:
            pass

    print(f'Termino thread: {indice[0]} até {indice[1]}!')


#definições para trabalhar com multi threads

#lines = 1000 # para limitar, basta retirar o comentário
concurrent = int(lines//40)
#concurrent = 15

divisao = lines//concurrent
resto = lines%concurrent
tam = lines
dicio = {}



print(f'''
        divisão: {divisao},
        resto: {resto},
        tam: {tam},
        concurrent: {concurrent}
    ''')


"""
EXEMPLO DAS DIVISÕES DE CONCURRENTs
divisão: 11,
resto: 1,
tam: 56,
concurrent: 5

for c:
0 = 0, 12
1 = 12, 23
2 = 23, 34
3 = 34, 45
4 = 45, 56

Termino thread: 12 até 23!
Termino thread: 45 até 56!
Termino thread: 23 até 34!
Termino thread: 34 até 45!
Termino thread: 0 até 12!

"""

## Laço abaixo definirá os conjuntos de trabalho
# 0 = 0, 12
# 1 = 23, 23

if __name__ == '__main__':

    for c in range(0, concurrent):
        
        if c == 0:
            dicio[c] = [c*concurrent, divisao+1]
        elif c == concurrent-1:
            dicio[c] = [(c*divisao)+1, tam]        
        else:
            dicio[c] = [(c*divisao)+1, (c*divisao)+divisao+1]


    tarefas = []    
    for con in range(0, concurrent):
        
        tarefa = Thread(target=func_mt, args=(dicio[con],))
        tarefas.append(tarefa)
        tarefa.start()


    for tarefa in tarefas:
        tarefa.join()


endTIME = timer()

print(f'seconds: {startTIME - endTIME}')
print(f'minutes: {(startTIME - endTIME)/60}')
print(f'{datetime.datetime.now()}')



##
# Abaixo código para operação single thread
#
##


'''
for c in urls:

    try:
        page = requests.get(c)
        #SoupBeautiful para trabalhar com as páginas
        soup = bs(page.content, 'html.parser')

        #Busca pela tag <script> na página
        scripts = soup.find_all('script')
        #Transformar em string
        string_js = str(scripts[0])

        #Limpar para JSON
        init = string_js.find('{')
        end = string_js.find('</script>')

        #trabalhar com json como se fosse um dicionário python
        jdata = json.loads(string_js[init:end])

        #Função para salvar no formato correto em arquivo txt
        logText(f'Nome="{jdata["name"]}" Preco={jdata["offers"]["price"]} SKU={jdata["sku"]}')

    except:
        pass
'''
