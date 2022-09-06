class GameObject:
    #classe raiz de todos os objetos do jogo
    def __init__(self, distance, direction):
        #distancia e angulo em relacao ao jogador
        self.distance = distance
        self.direction = direction

class Line(GameObject):
    def __init__(self, distance, direction, line_id):
        self.line_id = line_id
        GameObject.__init__(self, distance, direction)

class Goal(GameObject):
    def __init__(self, distance, direction, goal_id):
        self.goal_id = goal_id
        GameObject.__init__(self, distance, direction)

class Flag(GameObject):
    # a dictionary mapping all flag_ids to their on-field (x, y) coordinates
    # TODO: these are educated guesses based on Figure 4.2 in the documentation.
    #       where would one find the actual coordinates, besides in the server
    #       code?
    FLAG_COORDS = {
            # perimiter flags
            "tl50": (-50, -40),
            "tl40": (-40, -40),
            "tl30": (-30, -40),
            "tl20": (-20, -40),
            "tl10": (-10, -40),
            "t0": (0, -40),
            "tr10": (10, -40),
            "tr20": (20, -40),
            "tr30": (30, -40),
            "tr40": (40, -40),
            "tr50": (50, -40),

            "rt30": (60, -30),
            "rt20": (60, -20),
            "rt10": (60, -10),
            "r0": (60, 0),
            "rb10": (60, 10),
            "rb20": (60, 20),
            "rb30": (60, 30),

            "bl50": (-50, 40),
            "bl40": (-40, 40),
            "bl30": (-30, 40),
            "bl20": (-20, 40),
            "bl10": (-10, 40),
            "b0": (0, 40),
            "br10": (10, 40),
            "br20": (20, 40),
            "br30": (30, 40),
            "br40": (40, 40),
            "br50": (50, 40),

            "lt30": (-60, -30),
            "lt20": (-60, -20),
            "lt10": (-60, -10),
            "l0": (-60, 0),
            "lb10": (-60, 10),
            "lb20": (-60, 20),
            "lb30": (-60, 30),

            # goal flags ('t' and 'b' flags can change based on server parameter
            # 'goal_width', but we leave their coords as the default values.
            # TODO: make goal flag coords dynamic based on server_params
            "glt": (-55, -7.01),
            "gl": (-55, 0),
            "glb": (-55, 7.01),

            "grt": (55, -7.01),
            "gr": (55, 0),
            "grb": (55, 7.01),

            # penalty flags
            "plt": (-35, -20),
            "plc": (-35, 0),
            "plb": (-32, 20),

            "prt": (35, -20),
            "prc": (35, 0),
            "prb": (32, 20),

            # field boundary flags (on boundary lines)
            "lt": (-55, -35),
            "ct": (0, -35),
            "rt": (55, -35),

            "lb": (-55, 35),
            "cb": (0, 35),
            "rb": (55, 35),

            # center flag
            "c": (0, 0)
        }
    def __init__(self, distance, direction, flag_id):
        self.flag_id = flag_id
        GameObject.__init__(self, distance, direction)

class MobileObject(GameObject):
    #classe raiz de objetos que se movem (tambem filha de gameobject)
    def __init__(self, distance, direction, dist_change, dir_change, speed):
        #alem de posicao e direcao possuem velocidade e direcao de movimento
        self.dist_change = dist_change
        self.dir_change = dir_change
        self.speed = speed
        GameObject.__init__(self, distance, direction)

class Ball(MobileObject):
    def __init__(self, distance, direction, dist_change, dir_change, speed):
        MobileObject.__init__(self, distance, direction, dist_change, dir_change, speed)

class Player(MobileObject):
    def __init__(self, distance, direction, dist_change, dir_change, speed, team, side, uniform_number, body_direction, neck_direction):
        self.team = team
        self.side = side
        self.uniform_number = uniform_number
        self.body_direction = body_direction
        self.neck_direction = neck_direction
        MobileObject.__init__(self, distance, direction, dist_change, dir_change, speed)

