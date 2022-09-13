def estrategiaAtaque(self, WorldModel):
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
    goal_pos = (55, 0) if self.wm.side == WorldModel.SIDE_L else (-55, 0)
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
        
        