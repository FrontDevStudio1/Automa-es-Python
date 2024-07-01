from selenium import webdriver as web
from selenium.webdriver.common.by import By
import pandas as pd

#Versão alternativa do código. 
#Aqui é usado o pandas para criar a tabela

driver = web.Chrome() # Inicia-se a instância do Chrome Webdriver 

driver.get('https://www.r10gamer.com.br/') # O site que será usado como exemplo no projeto

nomes_jogos = driver.find_elements(By.XPATH,"//h2[@class='woocommerce-loop-product__title']")
precos = driver.find_elements(By.XPATH,"//span[@class='original-price']")


jogo = []
valor = []
for jogos, preco in zip(nomes_jogos, precos):
    jogo.append(jogos.text)
    valor.append(preco.text)
    print(jogos.text, preco.text)

dici = {'Jogos': jogo, 'Preço': valor}
planilha_atualizada = pd.DataFrame(dici)
nome_arquivo = input('Deseja salvar como? [Digite a extensão .xlsx ao final]')
# planilha_atualizada.to_excel('jogos_atualizado1.xlsx', index=False)
planilha_atualizada.to_excel(nome_arquivo, index=False)
