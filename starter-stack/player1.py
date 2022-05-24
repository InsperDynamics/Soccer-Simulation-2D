import os
path = 'starter-stack/Agent/src'
nome = 'insiraNome'
os.chdir(path)
os.system(f'./start.sh -t {nome}')