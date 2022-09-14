import collections
import queue
import message_parser
import sp_exceptions
import game_object
from world_model import WorldModel
PRINT_SERVER_MESSAGES = False
PRINT_SENT_COMMANDS = False

class MessageHandler:
    #handler para mensagens recebidas

    Message = collections.namedtuple("Message", "time sender message")

    def __init__(self, world_model):
        self.wm = world_model

    def handle_message(self, msg):
        parsed = message_parser.parse(msg)
        if parsed:
            if PRINT_SERVER_MESSAGES:
                print(parsed[0] + ":", parsed[1:], "\n")
            msg_func = "_handle_%s" % parsed[0]
            if hasattr(self, msg_func):
                getattr(self, msg_func).__call__(parsed)
            else:
                m = "Can't handle message type '%s', function '%s' not found."
                raise sp_exceptions.MessageTypeError(m % (parsed[0], msg_func))
            return parsed[0] #tipo da mensagem recebida

    def _handle_see(self, msg):
        sim_time = msg[1]
        new_ball = None
        new_flags = []
        new_goals = []
        new_lines = []
        new_players = []
        for obj in msg[2:]:
            name = obj[0]
            members = obj[1:]
            distance = None
            direction = None
            dist_change = None
            dir_change = None
            body_dir = None
            neck_dir = None
            if len(members) == 1:
                direction = members[0]
            elif len(members) >= 2:
                distance = members[0]
                direction = members[1]
                if len(members) >= 4:
                    dist_change = members[2]
                    dir_change = members[3]
                if len(members) >= 6:
                    body_dir = members[4]
                    neck_dir = members[5]
            # parse caso flag
            if name[0] == 'f':
                name[-1] = str(name[-1])
                flag_id = ''.join(name[1:])
                new_flags.append(game_object.Flag(distance, direction, flag_id))
            # parse caso player
            elif name[0] == 'p':
                teamname = None
                uniform_number = None
                if len(name) >= 2:
                    teamname = name[1]
                elif len(name) >= 3:
                    uniform_number = name[2]
                elif len(name) >= 4:
                    position = name[3]
                side = None
                if teamname is not None:
                    if teamname == self.wm.teamname:
                        side = self.wm.side
                    else:
                        if self.wm.side == WorldModel.SIDE_L:
                            side = WorldModel.SIDE_R
                        else:
                            side = WorldModel.SIDE_L
                # calcula velocidade do player (ainda nao implementamos isso)
                speed = None
                new_players.append(game_object.Player(distance, direction,
                    dist_change, dir_change, speed, teamname, side,
                    uniform_number, body_dir, neck_dir))
            # parse caso gol
            elif name[0] == 'g':
                goal_id = None
                if len(name) > 1:
                    goal_id = name[1]
                new_goals.append(game_object.Goal(distance, direction, goal_id))
            # parse caso linha
            elif name[0] == 'l':
                line_id = None
                if len(name) > 1:
                    line_id = name[1]
                new_lines.append(game_object.Line(distance, direction, line_id))
            # parse caso bola
            elif name[0] == 'b':
                # calcula velocidade da bola (ainda nao implementamos isso)
                speed = None
                new_ball = game_object.Ball(distance, direction, dist_change,
                        dir_change, speed)
            # parse caso bola muito longe
            elif name[0] == 'B':
                new_ball = game_object.Ball(None, None, None, None, None)
            # parse caso flag muito longe
            elif name[0] == 'F':
                new_flags.append(game_object.Flag(None, None, None))
            # parse caso gol muito longe
            elif name[0] == 'G':
                new_goals.append(game_object.Goal(None, None, None))
            # parse caso player muito longe
            elif name[0] == 'P':
                new_players.append(game_object.Player(None, None, None, None,
                    None, None, None, None, None, None))

        self.wm.process_new_info(new_ball, new_flags, new_goals, new_players,
                new_lines)

    def _handle_hear(self, msg):
        """
        Parses audible information and turns it into useful information.
        """

        time_recvd = msg[1] # server cycle when message was heard
        sender = msg[2] # name (or direction) of who sent the message
        message = msg[3] # message string

        # ignore messages sent by self (NOTE: would anybody really want these?)
        if sender == "self":
            return

        # handle messages from the referee, to update game state
        elif sender == "referee":
            # change the name for convenience's sake
            mode = message

            # deal first with messages that shouldn't be passed on to the agent

            # keep track of scores by setting them to the value reported.  this
            # precludes any possibility of getting out of sync with the server.
            if mode.startswith(WorldModel.RefereeMessages.GOAL_L):
                # split off the number, the part after the rightmost '_'
                self.wm.score_l = int(mode.rsplit("_", 1)[1])
                return
            elif mode.startswith(WorldModel.RefereeMessages.GOAL_R):
                self.wm.score_r = int(mode.rsplit("_", 1)[1])
                return

            # ignore these messages, but pass them on to the agent. these don't
            # change state but could still be useful.
            elif mode in (WorldModel.RefereeMessages.FOUL_L, WorldModel.RefereeMessages.FOUL_R, WorldModel.RefereeMessages.GOALIE_CATCH_BALL_L, WorldModel.RefereeMessages.GOALIE_CATCH_BALL_R, WorldModel.RefereeMessages.TIME_UP_WITHOUT_A_TEAM, WorldModel.RefereeMessages.HALF_TIME, WorldModel.RefereeMessages.TIME_EXTENDED):

                # messages are named 3-tuples of (time, sender, message)
                ref_msg = self.Message(time_recvd, sender, message)

                # pass this message on to the player and return
                self.wm.last_message = ref_msg
                return

            # deal with messages that indicate game mode, but that the agent
            # doesn't need to know about specifically.
            else:
                # set the mode to the referee reported mode string
                self.wm.play_mode = mode
                return

        # all other messages are treated equally
        else:
            # update the model's last heard message
            new_msg = MessageHandler.Message(time_recvd, sender, message)
            self.wm.prev_message = new_msg

    def _handle_sense_body(self, msg):
        """
        Deals with the agent's body model information.
        """

        # update the body model information when received. each piece of info is
        # a list with the first item as the name of the data, and the rest as
        # the values.
        for info in msg[2:]:
            name = info[0]
            values = info[1:]

            if name == "view_mode":
                self.wm.view_quality = values[0]
                self.wm.view_width = values[1]
            elif name == "stamina":
                self.wm.stamina = values[0]
                self.wm.effort = values[1]
            elif name == "speed":
                self.wm.speed_amount = values[0]
                self.wm.speed_direction = values[1]
            elif name == "head_angle":
                self.wm.neck_direction = values[0]

            # these update the counts of the basic actions taken
            elif name == "kick":
                self.wm.kick_count = values[0]
            elif name == "dash":
                self.wm.dash_count = values[0]
            elif name == "turn":
                self.wm.turn_count = values[0]
            elif name == "say":
                self.wm.say_count = values[0]
            elif name == "turn_neck":
                self.wm.turn_neck_count = values[0]
            elif name == "catch":
                self.wm.catch_count = values[0]
            elif name == "move":
                self.wm.move_count = values[0]
            elif name == "change_view":
                self.wm.change_view_count = values[0]

            # we leave unknown values out of the equation
            else:
                pass

    def _handle_change_player_type(self, msg):
        """
        Handle player change messages.
        """

    def _handle_player_param(self, msg):
        """
        Deals with player parameter information.
        """

    def _handle_player_type(self, msg):
        """
        Handles player type information.
        """

    def _handle_server_param(self, msg):
        """
        Stores server parameter information.
        """
        for param in msg[1:]:
            if len(param) != 2:
                continue
            key = param[0]
            value = param[1]
            if hasattr(self.wm.server_parameters, key):
                setattr(self.wm.server_parameters, key, value)
            else:
                raise AttributeError("Couldn't find a matching parameter in "
                        "ServerParameters class: '%s'" % key)

    def _handle_init(self, msg):
        side = msg[1]
        uniform_number = msg[2]
        play_mode = msg[3]
        self.wm.side = side
        self.wm.uniform_number = uniform_number
        self.wm.play_mode = play_mode

    @staticmethod
    def _handle_error(msg):
        m = "Server retornou um erro: '%s'" % msg[1]
        raise sp_exceptions.SoccerServerError(m)

    @staticmethod
    def _handle_warning(msg):
        m = "Server retornou um warning: '%s'" % msg[1]
        print(sp_exceptions.SoccerServerWarning(m))


