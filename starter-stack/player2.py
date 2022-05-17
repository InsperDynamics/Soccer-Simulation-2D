import os 

def player2():
    os.chdir('Agent1/src')
    os.system('./start.sh -t teamname') #Aqui você pode trocar o nome do time

player2()

#Por enquanto os diretórios estão iguais, porém quando baixarmos mais times é só fazer um commit
# alterar o diretório aqui para mudar o time