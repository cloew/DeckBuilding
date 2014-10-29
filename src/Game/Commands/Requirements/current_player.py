
class CurrentPlayer:
    """ Represents a command requirement that the command can only be run as the current player """
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        return player is game.currentTurn.player