def estrategiaAtaque(self, WorldModel):
    # determine the enemy goal position
    goal_pos = None
    if self.wm.side == WorldModel.SIDE_R:
        goal_pos = (-55, 0)
    else:
        goal_pos = (55, 0)


    # kick off!
    if self.wm.is_before_kick_off():
        # player 9 takes the kick off
        if self.wm.uniform_number == 9:
            if self.wm.is_ball_kickable():
                # kick with 100% extra effort at enemy goal
                self.wm.kick_to(goal_pos, 1.0)
            else:
                # move towards ball
                if self.wm.ball is not None:
                    if (self.wm.ball.direction is not None and
                            -7 <= self.wm.ball.direction <= 7):
                        self.wm.ah.dash(50)
                    else:
                        self.wm.turn_body_to_point((0, 0))

            # turn to ball if we can see it, else face the enemy goal
            if self.wm.ball is not None:
                self.wm.turn_neck_to_object(self.wm.ball)

            return

    # attack!
    else:
        # find the ball
        if self.wm.ball is None or self.wm.ball.direction is None:
            self.wm.ah.turn(30)
            return

        # kick it at the enemy goal
        if self.wm.is_ball_kickable():
            self.wm.kick_to(goal_pos, 1.0)
            return
        else:
            # move towards ball
            if -7 <= self.wm.ball.direction <= 7:
                self.wm.ah.dash(65)
            else:
                # face ball
                self.wm.ah.turn(self.wm.ball.direction/2)
            return