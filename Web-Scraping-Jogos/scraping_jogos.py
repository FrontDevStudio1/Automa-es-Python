from selenium import webdriver as web
from selenium.webdriver.common.by import By
import openpyxl as excel

#Projeto de automação
#com este código, entra-se no site do exemplo 
# É feita uma varredura do nome de todos os itens(jogos), e seus respectivos preços
#Após esse processo, todos os dados são organizados em uma tabela do excel

driver = web.Chrome() # Inicia-se a instância do Chrome Webdriver 

driver.get('https://www.r10gamer.com.br/')

nomes_jogos = driver.find_elements(By.XPATH,"//h2[@class='woocommerce-loop-product__title']")
precos = driver.find_elements(By.XPATH,"//span[@class='original-price']")


planilha = excel.Workbook()
planilha.create_sheet('Jogos')
planilha_jogos = planilha['Jogos']
planilha_jogos['A1'].value = 'Jogo'
planilha_jogos['B1'].value = 'Preço'

for jogos, preco in zip(nomes_jogos, precos):
    planilha_jogos.append([jogos.text,preco.text])
    print(jogos.text, preco.text)
planilha.save('jogos.xlsx')
