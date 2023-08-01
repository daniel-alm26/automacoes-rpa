import pyautogui as p

p.sleep(1)
p.doubleClick(x=199, y=46)
p.sleep(4)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(6)

localPesq = p.locateOnScreen('Pesquisa2.PNG', confidence=0.8)
localPesquisa = p.center(localPesq)
xPesquisa, yPesquisa = localPesquisa
p.moveTo(xPesquisa, yPesquisa, duration=2)
p.click(xPesquisa, yPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
p.sleep(6)
p.screenshot('Cursos.png')
p.sleep(3)

localClo = p.locateOnScreen('Close2.PNG', confidence=0.8)
localClose = p.center(localClo)
xClose, yClose = localClose
p.moveTo(xClose, yClose, duration=2)
p.click(xClose, yClose)



#p.sleep(2)


#print(p.position())