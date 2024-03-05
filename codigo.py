import pyautogui  # Importa o módulo pyautogui para automatização de UI
import pandas as pd  # Importa o módulo pandas para manipulação de dados
import time  # Importa o módulo time para manipulação de tempo (pausas)

# Define uma pausa de 0.5 segundos após cada comando do pyautogui para evitar sobrecargas
pyautogui.PAUSE = 0.5

# Abrir o google Chrome
pyautogui.press("win")  # Simula a pressão da tecla do Windows
pyautogui.write("chrome")  # Escreve "chrome" para buscar o aplicativo
pyautogui.press("enter")  # Pressiona enter para abrir o aplicativo
pyautogui.hotkey('alt', 'space')  # Abre o menu do sistema da janela ativa
pyautogui.press('x')  # Maximiza a janela do Chrome

# Acessar o site https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Digita a URL do site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")  # Acessa o site pressionando enter
time.sleep(2)  # Espera 2 segundos para a página carregar

# Digitar o login e senha
pyautogui.press("tab")  # Navega para o campo de login usando a tecla tab
pyautogui.write("emailteste@outlook.com")  # Digita o email de login
pyautogui.press("tab")  # Navega para o campo de senha
pyautogui.write("SenhaQualquer")  # Digita a senha

# Clicar em logar
pyautogui.press("enter")  # Pressiona enter para logar
time.sleep(2)  # Espera 2 segundos para o login ser processado

# Importar arquivo CSV
# Carrega os dados do arquivo CSV para um DataFrame
tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:  # Itera sobre cada linha do DataFrame
    # Informar o Código do Produto
    pyautogui.click(x=752, y=290)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # Informar a Marca do Produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Informar o Tipo do Produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # Informar a Categoria do Produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Informar o Preço Unitário do Produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Informar o Custo do Produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Informar a OBS
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # Pressiona enter após preencher todos os campos de uma linha
    pyautogui.press("enter")
    # Realiza um scroll para baixo na página, assumindo a inserção de múltiplos produtos
    pyautogui.scroll(5000)
