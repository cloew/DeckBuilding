
class RequestTarget:
    """ Represents a command requirement that passes when the request is for the player """
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        return game.currentTurn.request is not None and player in game.currentTurn.request.players