
import sys
import multiprocessing as mp
import threading
import time
import sock
import sp_exceptions
import handler
from math import *
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
    
    def check_ball(self,):
        pass

    def look(self,):
        pass

    def team_names(self,):
        pass

    def ear(self,mode):
        
        pass
    
    def eye(self,):
        pass


    def move(self,):
        pass 
    
    def recover(self,):
        pass 

    def change_player_type(self,):
        pass 


    def say(self,):
        pass 

    def compression(self,):
        pass

    def done(self,):
        pass 

    def illegal(self,):
        pass 

    

    def change_mode(self, play_mode):
        # modes : kick_off, free_kick, kick_in, or corner_kick, 
        self.wm.play_mode = play_mode
        pass

    def move_player(self,object,x,y,vx=0,vy=0): #object pode ser player ou bola
        distance = sqrt(x**2 + y**2)
        direction = atan(y/x) - atan(object.direction)
        object.distance = distance
        object.direction = direction

        pass

    def move_ball(self,object,x,y,vx=0,vy=0): #object pode ser player ou bola
        distance = sqrt(x**2 + y**2)

        pass
    

    def start(self):
        self.wm.play_mode = "kick_off_l"


    def recover(self):
        self.wm.stamina = 8000

    
        


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


