
import sys
import multiprocessing as mp
import threading
import time
import sock
import sp_exceptions
import handler
import math
from world_model import WorldModel


class Trainer:
    def __init__(self):
        self.__connected = False
        self.__sock = None
        self.wm = None
        self.game_state = None
        self.game_state_estimator = None
        self.__msg_thread = None
        self.__think_thread = None
        self.in_kick_off_formation = False


    def connect(self, host, port, teamname, version=11):
        if self.__connected:
            msg = "Ja estou conectado!"
            raise sp_exceptions.AgentConnectionStateError(msg)
        self.__sock = sock.Socket(host, port)
        self.wm = WorldModel(handler.ActionHandler(self.__sock))
        self.wm.teamname = teamname
        self.msg_handler = handler.MessageHandler(self.wm)
        # self.game_state = game_state()
        # self.game_state_estimator = game_state_estimator()
        # self.__msg_thread = threading.Thread(target=self.__message_loop, name="message_loop")
        # self.__msg_thread.daemon = True 
        # self.__msg_thread.start()
        init_address = self.__sock.address

        self.__sock.send((teamname, version))
        while self.__sock.address == init_address:
            time.sleep(0.0001)
        self.__think_thread.daemon = True
        self.__connected = True
        print('Sou o Trainer e estou conectado')

    def change_mode(play_mode):
        # modes : kick_off, free_kick, kick_in, or corner_kick, 

        pass

    def move(x,y,vx=0,vy=0):
        pass
    
    def check_ball():
        pass

    def start():
        pass

    def recover():
        pass

    def ear(mode):
        pass

    
        


if __name__ == "__main__":
    team_name = sys.argv[1]

    coach = Trainer()

    coach.connect("localhost", 6001, team_name)


    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminando threads de agentes...")
        print("quitando...")
        sys.exit()


