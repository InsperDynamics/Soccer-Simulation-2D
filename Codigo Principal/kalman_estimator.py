class game_state:
    def __init__(self,):
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

    def new_observation(self, ball_observation, flags_observation, goals_observation, lines_observation, players_observation):
        #estimar variaveis com o self.game_state_estimator e retornar o game_state atualizado
        return self



class game_state_estimator:
    def __init__(self):
        #inicializar estimador de kalman
        pass

    def update(self, game_state, player_acoes):
        #atualizar estimador de kalman
        #retornar estimativa do game_state atual
        pass