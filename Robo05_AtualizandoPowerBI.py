import pyautogui as p

    # Iniciar o arquivo RPA.pbix para abrir o PowerBI
p.hotkey('win', 'r')
p.sleep(1)
p.write('C:\RPA.pbix')
p.sleep(2)
p.press('enter')

    # Aguardando o PowerBI abrir o arquivo RPA.pbix. Obs.: Coloquei 100 secundos, pois o notebook é lento.
p.sleep(80)
p.click(x=720, y=96)
p.sleep(30)

    # Clicar no botão atualizar dentro do PowerBI para atualizar o Dash/Arquivo RPA.pbix
p.click(x=1346, y=14)
p.sleep(10)

    # Clicar no "X" para fechar o PowerBI
p.click(x=682, y=400)

    # Para descobrir as coordenadas da ação que você deseja
#p.sleep(3)
#print(p.position())