class ActionHandler:
    #handler para enviar mensagens

    class CommandType:
        TYPE_PRIMARY = 0
        TYPE_SECONDARY = 1
        CATCH = "catch"
        CHANGE_VIEW = "change_view"
        DASH = "dash"
        KICK = "kick"
        MOVE = "move"
        SAY = "say"
        SENSE_BODY = "sense_body"
        TURN = "turn"
        TURN_NECK = "turn_neck"
        def __init__(self):
            raise NotImplementedError("Não é possível instanciar um CommandType, acesse seus membros por meio de ActionHandler")

    Command = collections.namedtuple("Command", "cmd_type text")

    def __init__(self, server_socket):
        self.sock = server_socket
        self.q = queue.Queue()

    def send_commands(self):
        # envia todos os comandos colocados na fila
        # o comando primario vai por ultimo
        primary_cmd = None
        while 1:
            try:
                cmd = self.q.get_nowait()
            except queue.Empty:
                break
            if cmd.cmd_type == ActionHandler.CommandType.TYPE_PRIMARY:
                primary_cmd = cmd
            else:
                if PRINT_SENT_COMMANDS:
                    print("sent:", cmd.text)
                self.sock.send(cmd.text)
            self.q.task_done()
        if primary_cmd is not None:
            if PRINT_SENT_COMMANDS:
                print("sent:", primary_cmd.text)
            self.sock.send(primary_cmd.text)

    def move(self, x, y):
        #teleportar
        msg = "(move %.10f %.10f)" % (x, y)
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def turn(self, relative_degrees):
        msg = "(turn %.10f)" % relative_degrees
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def dash(self, power):
        msg = "(dash %.10f)" % power
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        # print(msg)
        self.q.put(cmd)

    def kick(self, power, relative_direction):
        msg = f"(kick {power} {relative_direction})"
        #msg = "(kick %.10f %.10f)" % (power, relative_direction)
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        print(msg)
        self.q.put(cmd)

    def catch(self, relative_direction):
        msg = "(catch %.10f)" % relative_direction
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def tackle(self, relative_direction):
        msg = "(tackle %.10f)" % relative_direction
        cmd_type = ActionHandler.CommandType.TYPE_PRIMARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def say(self, message):
        msg = "(say %s)" % message
        cmd_type = ActionHandler.CommandType.TYPE_SECONDARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def attentionto(self, teamname='our', unum=1, off=False):
        if not off:
            msg = "(attentionto %s %d)" % (teamname, unum)
        else:
            msg = "(attentionto off)"
        cmd_type = ActionHandler.CommandType.TYPE_SECONDARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def pointto(self, dist=0, direction=0, off=False):
        if not off:
            msg = "(pointto %.10f %.10f)" % (dist, direction)
        else:
            msg = "(pointto off)"
        cmd_type = ActionHandler.CommandType.TYPE_SECONDARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def turn_neck(self, relative_direction):
        msg = "(turn_neck %.10f)" % relative_direction
        cmd_type = ActionHandler.CommandType.TYPE_SECONDARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

    def change_view(self, width, quality):
        msg = "(change_view %s %s)" % (width, quality)
        cmd_type = ActionHandler.CommandType.TYPE_SECONDARY
        cmd = ActionHandler.Command(cmd_type, msg)
        self.q.put(cmd)

