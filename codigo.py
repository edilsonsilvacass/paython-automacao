import os
import subprocess
import pyautogui
import time
import pandas
from dotenv import load_dotenv

load_dotenv()

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# === COORDENADAS (USE auxiliar.py PARA CALIBRAR) ===
COORDS = {
    "email":    (448, 415),
    "senha":    (448, 460),   # tab apos email
    "login":    (448, 500),   # tab apos senha + enter
    "botao_cadastrar": (917, 49),
    "codigo":   (500, 200),   # primeiro campo do formulario
}
# ===================================================

print("Iniciando em 5 segundos... mova o mouse para o canto superior esquerdo para cancelar.")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

try:
    subprocess.Popen(["start", "chrome"], shell=True)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(link)
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(COORDS["email"])
    pyautogui.write(os.getenv("EMAIL", "seu_email@example.com"))
    pyautogui.press('tab')
    pyautogui.write(os.getenv("SENHA", "sua_senha"))
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)

    tabela = pandas.read_csv("produtos.csv")
    total = len(tabela)
    print(f"Iniciando cadastro de {total} produtos...")

    for indice, linha in tabela.iterrows():
        try:
            pyautogui.click(COORDS["botao_cadastrar"])
            time.sleep(0.5)
            pyautogui.click(COORDS["codigo"])

            for coluna in ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]:
                valor = str(linha[coluna]) if pandas.notna(linha[coluna]) else ""
                pyautogui.write(valor)
                pyautogui.press('tab')

            obs = str(linha["obs"]) if pandas.notna(linha["obs"]) else ""
            pyautogui.write(obs)
            pyautogui.press('tab')
            pyautogui.press('enter')

            print(f"[{indice+1}/{total}] Produto {linha['codigo']} cadastrado")
            time.sleep(0.3)
        except KeyboardInterrupt:
            print(f"\n[INTERRUPCAO] Cancelado no produto {linha['codigo']}")
            break
        except Exception as e:
            print(f"[ERRO] Falha ao cadastrar produto {linha.get('codigo', 'desconhecido')}: {e}")
            continue

    print("Cadastro concluido!")

except KeyboardInterrupt:
    print("\n[INTERRUPCAO] Script interrompido pelo usuario")
except Exception as e:
    print(f"[ERRO FATAL] {e}")