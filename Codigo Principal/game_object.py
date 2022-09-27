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
            "tl50": (-50, -39),
            "tl40": (-40, -39),
            "tl30": (-30, -39),
            "tl20": (-20, -39),
            "tl10": (-10, -39),
            "t0": (0, -40),
            "tr10": (10, -39),
            "tr20": (20, -39),
            "tr30": (30, -39),
            "tr40": (40, -39),
            "tr50": (50, -39),

            "rt30": (57.5, -30),
            "rt20": (57.5, -20),
            "rt10": (57.5, -10),
            "r0": (57.5, 0),
            "rb10": (57.5, 10),
            "rb20": (57.5, 20),
            "rb30": (57.5, 30),

            "bl50": (-50, 39),
            "bl40": (-40, 39),
            "bl30": (-30, 39),
            "bl20": (-20, 39),
            "bl10": (-10, 39),
            "b0": (0, 40),
            "br10": (10, 39),
            "br20": (20, 39),
            "br30": (30, 39),
            "br40": (40, 39),
            "br50": (50, 39),

            "lt30": (-57.5, -30),
            "lt20": (-57.5, -20),
            "lt10": (-57.5, -10),
            "l0": (-57.5, 0),
            "lb10": (-57.5, 10),
            "lb20": (-57.5, 20),
            "lb30": (-57.5, 30),

            # goal flags ('t' and 'b' flags can change based on server parameter
            # 'goal_width', but we leave their coords as the default values.
            # TODO: make goal flag coords dynamic based on server_params
            "glt": (-52.5, -7.01),
            "gl": (-52.5, 0),
            "glb": (-52.5, 7.01),

            "grt": (52.5, -7.01),
            "gr": (52.5, 0),
            "grb": (52.5, 7.01),

            # penalty flags
            "plt": (-36, -20),
            "plc": (-36, 0),
            "plb": (-36, 20),

            "prt": (36, -20),
            "prc": (36, 0),
            "prb": (36, 20),

            # field boundary flags (on boundary lines)
            "lt": (-52.5, -34),
            "ct": (0, -34),
            "rt": (52.5, -34),

            "lb": (-52.5, 34),
            "cb": (0, 34),
            "rb": (52.5, 34),

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

