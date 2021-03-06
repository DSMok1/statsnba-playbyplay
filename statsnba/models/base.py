from .nba import NBAGame, NBAPlayer, NBAEvent


class Backend(object):
    team = NotImplementedError
    event = NotImplementedError
    player = NotImplementedError
    game = NotImplementedError


class Event(object):
    def __init__(self, **kargs):
        self._backend = NBAEvent(**kargs)  # can further refactor

    def __eq__(self, other_player):
        return self._backend.__eq__(other_player)

    def __getattr__(self, item):
        return getattr(self._backend, item)


class Player(object):
    def __init__(self, **kargs):
        self._backend = NBAPlayer(**kargs)

    def __getattr__(self, item):
        return getattr(self._backend, item)

    def __hash__(self):
        return self._backend.__hash__()

    def __eq__(self, other):
        return self._backend.__eq__(other)
        # return self.name == other.name and self.team_abbr == other.team_abbr

    def __repr__(self):
        return '{}, {}'.format(self.name, self.team_abbr)


class Game(object):
    def __init__(self, **kargs):
            self._backend = NBAGame(game_id=kargs.pop('game_id'))

    def __getattr__(self, item):
        return getattr(self._backend, item)

    @property
    def lineups(self):
        lineups = []
        group = []
        for i, evt in enumerate(self.playbyplay[:-1]):
            group.append(evt)
            if evt.players != self.playbyplay[i+1].players:
                if len(group) > 1:
                    lineups.append(group)
                group = []
        return lineups

    def possessions(self):
        pass
