
class NoRequest:
    """ Represents a command requirement that passes when there is no request """
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        return game.currentTurn.request is None