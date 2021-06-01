from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Funções ###################################################################################################


def WebScraping(vURL, vBrowserDriver, vElementoXpathBusca):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    #Abertura do Navegador acessando a URL passada
    driver = webdriver.Chrome(chrome_options=options, executable_path=vBrowserDriver)
    driver.get(vURL)
    
    #Aguardar 15 segundos apos chamada da URL para garantir que a página esteja devidamente carregada
    driver.implicitly_wait(20) 
   
    #Procurar o elemente atraves do xPath
    element = driver.find_element_by_xpath(vElementoXpathBusca)
    #Pegar o Conteudo HTML do Elemento
    html_content = element.get_attribute('outerHTML')
    
    driver.implicitly_wait(10)  # in seconds
    driver.quit()

    return html_content 


def ParseHTML(vConteudo, vElemento, vClasse):
    # Passagem do conteúdo para o BeautifulSoup para que seja possivel realizar a analise e limpeza 
    soup = BeautifulSoup(vConteudo, 'html.parser')

    #Pegar o conteudo da div conforme classe apontada
    return soup.find(vElemento, id=vClasse) 


def GravaRetornoArquivo(vConteudoArquivo, vNomeArqui):
    with open(vNomeArqui, 'w', encoding='utf-8') as vFile:
        vConteudo = vConteudoArquivo
        vFile.write(vConteudo)
        vFile.close()


def EnviaEmail(vMensagem, vPara, vAssunto):
    # Corpo da mensagem do email #
    vEmail = MIMEMultipart()
    
    vPassword         = "*** SENHA DO EMAIL QUE IRÁ ENVIAR ***"
    vEmail['From']    = "*** EMAIL QUE VAI ENVIAR ***"
    vSMTP             = 'smtp.gmail.com'
    vPorta            = 587   

    vEmail['To']      = vPara
    vEmail['Subject'] = vAssunto

    vEmail.attach(MIMEText(vMensagem, 'plain'))

    server = smtplib.SMTP(vSMTP, port = vPorta)
    server.starttls()
    server.login(vEmail['From'], vPassword)
    server.sendmail(vEmail['From'], vEmail['To'], vEmail.as_string())
    server.quit()



#End Funções ###########################################################################################

vURL                = "http://www.b3.com.br/pt_br/"
vBrowserDriver      = "C:/Users/Henrique/Desktop/Programming/Python/chromedriver_win32/chromedriver.exe"
vElementoXpathBusca = "//*[@id='conteudo-principal']/div[1]/div/div[1]/div"

#Chamada da função para baixar o conteudo solicitado da URL informada
vHTMLRetorno  = WebScraping(vURL, vBrowserDriver,  vElementoXpathBusca)

#Armazena o resultado em um arquivo txt
GravaRetornoArquivo(vHTMLRetorno, 'return_v2.html') 



print('------------------------------------------------------------')
print('IBOVESPA: ' + ParseHTML(vHTMLRetorno, "div", "ibovPct").string)
print('Pontos: ' + ParseHTML(vHTMLRetorno, "div", "ibovPts").string)
print('------------------------------------------------------------')

print('Taxa DI: ' + ParseHTML(vHTMLRetorno, "div", "taxaPct").string + ' - ' + ParseHTML(vHTMLRetorno, "div", "taxaData").string)
print('------------------------------------------------------------')

print('Índice DI: ' + ParseHTML(vHTMLRetorno, "div", "indicePts").string + ' - ' + ParseHTML(vHTMLRetorno, "div", "indiceData").string)
print('------------------------------------------------------------')


EnviaEmail('Teste', 'EMAIL_DESTINO@EMAIL.COM', 'Dados B3')