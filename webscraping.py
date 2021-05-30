#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json

# Funções ###################################################################################################

def WebScraping(vURL, vBrowserDriver, vElementoXpathBusca):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    #Abertura do Navegador acessando a URL passada
    driver = webdriver.Chrome(chrome_options=options, executable_path=vBrowserDriver)
    driver.get(vURL)
    driver.implicitly_wait(10)  # in seconds
   
    #Procurar o elemente atraves do xPath
    element = driver.find_element_by_xpath(vElementoXpathBusca)
    #Pegar o Conteudo HTML do Elemento
    html_content = element.get_attribute('outerHTML')
    
    driver.implicitly_wait(10)  # in seconds
    driver.quit()

    return html_content 

def ParseHTML(vConteudo, vElemento, vClasse):
    # Passagem do contudo para o BeautifulSoup para que seja possivel realizar a analise e limpeza 
    soup = BeautifulSoup(vConteudo, 'html.parser')

    #Pegar o conteudo da div conforme classe apontada
    return soup.find(vElemento, id=vClasse) 


#End Funções ###########################################################################################

vURL                = "https://s.tradingview.com/embed-widget/market-overview/bovespa/?locale=br#%7B%22showChart%22%3Afalse%2C%22width%22%3A%22100%25%22%2C%22height%22%3A%22400%22%2C%22largeChartUrl%22%3A%22http%3A%2F%2Fwww.b3.com.br%2Fpt_br%2Fmarket-data-e-indices%2Fservicos-de-dados%2Fmarket-data%2Fcotacoes%2F%22%2C%22tabs%22%3A%5B%7B%22title%22%3A%22Maiores%20altas%22%2C%22symbols%22%3A%5B%7B%22s%22%3A%22BMFBOVESPA%3APETR3%22%2C%22d%22%3A%22PETROBRAS%20%20%20ON%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AWEGE3%22%2C%22d%22%3A%22WEG%20%20%20%20%20%20%20%20%20ON%20%20%20%20%20%20NM%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3APETR4%22%2C%22d%22%3A%22PETROBRAS%20%20%20PN%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3ALAME4%22%2C%22d%22%3A%22LOJAS%20AMERICPN%20%20%20%20%20%20N1%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AMGLU3%22%2C%22d%22%3A%22MAGAZ%20LUIZA%20ON%20%20%20%20%20%20NM%22%7D%5D%7D%2C%7B%22title%22%3A%22Maiores%20baixas%22%2C%22symbols%22%3A%5B%7B%22s%22%3A%22BMFBOVESPA%3ASBSP3%22%2C%22d%22%3A%22SABESP%20%20%20%20%20%20ON%20%20%20%20%20%20NM%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AAZUL4%22%2C%22d%22%3A%22AZUL%20%20%20%20%20%20%20%20PN%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AIRBR3%22%2C%22d%22%3A%22IRBBRASIL%20REON%20%20%20%20%20%20NM%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AGOLL4%22%2C%22d%22%3A%22GOL%20%20%20%20%20%20%20%20%20PN%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AEMBR3%22%2C%22d%22%3A%22EMBRAER%20%20%20%20%20ON%20%20%20%20%20%20NM%22%7D%5D%7D%2C%7B%22title%22%3A%22Mais%20negociadas%22%2C%22symbols%22%3A%5B%7B%22s%22%3A%22BMFBOVESPA%3APETR4%22%2C%22d%22%3A%22PETROBRAS%20%20%20PN%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AVALE3%22%2C%22d%22%3A%22VALE%20%20%20%20%20%20%20%20ON%20%20%20%20%20%20NM%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3APETR3%22%2C%22d%22%3A%22PETROBRAS%20%20%20ON%20%20%20%20%20%20N2%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3AITUB4%22%2C%22d%22%3A%22ITAUUNIBANCOPN%20%20EJ%20%20N1%22%7D%2C%7B%22s%22%3A%22BMFBOVESPA%3ABBDC4%22%2C%22d%22%3A%22BRADESCO%20%20%20%20PN%20%20%20%20%20%20N1%22%7D%5D%7D%5D%2C%22utm_source%22%3A%22www.b3.com.br%22%2C%22utm_medium%22%3A%22widget%22%2C%22utm_campaign%22%3A%22market-overview%22%7D"
vBrowserDriver      = "C:/Users/Henrique/Desktop/Programming/Python/chromedriver_win32/chromedriver.exe"
vElementoXpathBusca = "//*[@id='widget-market-overview-container']/div[2]/div/div[1]/div/div"

#Chamada da função para baixar o conteudo solicitado da URL informada
vHTMLRetorno  = WebScraping(vURL, vBrowserDriver,  vElementoXpathBusca)


#Armazena o resulto em um arquivo txt
with open('return_v3.html', 'w', encoding='utf-8') as vFile:
    vConteudo = vHTMLRetorno
    vFile.write(vConteudo)
    vFile.close()



soup = BeautifulSoup(vConteudo, 'html.parser')

    #Pegar o conteudo da div conforme classe apontada
soup.find('div', class_='tv-site-table__column tv-widget-watch-list__main-column') 

vItens = soup.find_all('a')



for cursor_data in vItens:
    vTexto = cursor_data.get('data-symbol')
    print(vTexto.replace("BMFBOVESPA:", "") )
'''
print('------------------------------------------------------------')
print('IBOVESPA: ' + ParseHTML(vHTMLRetorno, "div", "ibovPct").string)
print('Pontos: ' + ParseHTML(vHTMLRetorno, "div", "ibovPts").string)
print('------------------------------------------------------------')

print('Taxa DI: ' + ParseHTML(vHTMLRetorno, "div", "taxaPct").string + ' - ' + ParseHTML(vHTMLRetorno, "div", "taxaData").string)
print('------------------------------------------------------------')

print('Índice DI: ' + ParseHTML(vHTMLRetorno, "div", "indicePts").string + ' - ' + ParseHTML(vHTMLRetorno, "div", "indiceData").string)
print('------------------------------------------------------------')
'''
#vTrataParse = ParseHTML(vHTMLRetorno, "div", "large-3 medium-3 columns").string
#print('Pontos: ' + vTrataParse)
