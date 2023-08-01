import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('Oi!!! Eu sou um Bot!')
p.sleep(2)
valor = p.getActiveWindow()
valor.close()
p.press('right')
p.sleep(2)
p.press('enter')

#p.moveTo(x=110, y=562, duration=3)
#p.click(x=110, y=562)

#p.sleep(2)
#print(p.position())

#p.hotkey('win', 'r') # Consigo passar para ele teclas de atalho do meu teclado. Consegue executar através                       dessa função 'hotkey()' as teclas do meu teclado.

#p.sleep(1)

#p.typewrite('notepad') # Esse comando serve para escrever um texto.

#p.sleep(2)

#p.press('enter') # Para pressionar uma tecla do teclado, diferente de 'click' que é para clicar em algum                    arquivo/aplicativo

#valor = p.getActiveWindow() # Pega qual janela está aberta. Vai identificar qual janela está aberta no momento

#valor.close() # Para fechar a janela que está ativa no momento.