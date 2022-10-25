def formacaoKickoff(self, WorldModel):
    #print(self.wm.play_mode)
    # if not self.in_kick_off_formation:
    if self.wm.play_mode in [WorldModel.PlayModes.BEFORE_KICK_OFF,
                            WorldModel.PlayModes.KICK_OFF_R,
                            WorldModel.PlayModes.KICK_OFF_L,]:
        print("Teleport")
        side_mod = -1 if self.wm.side == WorldModel.SIDE_R else 1
        if self.wm.uniform_number == 1:
            self.wm.teleport_to_point((-50 * side_mod, 0))
        elif self.wm.uniform_number == 2:
            self.wm.teleport_to_point((-40 * side_mod, 15))
        elif self.wm.uniform_number == 3:
            self.wm.teleport_to_point((-40 * side_mod, 0))
        elif self.wm.uniform_number == 4:
            self.wm.teleport_to_point((-40 * side_mod, -15))
        elif self.wm.uniform_number == 5:
            self.wm.teleport_to_point((-5 * side_mod, -30))
        elif self.wm.uniform_number == 6:
            self.wm.teleport_to_point((-20 * side_mod, 20))
        elif self.wm.uniform_number == 7:
            self.wm.teleport_to_point((-20 * side_mod, 0))
        elif self.wm.uniform_number == 8:
            self.wm.teleport_to_point((-20 * side_mod, -20))
        elif self.wm.uniform_number == 9:
            self.wm.teleport_to_point((-10 * side_mod, 10))
        elif self.wm.uniform_number == 10:
            self.wm.teleport_to_point((-5 * side_mod, 30))
        elif self.wm.uniform_number == 11:
            self.wm.teleport_to_point((-10 * side_mod, -10))
        # self.in_kick_off_formation = True
        return

def ataqueBasico(self, WorldModel):
    # L_GAME_MODES = [
    #     WorldModel.KICK_OFF_L,
    #     WorldModel.KICK_IN_L,
    #     WorldModel.FREE_KICK_L,
    #     WorldModel.CORNER_KICK_L,
    #     WorldModel.GOAL_KICK_L,
    #     WorldModel.OFFSIDE_L,
    # ]
    # L_GAME_MODES = [
    #     WorldModel.KICK_OFF_R,
    #     WorldModel.KICK_IN_R,
    #     WorldModel.FREE_KICK_R,
    #     WorldModel.CORNER_KICK_R,
    #     WorldModel.GOAL_KICK_R,
    #     WorldModel.OFFSIDE_R,
    # ]
    # determine the enemy goal position
    goal_pos = (52.5, 0) if self.wm.side == WorldModel.SIDE_L else (-52.5, 0)
    # kick off!
    if self.wm.is_before_kick_off():
        return
    else:
        # find the ball
        if self.wm.ball is None or self.wm.ball.direction is None:
            self.wm.ah.turn(30)
            return
        self.wm.align_neck_with_body()            

        # catch ball
        # if self.wm.is_ball_kickable():
        #     # kick it at the enemy goal
        #     self.wm.chute_fraco(goal_pos)
        #     return
        if self.wm.is_ball_kickable():
            ball_pos = self.wm.get_object_absolute_coords(self.wm.ball)
            self.wm.turn_body_to_point(ball_pos)
            self.wm.kick_to(goal_pos)
            return

        else:
            self.wm.catch = False
            # move towards ball
            if -7 <= self.wm.ball.direction <= 7:
                self.wm.turn_neck_to_object(self.wm.ball)
                self.wm.ah.dash(65)
            else:
                # face ball
                self.wm.ah.turn(self.wm.ball.direction/2)
            return