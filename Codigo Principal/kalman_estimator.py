import math

class game_state:
    def __init__(self,):
        self.uniform = 1
        self.game_tick = 0
        self.game_isPaused = True
        self.score_left = 0
        self.score_right = 0
        self.playerX = [0] * 22
        self.playerY = [0] * 22
        self.playerVX = [0] * 22
        self.playerVY = [0] * 22
        self.playerBodyAngle = [0] * 22
        self.playerNeckAngle = [0] * 22
        self.playerStamina = [0] * 22
        self.ballX = 0
        self.ballY = 0
        self.ballVX = 0
        self.ballVY = 0

    def get_object_absolute_coords(self, obj):
        if obj.distance is None:
            return None
        dx = obj.distance * math.cos(obj.direction)
        dy = obj.distance * math.sin(obj.direction)
        vx = obj.dist_change * math.cos(obj.dir_change)
        vy = obj.dist_change * math.sin(obj.dir_change)
        return (self.playerX[self.uniform] + dx, self.playerY[self.uniform] + dy, vx, vy)

    def new_observation(self, self_abs_coords, self_abs_body_dir, self_abs_neck_dir, ball_observation, players_observation):
        (self.playerX[self.uniform], self.playerY[self.uniform]) = self_abs_coords
        self.playerBodyAngle[self.uniform] = self_abs_body_dir
        self.playerNeckAngle[self.uniform] = self_abs_neck_dir
        if ball_observation is not None:
            (self.ballX, self.ballY, self.ballVX, self.ballVY) = self.get_object_absolute_coords(ball_observation)
        for player in players_observation:
            if player.uniform_number is not None:
                (self.playerX[player.uniform_number], self.playerY[player.uniform_number], self.playerVX[player.uniform_number], self.playerVY[player.uniform_number]) = self.get_object_absolute_coords(player)
                self.playerBodyAngle[player.uniform_number] = player.body_direction
                self.playerNeckAngle[player.uniform_number] = player.neck_direction
        return self


class game_state_estimator:
    def __init__(self):
        #inicializar estimador de kalman
        pass

    def update(self, game_state, player_acoes):
        #atualizar estimador de kalman
        #retornar estimativa do game_state atual
        pass