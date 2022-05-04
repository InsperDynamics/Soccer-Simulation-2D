import os 

def server():
    os.chdir('rcssserver-15.2.2/src')
    os.system('rcssserver')

server()