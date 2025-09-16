import pyautogui
import time # -> biblioteca do proprio Python responsavel por fazer controle de tempo entre os codigos

pyautogui.PAUSE = 0.5 # -> definindo Delay entre os comandos

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
