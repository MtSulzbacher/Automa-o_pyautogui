# README para Script de Automação com PyAutoGUI e Pandas

## Descrição

Este script automatiza a tarefa de preenchimento de informações de produtos em um website específico a partir de dados contidos em um arquivo CSV. Utiliza o módulo `pyautogui` para controlar o teclado e o mouse, simulando a interação do usuário com a interface gráfica, e o módulo `pandas` para a manipulação dos dados dos produtos. As principais ações realizadas pelo script incluem abrir o Google Chrome, acessar um site, fazer login e preencher os campos de um formulário com os dados dos produtos.

## Requisitos

- Python 3.x
- PyAutoGUI
- Pandas
- Google Chrome instalado

## Instalação

Para utilizar este script, você primeiro precisa instalar o Python 3.x em seu sistema, caso ainda não tenha. Após a instalação do Python, você precisará instalar as bibliotecas PyAutoGUI e Pandas. Isso pode ser feito através do pip, o gerenciador de pacotes do Python, com os seguintes comandos:

```
pip install pyautogui pandas
```

## Uso

Antes de executar o script, certifique-se de que o arquivo `produtos.csv` contendo os dados dos produtos está na mesma pasta que o script e está formatado corretamente. O arquivo CSV deve ter as colunas `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo` e `obs`, com cada produto em sua própria linha.

Para executar o script, navegue até o diretório contendo o arquivo do script e execute o seguinte comando no terminal ou prompt de comando:

```
python nome_do_script.py
```

Certifique-se de que o Google Chrome esteja acessível e que as coordenadas usadas no script para cliques do mouse correspondam à resolução da sua tela e ao layout da página. Você pode precisar ajustar essas coordenadas no script para que ele funcione corretamente em sua configuração.

## Aviso

Este script depende da posição dos elementos da interface gráfica, que podem variar conforme a resolução da tela, o tamanho da janela do navegador e possíveis atualizações na página web de destino. Portanto, pode ser necessário ajustar as coordenadas de cliques do mouse e a ordem de tabulação para campos de formulário para garantir o funcionamento correto do script em ambientes diferentes. Utilize este script com cautela e sempre teste em um ambiente seguro para evitar preencher informações incorretas ou realizar ações indesejadas.
