import pyautogui
import time # -> biblioteca do proprio Python responsavel por fazer controle de tempo
import pandas

pyautogui.PAUSE = 0.2 # -> definindo Delay entre os comandos

pyautogui.press("win") # -> press serve pra apertar 1 tecla
pyautogui.write("opera") # -> write serve pra escrever textos
pyautogui.press("enter")


# Digitando o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # -> definindo que o codigo vai pausar por 3 Segundos após o site ser digitado

pyautogui.click(x=725, y=388) # -> clica na posição da barra de email
pyautogui.write("bananas")


pyautogui.press("tab") # -> aperta TAB para mudar o campo na tela (mudando de email - > senha - > logar)

pyautogui.write("123") # -> digitando senha

pyautogui.press("tab") 
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv") # -> usando o pandas pra ler o CSV e armazenar as informações dentro da variavel Tabela



for linha in tabela.index: # -> Loop pra prencher o formulario de produtos 
# -> o pandas transforma o arquivo CSV em um DataFrame (Parecido com Excel)
 # -> depois disso o pandas o .index vai linha por linha da tabela 
    pyautogui.click(x=753, y=280)

    codigo = tabela.loc[linha, "codigo"] # -> o loc serve pra especificar pegar a coluna, dentro vc passa 2 parametros, Linha (Linha da tabela) 
    # e nome da coluna
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # -> aqui é necessario mudar o tipo pra String para que possa ser escrito pela automação

    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
