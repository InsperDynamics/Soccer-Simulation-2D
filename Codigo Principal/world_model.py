import math
import random
import game_object

class WorldModel:
    SIDE_L = "l"
    SIDE_R = "r"

    class PlayModes:
        BEFORE_KICK_OFF = "before_kick_off"
        PLAY_ON = "play_on"
        TIME_OVER = "time_over"
        KICK_OFF_L = "kick_off_l"
        KICK_OFF_R = "kick_off_r"
        KICK_IN_L = "kick_in_l"
        KICK_IN_R = "kick_in_r"
        FREE_KICK_L = "free_kick_l"
        FREE_KICK_R = "free_kick_r"
        CORNER_KICK_L = "corner_kick_l"
        CORNER_KICK_R = "corner_kick_r"
        GOAL_KICK_L = "goal_kick_l"
        GOAL_KICK_R = "goal_kick_r"
        DROP_BALL = "drop_ball"
        OFFSIDE_L = "offside_l"
        OFFSIDE_R = "offside_r"
        GOAL_L = "goal_l"
        GOAL_R = "goal_r"
        def __init__(self):
            raise NotImplementedError("Nao crie um objeto playmode. Acesse pelo WorldModel")

    class RefereeMessages:
        FOUL_L = "foul_l"
        FOUL_R = "foul_r"
        GOALIE_CATCH_BALL_L = "goalie_catch_ball_l"
        GOALIE_CATCH_BALL_R = "goalie_catch_ball_r"
        TIME_UP_WITHOUT_A_TEAM = "time_up_without_a_team"
        TIME_UP = "time_up"
        HALF_TIME = "half_time"
        TIME_EXTENDED = "time_extended"
        GOAL_L = "goal_l_"
        GOAL_R = "goal_r_"
        def __init__(self):
            raise NotImplementedError("Nao crie um objeto playmode. Acesse pelo WorldModel")

    def __init__(self, action_handler):
        self.ah = action_handler
        self.sim_time = 0
        self.ball = None
        self.flags = []
        self.goals = []
        self.players = []
        self.lines = []
        self.home_point = (None, None)
        self.score_l = 0
        self.score_r = 0
        self.teamname = None
        self.side = None
        self.uniform_number = None
        self.last_message_referee = None
        self.last_message_teammate = None
        self.play_mode = WorldModel.PlayModes.BEFORE_KICK_OFF
        self.view_width = None
        self.view_quality = None
        self.stamina = None
        self.effort = None
        self.speed_amount = None
        self.speed_direction = None
        self.neck_direction = None
        self.kick_count = None
        self.dash_count = None
        self.turn_count = None
        self.say_count = None
        self.turn_neck_count = None
        self.catch_count = None
        self.move_count = None
        self.change_view_count = None
        self.abs_coords = (0, 0)
        self.abs_neck_dir = 0
        self.abs_body_dir = 0
        self.server_parameters = ServerParameters()


    def triangulate_direction(self, flags, flag_dict):
        # tenta triangular direcao absoluta baseado em flags atualmente visiveis
        abs_angles = []
        for f in self.flags:
            if f.distance is not None and f.flag_id in flag_dict:
                flag_point = flag_dict[f.flag_id]
                abs_dir = self.angle_between_points(self.abs_coords, flag_point)
                abs_angles.append(abs_dir)
        if len(abs_angles) > 0:
            return sum(abs_angles) / len(abs_angles)
        return None


    def triangulate_position(self, flags, flag_dict, angle_step=36):
        # tenta estimar posicao com algoritmo de k-means, a partir das flags visiveis
        points = []
        for f in flags:
            if f.distance is None or f.flag_id not in flag_dict:
                continue
            for i in range(0, 360, angle_step):
                dy = f.distance * math.sin(math.radians(i))
                dx = f.distance * math.cos(math.radians(i))
                fcoords = flag_dict[f.flag_id]
                new_point = (fcoords[0] + dx, fcoords[1] + dy)
                if (new_point[0] > 60 or new_point[0] < -60 or
                        new_point[1] < -40 or new_point[1] > 40):
                    continue
                points.append(new_point)
        clusters = self.cluster_points(points)
        center_with_most_points = (0, 0)
        max_points = 0
        for c in clusters:
            if len(clusters[c]) > max_points:
                center_with_most_points = c
                max_points = len(clusters[c])
        return center_with_most_points


    def cluster_points(self, points, num_cluster_iterations=15):
        # aplicacao do k-means
        centers = set([])
        for i in range(int(math.sqrt(len(points) / 2))):
            rand_center = (random.randint(-55, 55), random.randint(-35, 35))
            centers.add(rand_center)
        latest = {}
        cur = {}
        for i in range(num_cluster_iterations):
            for c in centers:
                cur[c] = []
            for p in points:
                c_dists = map(lambda c: (self.euclidean_distance(c, p), c),
                             centers)
                nearest_center = min(c_dists)[1]
                cur[nearest_center].append(p)
            new_centers = set([])
            for cluster in cur.values():
                tot_x = 0
                tot_y = 0
                if len(cluster) == 0:
                    continue
                for p in cluster:
                    tot_x += p[0]
                    tot_y += p[1]
                ave_center = (tot_x / len(cluster), tot_y / len(cluster))
                new_centers.add(ave_center)
            centers = new_centers
            latest = cur
            cur = {}
        return latest


    @staticmethod
    def euclidean_distance(point1, point2):
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


    @staticmethod
    def angle_between_points(point1, point2):
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        dx = x2 - x1
        dy = y2 - y1
        a = math.degrees(math.atan2(dy, dx))
        if a < 0:
            a = 360 + a
        return a


    def process_new_info(self, sim_time, ball, flags, goals, players, lines):
        self.sim_time = sim_time
        self.ball = ball
        self.flags = flags
        self.goals = goals
        self.players = players
        self.lines = lines
        flag_dict = game_object.Flag.FLAG_COORDS
        new_pos_cluster = self.triangulate_position(self.flags, flag_dict)
        self.abs_coords = (self.abs_coords[0]*0.5 + new_pos_cluster[0]*0.5, self.abs_coords[1]*0.5 + new_pos_cluster[1]*0.5)
        self.abs_neck_dir = self.triangulate_direction(self.flags, flag_dict)
        if self.abs_neck_dir is not None and self.neck_direction is not None:
            self.abs_body_dir = self.abs_neck_dir - self.neck_direction
        else:
            self.abs_body_dir = None


    def is_before_kick_off(self):
        return self.play_mode == WorldModel.PlayModes.BEFORE_KICK_OFF


    def is_kick_off_us(self):
        ko_left = WorldModel.PlayModes.KICK_OFF_L
        ko_right = WorldModel.PlayModes.KICK_OFF_R
        print(self.play_mode)
        return ((self.side == WorldModel.SIDE_L and self.play_mode == ko_left) or (self.side == WorldModel.SIDE_R and self.play_mode == ko_right))


    def is_dead_ball_them(self):
        #kick_in significa lateral
        #free_kick significa penalte
        #corner_kick significa escanteio
        kil = WorldModel.PlayModes.KICK_IN_L
        kir = WorldModel.PlayModes.KICK_IN_R
        fkl = WorldModel.PlayModes.FREE_KICK_L
        fkr = WorldModel.PlayModes.FREE_KICK_R
        ckl = WorldModel.PlayModes.CORNER_KICK_L
        ckr = WorldModel.PlayModes.CORNER_KICK_R
        pm = self.play_mode
        if self.side == WorldModel.SIDE_L:
            return pm in (kir, fkr, ckr)
        else:
            return pm in (kil, fkl, ckl)


    def is_ball_kickable(self):
        return (self.ball is not None and
                self.ball.distance is not None and
                self.ball.distance <= self.server_parameters.kickable_margin)


    def get_ball_speed_max(self):
        return self.server_parameters.ball_speed_max


    def kick_to(self, point, extra_power=0.0):
        if self.abs_coords is not None:
            max_kick_dist = 55.0 # maxíma distância percorrida pela bola na força maxima
            point_dist = self.euclidean_distance(self.abs_coords, point)
            dist_ratio = point_dist / max_kick_dist
            # calcula força para fazer a bola parar no ponto
            required_power = dist_ratio * self.server_parameters.maxpower
            effective_power = self.get_effective_kick_power(self.ball, required_power)
            if required_power:
                required_power += 1 - (effective_power / required_power)
                power = required_power * (1 + extra_power) # forca extra se quisermos fazer a bola passar do ponto
                ball_pos = self.get_object_absolute_coords(self.ball)
                angle_to_point = self.angle_between_points(self.abs_coords, point)
                angle = - angle_to_point
                print(self.abs_coords)
                # print(round(self.abs_body_dir, 2) , round(angle_to_point, 2))
                self.ah.kick(100, angle) # chuta


    def get_effective_kick_power(self, ball, power):
        # calcula forca efetiva de chute baseado na distancia e angulo que a bola esta
        if ball.distance is None:
            return
        kick_power = max([min([power, self.server_parameters.maxpower]), self.server_parameters.minpower])
        kick_power *= self.server_parameters.kick_power_rate
        a = 0.25 * (ball.direction / 180)
        b = 0.25 * (ball.distance / self.server_parameters.kickable_margin)
        return 1 - a - b


    def turn_neck_to_object(self, obj):
        self.ah.turn_neck(obj.direction)


    def get_distance_to_point(self, point):
        return self.euclidean_distance(self.abs_coords, point)


    def turn_body_to_point(self, point):
        abs_point_dir = self.angle_between_points(self.abs_coords, point)
        relative_dir = self.abs_body_dir - abs_point_dir
        self.ah.turn(relative_dir)


    def get_object_absolute_coords(self, obj):
        if obj.distance is None:
            return None
        dx = obj.distance * math.cos(obj.direction)
        dy = obj.distance * math.sin(obj.direction)
        return (self.abs_coords[0] + dx, self.abs_coords[1] + dy)


    def teleport_to_point(self, point):
        self.ah.move(point[0], point[1])
        # print("Teleport")


    def align_neck_with_body(self):
        if self.neck_direction is not None:
            self.ah.turn_neck(self.neck_direction * -1)


    def get_nearest_teammate_to_point(self, point):
        distances = []
        for p in self.players:
            if p.side != self.side:
                continue
            p_coords = self.get_object_absolute_coords(p)
            distances.append((self.euclidean_distance(point, p_coords), p))
        nearest = min(distances)[1]
        return nearest


    def get_stamina(self):
        return self.stamina


    def get_stamina_max(self):
        return self.server_parameters.stamina_max


    def turn_body_to_object(self, obj):
        self.ah.turn(obj.direction)

