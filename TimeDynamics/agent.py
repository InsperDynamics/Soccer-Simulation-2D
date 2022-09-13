#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import multiprocessing as mp
import threading
import time
from estrategia_ataque import estrategiaAtaque
import sock
import sp_exceptions
import handler
from world_model import WorldModel
from estrategia_basica import *
from estrategia_ataque import *

class Agent:
    def __init__(self):
        self.__connected = False
        self.__sock = None
        self.wm = None
        self.msg_handler = None
        self.__parsing = False
        self.__msg_thread = None
        self.__thinking = False
        self.__think_thread = None
        self.__should_think_on_data = False
        self.__send_commands = False
        self.in_kick_off_formation = False
        self.goalie = False


    def connect(self, host, port, teamname, version=11):
        if self.__connected:
            msg = "Ja estou conectado!"
            raise sp_exceptions.AgentConnectionStateError(msg)

        self.__sock = sock.Socket(host, port)
        self.wm = WorldModel(handler.ActionHandler(self.__sock))
        self.wm.teamname = teamname
        self.msg_handler = handler.MessageHandler(self.wm)

        self.__parsing = True
        self.__msg_thread = threading.Thread(target=self.__message_loop, name="message_loop")
        self.__msg_thread.daemon = True 
        self.__msg_thread.start()

        init_address = self.__sock.address
        init_msg = "(init %s (version %d))"
        self.__sock.send(init_msg % (teamname, version))
        while self.__sock.address == init_address:
            time.sleep(0.0001)

        self.__thinking = False
        self.__think_thread = threading.Thread(target=self.__think_loop, name="think_loop")
        self.__think_thread.daemon = True

        self.__connected = True


    def play(self):
        if not self.__connected:
            msg = "Ainda nao estou conectado!"
            raise sp_exceptions.AgentConnectionStateError(msg)
        if self.__thinking:
            raise sp_exceptions.AgentAlreadyPlayingError("Ja estou jogando!")
        self.in_kick_off_formation = False
        self.__thinking = True
        self.__should_think_on_data = True
        self.__think_thread.start()


    def disconnect(self):
        if not self.__connected:
            return
        self.__parsing = False
        self.__thinking = False
        self.__sock.send("desconectando...")
        if self.__msg_thread.is_alive():
            self.__msg_thread.join(0.01)
        if self.__think_thread.is_alive():
            self.__think_thread.join(0.01)
        Agent.__init__(self)


    def __message_loop(self):
        # NAO CHAMAR EXTERNAMENTE!
        while self.__parsing:
            raw_msg = self.__sock.recv()
            msg_type = self.msg_handler.handle_message(raw_msg)
            if msg_type == handler.ActionHandler.CommandType.SENSE_BODY:
                self.__send_commands = True
            self.__should_think_on_data = True


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


    def think(self):
        if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
            raise Exception("Uma thread morreu!")
        #IMPLEMENTACAO DA ESTRATEGIA VEM AQUI
        estrategiaBasica(self, WorldModel)
        estrategiaAtaque(self, WorldModel)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Argumentos de programa insuficientes (preciso do nome da equipe e do numero de players)")
        sys.exit()
    team_name = sys.argv[1]
    num_players = int(sys.argv[2])

    def spawn_agent(team_name):
        a = Agent()
        a.connect("localhost", 6000, team_name)
        a.play()
        while 1:
            time.sleep(1)

    agentthreads = []
    for agent in range(num_players):
        print("Spawnando agente {}...".format(agent))
        at = mp.Process(target=spawn_agent, args=(sys.argv[1],))
        # at = mp.Process(target=spawn_agent, args=(team_name,)) também deve funcionar

        at.daemon = True
        at.start()
        agentthreads.append(at)
    print("Agentes iniciados")  

    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminando threads de agentes...")
        for at in agentthreads:
            at.terminate()
        print("quitando...")
        sys.exit()

