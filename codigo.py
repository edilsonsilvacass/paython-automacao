

import pyautogui
import time

# pyautogui.click - clica
# pyautogui.write - escreve
# pyautogui.press - aperta uma tecla
# pyautogui.hotkey - aperta uma combinação de teclas

pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundos entre as ações
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1: Entra no sistema da empresa
# Abrir o navegador
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
# fazer uma pausar maior para esperar o navegador abrir
time.sleep(3)  # Pausa de 3segundos para esperar o navegador abrir

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=448, y=415)  # Substitua
pyautogui.write("seu_email@example.com")
pyautogui.press('tab')  # Mover para o campo de senha
pyautogui.write("sua_senha")
pyautogui.press('tab') # Mover para o botão de login
pyautogui.press('enter')  # Pressionar Enter para fazer login# fazer uma pausar maior para esperar o navegador abrir
time.sleep(3)  # Pausa de 3segundos para esperar o navegador abrir


 


# pip install pyautogui
# Passo 3: Abrir a base de dados
# pip install pandas openpyxl
import pandas 

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
# Passo 4: Cadastrar 1 produto
# codigo
pyautogui.click(x=917, y=49)  # Substitua com as coordenadas do botão "Cadastrar Produto"
pyautogui.write("MOLO000251")
pyautogui.press('tab')
#marca
pyautogui.write("Logitech")
pyautogui.press('tab')
#tipo
pyautogui.write("Mouse")
pyautogui.press('tab')
#categoria
pyautogui.write("1")
pyautogui.press('tab')
#preco_unitario
pyautogui.write("25.95")
pyautogui.press('tab')
#custo
pyautogui.write("6.5")
pyautogui.press('tab')
#obs
pyautogui.write("NaN")
pyautogui.press('tab')

pyautogui.press('enter')  # Pressionar Enter para cadastrar o produto

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos
   
