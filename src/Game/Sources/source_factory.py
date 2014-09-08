
class SourceFactory:
    """ Factory to construct card sources """
    
    def getSource(self, sourceType, game, event=None):
        """ Return the source for the given source tyoe and game """
        if sourceType == "PLAYED":
            return game.currentTurn.playedCards
        elif sourceType == "EVENT":
            return event
        return None
        
SourceFactory = SourceFactory()