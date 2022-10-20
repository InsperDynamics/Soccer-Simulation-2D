#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import multiprocessing as mp
import threading
import time
import sock
import sp_exceptions
import handler
import math
from world_model import WorldModel
from estrategia_basica import *
from kalman_estimator import *
from estrategia_ML import *
from coach import *

class Agent:
    def __init__(self):
        self.__connected = False
        self.__sock = None
        self.wm = None
        self.game_state = None
        self.game_state_estimator = None
        self.msg_handler = None
        self.__parsing = False
        self.__msg_thread = None
        self.__thinking = False
        self.__think_thread = None
        self.__should_think_on_data = False
        self.__send_commands = False
        self.in_kick_off_formation = False


    def connect(self, host, port, teamname, goalie, version=11):
        if self.__connected:
            msg = "Ja estou conectado!"
            raise sp_exceptions.AgentConnectionStateError(msg)
        self.__sock = sock.Socket(host, port)
        self.wm = WorldModel(handler.ActionHandler(self.__sock))
        self.wm.teamname = teamname
        self.msg_handler = handler.MessageHandler(self.wm)
        self.game_state = game_state()
        self.game_state_estimator = game_state_estimator()
        self.__parsing = True
        self.__msg_thread = threading.Thread(target=self.__message_loop, name="message_loop")
        self.__msg_thread.daemon = True 
        self.__msg_thread.start()
        init_address = self.__sock.address
        if goalie:
            init_msg = "(init %s (version %d)(goalie))"
        else:
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

    def transmit_say(self, selfX, selfY, selfSTA):
        #formato "NXYNXYNXYS" (camisa, x e y de si mesmo e dos 2 jogadores mais próximos, e a stamina de si mesmo)
        disttoself = []
        for i in range(22):
            try:
                disttoself.append(math.sqrt((selfX - self.game_state.playerX[i])**2 + (selfY - self.game_state.playerY[i])**2))
            except IndexError:
                pass
        idsofsorted = sorted(range(len(disttoself)), key=lambda k: disttoself[k])
        if len(idsofsorted) > 2:
            msg = ""
            characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ".", "+", "*", "/", "?", "<", ">"]
            for playerid in idsofsorted[0:3]:
                msg += characters[playerid]
                msg += characters[int(round((self.game_state.playerX[playerid] + 55)/2))]
                msg += characters[int(round(self.game_state.playerY[playerid] + 35))]
            msg += characters[int(round(selfSTA))]
            self.wm.ah.say(msg)

    def transmit_pointto(self, selfX, selfY):
        disttoself = math.sqrt((selfX - self.ballX)**2 + (selfY - self.ballY)**2)
        dirtoself = math.atan2(self.ballY - selfY, self.ballX - selfX)
        if dirtoself < 0:
            dirtoself += 2*math.pi
        dirtoself = dirtoself*180/math.pi
        self.wm.ah.pointto(disttoself, dirtoself)


    def think(self):
        #IMPLEMENTACAO DA ESTRATEGIA VEM AQUI!
        if not self.__think_thread.is_alive() or not self.__msg_thread.is_alive():
            raise Exception("Uma thread morreu!")
        formacaoKickoff(self, WorldModel)
        #ataqueBasico(self, WorldModel)
        acaoJogadores = queryModel(game_state)
        if self.wm.side == WorldModel.SIDE_L:
            selfX = self.game_state.playerX[self.wm.uniform_number - 1]
            selfY = self.game_state.playerY[self.wm.uniform_number - 1]
            selfSTA = self.game_state.playerStamina[self.wm.uniform_number - 1]
            acao = acaoJogadores[self.wm.uniform_number - 1]
        else:
            selfX = self.game_state.playerX[11 + self.wm.uniform_number - 1]
            selfY = self.game_state.playerY[11 + self.wm.uniform_number - 1]
            selfSTA = self.game_state.playerStamina[11 + self.wm.uniform_number - 1]
            acao = acaoJogadores[11 + self.wm.uniform_number - 1]
        self.transmit_say(selfX, selfY, selfSTA)
        self.transmit_pointto(selfX, selfY)
        #chamar funcoes do self.wm.ah baseado na acao (olhar handler.py)
        self.game_state.game_tick = self.wm.sim_time
        self.game_state.game_isPaused = (not self.wm.play_mode == WorldModel.PlayModes.PLAY_ON)
        self.game_state.score_left = self.wm.score_l
        self.game_state.score_right = self.wm.score_r
        self.game_state = self.game_state.new_observation(self.wm.ball, self.wm.flags, self.wm.goals, self.wm.lines, self.wm.players)
        self.game_state_estimator.update(self.game_state, acaoJogadores)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Argumentos de programa insuficientes (preciso do nome da equipe e do numero de players)")
        sys.exit()
    team_name = sys.argv[1]
    num_players = int(sys.argv[2])


    def spawn_agent(team_name, goalie):
        a = Agent()
        a.connect("localhost", 6000, team_name, goalie=goalie)
        # a.play()
        while 1:
            time.sleep(1)

    agentthreads = []
    for agent in range(num_players):
        if agent == 0:
            print("Spawnando goleiro...")
            at = mp.Process(target=spawn_agent, args=(sys.argv[1],True,))
        else:
            print("Spawnando agente {}...".format(agent))
            at = mp.Process(target=spawn_agent, args=(sys.argv[1],False,))
        at.daemon = True
        at.start()
        agentthreads.append(at)



    try:
        while 1:
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Terminando threads de agentes...")
        for at in agentthreads:
            at.terminate()
        print("quitando...")
        sys.exit()

