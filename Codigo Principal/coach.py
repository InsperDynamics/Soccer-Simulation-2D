
import sys
import multiprocessing as mp
import threading
import time
import sock
import sp_exceptions
import handler
from math import *
from world_model import WorldModel


class Coach:
    def __init__(self):
        self.team_name = team_name
        self.__connected = False
        self.__sock = None
        self.wm = None
        self.game_state = None
        self.game_state_estimator = None
        self.__msg_thread = None
        self.__think_thread = None
        self.__should_think_on_data = False
        self.__send_commands = False
        self.in_kick_off_formation = False
        self.eye = False
        self.msg_atual = None
        self.compression = None

    def connect(self, host, port, teamname, version=11):
        if self.__connected:
            msg = "Ja estou conectado!"
            raise sp_exceptions.AgentConnectionStateError(msg)
        self.__sock = sock.Socket(host, port)
        self.wm = WorldModel(handler.ActionHandler(self.__sock))
        self.wm.teamname = teamname
        # self.msg_handler = handler.MessageHandler(self.wm)
        init_address = self.__sock.address
        self.__parsing = True
        self.__msg_thread = threading.Thread(target=self.__message_loop, name="message_loop")
        # self.__msg_thread.daemon = True 
        self.__msg_thread.start()
        init_msg = "(init %s (version %d))"
        self.__sock.send(init_msg % (teamname, version))
        while self.__sock.address == init_address:
            time.sleep(0.0001)
        self.__connected = True
        print('Sou o Coach e estou conectado')
    
    def __message_loop(self):
        # NAO CHAMAR EXTERNAMENTE!
        while self.__parsing:
            raw_msg = self.__sock.recv()
            # msg_type = self.msg_handler.handle_message(raw_msg)
            # if msg_type == handler.ActionHandler.CommandType.SENSE_BODY:
            #     self.__send_commands = True
            # self.__should_think_on_data = True

    def think(self):
        #IMPLEMENTACAO DA ESTRATEGIA VEM AQUI!
        if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
            raise Exception("Uma thread morreu!")
        print("Sou o Coach e estou pensando")

    def __think_loop(self):
        # NAO CHAMAR EXTERNAMENTE!
        while self.__thinking:
            if self.__send_commands:
                self.__send_commands = False
                self.wm.ah.send_commands()
            if self.__should_think_on_data:
                self.__should_think_on_data = False
                self.think()
            else:
                time.sleep(0.0001)

    def bye(self):
        print('Byee')
        sys.exit()

    def check_ball(self,):
        x,y = self.wm.get_object_absolute_coords(obj)
        return x,y

    def look(self,obj):
        x,y = self.wm.get_object_absolute_coords(obj)


        pass

    def team_names(self):
        #Devolver o nome dos times
        pass

    
    def eye(self,boolean):
        self.eye = boolean

    def change_player_type(self,num,player_type): 
        #saber acessar os player pelos números
        pass 

    def say(self,clang_msg):
        self.msg_atual = clang_msg

    def compression(self,level):
        #Olhar a sessão no regulamento para entender
        self.compression = level
        pass

    def done(self):
        pass 

    def illegal(self,):
        pass 

    def change_mode(self, play_mode):
        # modes : kick_off, free_kick, kick_in, or corner_kick, 
        self.wm.play_mode = play_mode

    def move_player(self,object,x,y,vx=0,vy=0): #object pode ser player ou bola
        distance = sqrt(x**2 + y**2)
        direction = atan(y/x) - atan(object.direction)
        object.distance = distance
        object.direction = direction

    
        


if __name__ == "__main__":
    team_name = sys.argv[1]

    coach = Coach()

    coach.connect("localhost", 6002, team_name)


    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminando threads de agentes...")
        print("quitando...")
        sys.exit()


