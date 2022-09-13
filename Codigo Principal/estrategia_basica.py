def estrategiaBasica(self, WorldModel):
    # take places on the field by uniform number
    if not self.in_kick_off_formation:
        
        # used to flip x coords for other side
        side_mod = -1 if self.wm.side == WorldModel.SIDE_R else 1

        if self.wm.uniform_number == 1:
            self.wm.teleport_to_point((-5 * side_mod, 30))
        elif self.wm.uniform_number == 2:
            self.wm.teleport_to_point((-40 * side_mod, 15))
        elif self.wm.uniform_number == 3:
            self.wm.teleport_to_point((-40 * side_mod, 00))
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
            self.wm.teleport_to_point((-10 * side_mod, 0))
        elif self.wm.uniform_number == 10:
            self.wm.teleport_to_point((-10 * side_mod, 20))
        elif self.wm.uniform_number == 11:
            self.wm.teleport_to_point((-10 * side_mod, -20))

        self.in_kick_off_formation = True

        return