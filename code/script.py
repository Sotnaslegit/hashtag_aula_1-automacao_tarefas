# importação
import pyautogui
import pandas
import time

# confiugurações iniciais
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
user = "admin"
password = "admin"

table = pandas.read_csv("produtos.csv")
print(table)

# abrir navegador e acessar o site
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# login
pyautogui.click(848, 362)
pyautogui.write(user)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("enter")
time.sleep(3)

# cadastrar
for line in table.index:
    codigo = str(table.loc[line, "codigo"])
    marca = str(table.loc[line, "marca"])
    tipo = str(table.loc[line, "tipo"])
    categoria = str(table.loc[line, "categoria"])
    preco_unitario = str(table.loc[line, "preco_unitario"])
    custo = str(table.loc[line, "custo"])
    obs = str(table.loc[line, "obs"])

    pyautogui.click(555, 255)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    if obs != "NaN":
        pyautogui.write(obs)
        pyautogui.press("enter")
