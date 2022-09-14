import os
path = 'starter-stack/Agent/src'
nome = 'insiraOutroNome'
os.chdir(path)
os.system(f'./start.sh -t {nome}')