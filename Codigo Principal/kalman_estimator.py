import numpy as np
import math

class game_state:
    def __init__(self,):
        self.uniform = 1
        self.game_tick = 0
        self.game_isPaused = True
        self.score_left = 0
        self.score_right = 0
        self.playerX = [-50, -40, -40, -40, -5, -20, -20, -20, -10, -5, -10, 50, 40, 40, 40, 5, 20, 20, 20, 10, 5, 10]
        self.playerY = [0, 15, 0, -15, -30, 20, 0, -20, 10, 30, -10, 0, 15, 0, -15, -30, 20, 0, -20, 10, 30, -10]
        self.playerVX = [0] * 22
        self.playerVY = [0] * 22
        self.playerBodyAngle = [180] * 11 + [0] * 11
        self.playerNeckAngle = [180] * 11 + [0] * 11
        self.ballX = 0
        self.ballY = 0
        self.ballVX = 0
        self.ballVY = 0
        self.lastPlayerObs = [None]*22
        self.lastBallObs = None
        self.playerTimeSinceLastObs = [0]*22
        self.ballTimeSinceLastObs = 0


    def get_object_absolute_coords(self, obj):
        if obj is None or obj.distance is None or obj.direction is None or obj.dist_change is None or obj.dir_change is None:
            return (None, None, None, None)
        dx = obj.distance * math.cos(obj.direction) 
        dy = obj.distance * math.sin(obj.direction)
        vx = obj.dist_change * math.cos(obj.dir_change) 
        vy = obj.dist_change * math.sin(obj.dir_change)
        return (self.playerX[self.uniform] + dx, self.playerY[self.uniform] + dy, vx, vy) 

    def interpret_hear(self, last_message_teammate):
        if last_message_teammate is not None:
            try:
                #formato "NXYNXYNXYS" (camisa, x e y do sender e dos 2 jogadores mais próximos a ele, e a stamina do sender)
                characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ".", "+", "*", "/", "?", "<", ">"]
                for i in range(3):
                    player_id = characters.index(str(last_message_teammate)[i * 3])
                    self.playerX[player_id] = characters.index(str(last_message_teammate)[i * 3 + 1]) * 2
                    self.playerY[player_id] = characters.index(str(last_message_teammate)[i * 3 + 2]) * 1
                self.playerStamina[characters.index(str(last_message_teammate)[0])] = characters.index(str(last_message_teammate)[9])
            except IndexError:
                pass

    def new_observation(self, self_abs_coords, self_abs_body_dir, self_abs_neck_dir, ball_observation, players_observation):
        (self.playerX[self.uniform], self.playerY[self.uniform]) = self_abs_coords
        self.playerBodyAngle[self.uniform] = self_abs_body_dir
        self.playerNeckAngle[self.uniform] = self_abs_neck_dir
        self.playerTimeSinceLastObs = [x+1 for x in self.playerTimeSinceLastObs]
        self.ballTimeSinceLastObs += 1
        if ball_observation is not None:
            abscords = self.get_object_absolute_coords(ball_observation)
            if abscords[0] is not None:
                self.ballX = self.ballX * 0.5 + abscords[0] * 0.5
                self.ballY = self.ballY * 0.5 + abscords[1] * 0.5
            if abscords[2] is not None:
                self.ballVX = self.ballVX * 0.5 + abscords[2] * 0.5
                self.ballVY = self.ballVY * 0.5 + abscords[3] * 0.5
            self.lastBallObs = ball_observation
            self.ballTimeSinceLastObs = 0
        for player in players_observation:
            if player.uniform_number is not None:
                if player.side == 'r':
                    player_id = player.uniform_number + 11 - 1
                else:
                    player_id = player.uniform_number - 1
                self.playerTimeSinceLastObs[player_id] = 0
                abscords = self.get_object_absolute_coords(player)
                if abscords[0] is not None:
                    self.playerX[player_id] = self.playerX[player_id] * 0.5 + abscords[0] * 0.5
                    self.playerY[player_id] = self.playerY[player_id] * 0.5 + abscords[1] * 0.5
                if abscords[2] is not None:
                    self.playerVX[player_id] = self.playerVX[player_id] * 0.5 + abscords[2] * 0.5
                    self.playerVY[player_id] = self.playerVY[player_id] * 0.5 + abscords[3] * 0.5
                self.playerBodyAngle[player_id] = player.body_direction
                self.playerNeckAngle[player_id] = player.neck_direction
                self.lastPlayerObs[player_id] = player
        return self


class game_state_estimator:
    def __init__(self):
        #inicializar estimador de kalman
        pass

    def update(self, game_state, player_acoes):
        #atualizar estimador de kalman
        #retornar estimativa do game_state atual
        pass