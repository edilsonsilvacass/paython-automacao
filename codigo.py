import os
import pyautogui
import time
import pandas
from dotenv import load_dotenv

load_dotenv()

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

# Passo 2: Login
pyautogui.click(x=448, y=415)
pyautogui.write(os.getenv("EMAIL", "seu_email@example.com"))
pyautogui.press('tab')
pyautogui.write(os.getenv("SENHA", "sua_senha"))
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# Passo 3: Carregar base de dados
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar produtos via loop
for linha in tabela.index:
    produto = tabela.loc[linha]

    pyautogui.click(x=917, y=49)
    pyautogui.write(str(produto["codigo"]))
    pyautogui.press('tab')
    pyautogui.write(str(produto["marca"]))
    pyautogui.press('tab')
    pyautogui.write(str(produto["tipo"]))
    pyautogui.press('tab')
    pyautogui.write(str(produto["categoria"]))
    pyautogui.press('tab')
    pyautogui.write(str(produto["preco_unitario"]))
    pyautogui.press('tab')
    pyautogui.write(str(produto["custo"]))
    pyautogui.press('tab')
    obs = str(produto["obs"]) if pandas.notna(produto["obs"]) else ""
    pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.3)
