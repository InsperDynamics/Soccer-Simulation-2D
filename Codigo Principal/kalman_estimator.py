import math

class game_state:
    def __init__(self,):
        self.game_tick = 0
        self.game_isPaused = True
        self.score_left = 0
        self.score_right = 0
        self.playerTimeSinceLastObs = [0] * 22
        self.playerX = [-50, -40, -40, -40, -5, -20, -20, -20, -10, -5, -10, 50, 40, 40, 40, 5, 20, 20, 20, 10, 5, 10]
        self.playerY = [0, 15, 0, -15, -30, 20, 0, -20, 10, 30, -10, 0, 15, 0, -15, -30, 20, 0, -20, 10, 30, -10]
        self.playerVX = [0] * 22
        self.playerVY = [0] * 22
        self.playerBodyAngle = [0] * 11 + [180] * 11
        self.playerNeckAngle = [0] * 11 + [180] * 11
        self.ballTimeSinceLastObs = 0
        self.ballX = 0
        self.ballY = 0
        self.ballVX = 0
        self.ballVY = 0

        self.uniform = 1

    def get_object_absolute_coords(self, obj):
        if obj.distance is None or obj.direction is None or obj.dist_change is None or obj.dir_change is None:
            return None
        dx = obj.distance * math.cos(obj.direction)
        dy = obj.distance * math.sin(obj.direction)
        vx = obj.dist_change * math.cos(obj.dir_change)
        vy = obj.dist_change * math.sin(obj.dir_change)
        return (self.playerX[self.uniform] + dx, self.playerY[self.uniform] + dy, vx, vy)

    def interpret_hear(self, last_message_teammate):
        if last_message_teammate is not None:
            #print(len(last_message_teammate.message), last_message_teammate.message)
            if len(str(last_message_teammate.message)) == 9:
                #formato "NXYNXYNXY" (camisa, x e y do sender e dos 2 jogadores mais próximos a ele)
                characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "(", ")", ".", "+", "*", "/", "?", "<", ">"]
                try:
                    for i in range(3):
                        player_id = characters.index(str(last_message_teammate.message[i * 3]))
                        self.playerX[player_id] = (characters.index(str(last_message_teammate.message[i * 3 + 1])) * 2) - 55
                        self.playerY[player_id] = (characters.index(str(last_message_teammate.message[i * 3 + 2])) * 1) - 35
                except Exception as e:
                    print(e)

    def new_observation(self, self_abs_coords, self_abs_body_dir, self_abs_neck_dir, ball_observation, players_observation):
        (self.playerX[self.uniform], self.playerY[self.uniform]) = self_abs_coords
        self.playerBodyAngle[self.uniform] = self_abs_body_dir
        self.playerNeckAngle[self.uniform] = self_abs_neck_dir
        if ball_observation is not None:
            self.ballTimeSinceLastObs = 0
            abscords = self.get_object_absolute_coords(ball_observation)
            if abscords is not None:
                (self.ballX, self.ballY, self.ballVX, self.ballVY) = abscords
        else:
            self.ballTimeSinceLastObs += 1
        for player_id in range(22):
            self.playerTimeSinceLastObs[player_id] += 1
        for player in players_observation:
            if player.uniform_number is not None:
                if player.side == 'r':
                    player_id = player.uniform_number + 11 - 1
                else:
                    player_id = player.uniform_number - 1
                self.playerTimeSinceLastObs[player_id] = 0
                abscords = self.get_object_absolute_coords(player)
                if abscords is not None:
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