
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
        init_address = self.__sock.address
        init_msg = "(init %s (version %d))"
        self.__sock.send(init_msg % (teamname, version))
        while self.__sock.address == init_address:
            time.sleep(0.0001)
            print("waiting")
        self.__think_thread.daemon = True
        self.__connected = True
        print('Sou o Coach e estou conectado')
    
    def __message_loop(self):
        # NAO CHAMAR EXTERNAMENTE!
        while self.__parsing:
            raw_msg = self.__sock.recv()
            msg_type = self.msg_handler.handle_message(raw_msg)
            if msg_type == handler.ActionHandler.CommandType.SENSE_BODY:
                self.__send_commands = True
            self.__should_think_on_data = True
            
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

    coach.connect("localhost", 6002, team_name)


    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminando threads de agentes...")
        print("quitando...")
        sys.exit()


