import time
import pyautogui

print("=== CALIBRAGEM DE COORDENADAS ===")
print("Abra a pagina de login no Chrome e posicione o mouse")
print("sobre cada elemento quando solicitado (5s para posicionar).")
print()

input("Pressione Enter quando estiver na pagina de login...")

print("1. Posicione o mouse sobre o campo EMAIL...")
time.sleep(5)
email_x, email_y = pyautogui.position()
print(f"   EMAIL: x={email_x}, y={email_y}")

print("2. Posicione o mouse sobre o campo SENHA...")
time.sleep(5)
senha_x, senha_y = pyautogui.position()
print(f"   SENHA: x={senha_x}, y={senha_y}")

print("3. Posicione o mouse sobre o botao ENVIAR/LOGIN...")
time.sleep(5)
login_x, login_y = pyautogui.position()
print(f"   LOGIN: x={login_x}, y={login_y}")

input("Pressione Enter apos fazer login e abrir o formulario de cadastro...")

print("4. Posicione o mouse sobre o campo CODIGO DO PRODUTO...")
time.sleep(5)
cod_x, cod_y = pyautogui.position()
print(f"   CODIGO: x={cod_x}, y={cod_y}")

print("5. Posicione o mouse sobre a MARCA...")
time.sleep(5)
marca_x, marca_y = pyautogui.position()
print(f"   MARCA: x={marca_x}, y={marca_y}")

print("6. Posicione o mouse sobre OBS...")
time.sleep(5)
obs_x, obs_y = pyautogui.position()
print(f"   OBS: x={obs_x}, y={obs_y}")

print()
print("=== COORDENADAS PARA COPIAR PARA O codigo.py ===")
print(f"email   = ({email_x}, {email_y})")
print(f"senha   = ({senha_x}, {senha_y})")
print(f"login   = ({login_x}, {login_y})")
print(f"codigo  = ({cod_x}, {cod_y})")
print(f"marca   = ({marca_x}, {marca_y})")
print(f"obs     = ({obs_x}, {obs_y})")
