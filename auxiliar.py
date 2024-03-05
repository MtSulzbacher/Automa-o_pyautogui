import pyautogui
import time
import pandas as pd

posicao = pyautogui.position()

time.sleep(5)

print(posicao)

tabela = pd.read_csv("produtos.csv")
print(tabela)


# auxiliar para verificar a posição do mouse e o conteudo do arquivo CSV.
