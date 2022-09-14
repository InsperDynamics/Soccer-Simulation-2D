from lib.rcsc.types import SideID, GameModeType


class GameMode:
    def __init__(self, game_mode: GameModeType = None):
        self._game_mode: GameModeType = game_mode
        self._mode_name: str = None
        self._side: SideID = None
        if game_mode is not None:
            self._mode_name = self._set_mode_name()
            self._side = self._set_side()

    def type(self) -> GameModeType:
        return self._game_mode

    def side(self) -> SideID:
        return self._side

    def mode_name(self) -> str:
        return self._mode_name

    def _set_side(self) -> SideID:
        if self._game_mode.value[-2:] == '_l' or self._game_mode.value[-2:] == '_r':
            return SideID(self._game_mode.value[-1])
        return SideID.NEUTRAL

    def _set_mode_name(self) -> str:
        if self._game_mode.value[-2:] == '_l' or self._game_mode.value[-2:] == '_r':
            return self._game_mode.value[:-2]
        return self._game_mode.value

    def set_game_mode(self, play_mode: GameModeType):
        self.__init__(play_mode)

    def is_teams_set_play(self, team_side: SideID):
        mode_name = self.mode_name()
        if mode_name in ("kick_off", "kick_in", "corner_kick", "goal_kick", "free_kick", "goalie_catch", "indirect_free_kick"):
            return self.side() == team_side
        elif mode_name in ("off_side", "foul_charge", "foul_push", "free_kick_fault", "back_pass", "catch_fault"):
            return self.side() != team_side
        return False

    def is_penalty_kick_mode(self):
        if self.type() in [GameModeType.PenaltySetup_Left, GameModeType.PenaltySetup_Right, GameModeType.PenaltyReady_Left, GameModeType.PenaltyReady_Right, GameModeType.PenaltyTaken_Left, GameModeType.PenaltyReady_Right, GameModeType.PenaltyMiss_Left, GameModeType.PenaltyMiss_Right, GameModeType.PenaltyScore_Left, GameModeType.PenaltyScore_Right]:
            return True
        return False
        # todo add PlayMode.PenaltyOnfield, PenaltyFoul_

    def is_our_set_play(self, our_side: SideID):
        return self.is_teams_set_play(our_side)
