import numpy as np

class game_state:
    def __init__(self,):
        self.uniform = 1
        self.game_tick = 0
        self.game_isPaused = True
        self.score_left = 0
        self.score_right = 0
        self.playerX = np.zeros(22)
        self.playerY = np.zeros(22)
        self.playerVX = np.zeros(22)
        self.playerVY = np.zeros(22)
        self.playerBodyAngle = np.zeros(22)
        self.playerNeckAngle = np.zeros(22)
        self.playerStamina = np.zeros(22)
        self.ballX = 0
        self.ballY = 0
        self.ballVX = 0
        self.ballVY = 0
        self.lastPlayerObs = np.zeros(22)
        self.lastBallObs = np.zeros(1)

    def get_object_absolute_coords(self, obj):
        if obj.distance is None:
            return None
        dx = obj.distance * np.cos(obj.direction)
        dy = obj.distance * np.sin(obj.direction)
        vx = obj.dist_change * np.cos(obj.dir_change)
        vy = obj.dist_change * np.sin(obj.dir_change)
        return (self.playerX[self.uniform] + dx, self.playerY[self.uniform] + dy, vx, vy)

    def interpret_hear(self, last_message_teammate):
        #formato "NXYNXYNXYS" (camisa, x e y do sender e dos 2 jogadores mais próximos a ele, e a stamina do sender)
        characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ".", "+", "*", "/", "?", "<", ">"]
        for i in range(3):
            player_id = characters.index(last_message_teammate[i * 3])
            self.playerX[player_id] = characters.index(last_message_teammate[i * 3 + 1]) * 2
            self.playerY[player_id] = characters.index(last_message_teammate[i * 3 + 2]) * 1
        self.playerStamina[characters.index(last_message_teammate[0])] = characters.index(last_message_teammate[9])

    def new_observation(self, self_abs_coords, self_abs_body_dir, self_abs_neck_dir, ball_observation, players_observation):
        (self.playerX[self.uniform], self.playerY[self.uniform]) = self_abs_coords
        self.playerBodyAngle[self.uniform] = self_abs_body_dir
        self.playerNeckAngle[self.uniform] = self_abs_neck_dir
        if ball_observation is not None:
            (self.ballX, self.ballY, self.ballVX, self.ballVY) = self.get_object_absolute_coords(ball_observation)
        for player in players_observation:
            if player.uniform_number is not None:
                if player.side == 'r':
                    player_id = player.uniform_number + 11 - 1
                else:
                    player_id = player.uniform_number - 1
                (self.playerX[player_id], self.playerY[player_id], self.playerVX[player_id], self.playerVY[player_id]) = self.get_object_absolute_coords(player)
                self.playerBodyAngle[player_id] = player.body_direction
                self.playerNeckAngle[player_id] = player.neck_direction
        return self


class game_state_estimator:
    def __init__(self):
        #inicializar estimador de kalman
        pass

    def update(self, game_state, player_acoes):
        #atualizar estimador de kalman
        #retornar estimativa do game_state atual
        pass