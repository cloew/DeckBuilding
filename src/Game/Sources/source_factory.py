
class SourceFactory:
    """ Factory to construct card sources """
    
    def getSource(self, sourceType, game):
        """ Return the source for the given source tyoe and game """
        if sourceType == "PLAYED":
            return game.currentTurn.playedCards
        return None
        
SourceFactory = SourceFactory()