class ServerParameters:
    def __init__(self):
        #parametros padrão, sao atualizados
        self.audio_cut_dist = 50
        self.auto_mode = 0
        self.back_passes = 1
        self.ball_accel_max = 2.7
        self.ball_decay = 0.94
        self.ball_rand = 0.05
        self.ball_size = 0.085
        self.ball_speed_max = 2.7
        self.ball_stuck_area = 3
        self.ball_weight = 0.2
        self.catch_ban_cycle = 5
        self.catch_probability = 1
        self.catchable_area_l = 2
        self.catchable_area_w = 1
        self.ckick_margin = 1
        self.clang_advice_win = 1
        self.clang_define_win = 1
        self.clang_del_win = 1
        self.clang_info_win = 1
        self.clang_mess_delay = 50
        self.clang_mess_per_cycle = 1
        self.clang_meta_win = 1
        self.clang_rule_win = 1
        self.clang_win_size = 300
        self.coach = 0
        self.coach_port = 6001
        self.coach_w_referee = 0
        self.connect_wait = 300
        self.control_radius = 2
        self.dash_power_rate =0.006
        self.drop_ball_time = 200
        self.effort_dec = 0.005
        self.effort_dec_thr = 0.3
        self.effort_inc = 0.01
        self.effort_inc_thr = 0.6
        self.effort_init = 1
        self.effort_min = 0.6
        self.forbid_kick_off_offside = 1
        self.free_kick_faults = 1
        self.freeform_send_period = 20
        self.freeform_wait_period = 600
        self.fullstate_l = 0
        self.fullstate_r = 0
        self.game_log_compression = 0
        self.game_log_dated = 1
        self.game_log_dir = './'
        self.game_log_fixed = 0
        self.game_log_fixed_name = 'rcssserver'
        self.game_log_version = 3
        self.game_logging = 1
        self.game_over_wait = 100
        self.goal_width = 14.02
        self.goalie_max_moves = 2
        self.half_time = 300
        self.hear_decay = 1
        self.hear_inc = 1
        self.hear_max = 1
        self.inertia_moment = 5
        self.keepaway = 0
        self.keepaway_length = 20
        self.keepaway_log_dated = 1
        self.keepaway_log_dir = './'
        self.keepaway_log_fixed = 0
        self.keepaway_log_fixed_name = 'rcssserver'
        self.keepaway_logging = 1
        self.keepaway_start = -1
        self.keepaway_width = 20
        self.kick_off_wait = 100
        self.kick_power_rate = 0.027
        self.kick_rand = 0
        self.kick_rand_factor_l = 1
        self.kick_rand_factor_r = 1
        self.kickable_margin = 0.7
        self.landmark_file = '~/.rcssserver-landmark.xml'
        self.log_date_format = '%Y%m%d%H%M-'
        self.log_times = 0
        self.max_goal_kicks = 3
        self.maxmoment = 180
        self.maxneckang = 90
        self.maxneckmoment = 180
        self.maxpower = 100
        self.minmoment = -180
        self.minneckang = -90
        self.minneckmoment = -180
        self.minpower = -100
        self.nr_extra_halfs = 2
        self.nr_normal_halfs = 2
        self.offside_active_area_size = 2.5
        self.offside_kick_margin = 9.15
        self.olcoach_port = 6002
        self.old_coach_hear = 0
        self.pen_allow_mult_kicks = 1
        self.pen_before_setup_wait = 30
        self.pen_coach_moves_players = 1
        self.pen_dist_x = 42.5
        self.pen_max_extra_kicks = 10
        self.pen_max_goalie_dist_x = 14
        self.pen_nr_kicks = 5
        self.pen_random_winner = 0
        self.pen_ready_wait = 50
        self.pen_setup_wait = 100
        self.pen_taken_wait = 200
        self.penalty_shoot_outs = 1
        self.player_accel_max = 1
        self.player_decay = 0.4
        self.player_rand = 0.1
        self.player_size = 0.3
        self.player_speed_max = 1.2
        self.player_weight = 60
        self.point_to_ban = 5
        self.point_to_duration = 20
        self.port = 6000
        self.prand_factor_l = 1
        self.prand_factor_r = 1
        self.profile = 0
        self.proper_goal_kicks = 0
        self.quantize_step = 0.1
        self.quantize_step_l = 0.01
        self.record_messages = 0
        self.recover_dec = 0.002
        self.recover_dec_thr = 0.3
        self.recover_init = 1
        self.recover_min = 0.5
        self.recv_step = 10
        self.say_coach_cnt_max = 128
        self.say_coach_msg_size = 128
        self.say_msg_size = 10
        self.send_comms = 0
        self.send_step = 150
        self.send_vi_step = 100
        self.sense_body_step = 100
        self.simulator_step = 100
        self.slow_down_factor = 1
        self.slowness_on_top_for_left_team = 1
        self.slowness_on_top_for_right_team = 1
        self.stamina_inc_max = 45
        self.stamina_max = 4000
        self.start_goal_l = 0
        self.start_goal_r = 0
        self.stopped_ball_vel = 0.01
        self.synch_micro_sleep = 1
        self.synch_mode = 0
        self.synch_offset = 60
        self.tackle_back_dist = 0.5
        self.tackle_cycles = 10
        self.tackle_dist = 2
        self.tackle_exponent = 6
        self.tackle_power_rate = 0.027
        self.tackle_width = 1
        self.team_actuator_noise = 0
        self.text_log_compression = 0
        self.text_log_dated = 1
        self.text_log_dir = './'
        self.text_log_fixed = 0
        self.text_log_fixed_name = 'rcssserver'
        self.text_logging = 1
        self.use_offside = 1
        self.verbose = 0
        self.visible_angle = 90
        self.visible_distance = 3
        self.wind_ang = 0
        self.wind_dir = 0
        self.wind_force = 0
        self.wind_none = 0
        self.wind_rand = 0
        self.wind_random = 0