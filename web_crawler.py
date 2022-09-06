#Lucas Lima Fernandes

import scrapy
import datetime
from bs4 import BeautifulSoup as bs
import requests


def logText(texto):
    """
    Salva um arquivo de log em txt
    *texto = passar string 
    """

    file_path = f'data_crawler.txt'
    
    with open(file_path, 'a') as file:
        file.write(f'{texto}\n')
        file.close()


url = 'https://www.drogaraia.com.br/'
page = requests.get(url)
#SoupBeautiful para trabalhar com as páginas
soup = bs(page.content, 'html.parser')

#Busca pelos sub menus na página
a = 'enustyles__StyleSubLink'
scripts = soup.find_all('a',{'class':'EIkoI'})


#salva as urls dos sub menus
urls_list = []

for c in scripts:
    string = str(c)
    #print(string)
    init = string.find('href="')
    end = string.find('">')
    print(f'{url}{string[init+7:end]}')
    urls_list.append(f'{url}{string[init+7:end]}')




## SCRAPY
class DG_Spider(scrapy.Spider):
    name = 'drogaRaia'
    allowed_domains = ['drogaraia.com.br']
    start_urls = urls_list
    #start_urls = ['https://www.drogaraia.com.br/']

    def parse(self, response):
        #Seletor pela class LinkNext
        SET_SELECTOR = '.LinkNext'

        #contador, pois estava duplicando as urls
        c = 0
        for i in response.css(SET_SELECTOR): 

            text = i.css('a::attr(href)').get()

            if text[0:29] == 'https://www.drogaraia.com.br/' and c%2 == 0:
                
                logText(i.css('a::attr(href)').get())
            else:
                pass
            c+=1

