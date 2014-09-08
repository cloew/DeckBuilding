
class SourceFactory:
    """ Factory to construct card sources """
    
    def getSource(self, sourceType, game, event=None):
        """ Return the source for the given source tyoe and game """
        if sourceType == "EVENT":
            return event
        elif sourceType == "LINE_UP":
            return game.lineUp
        elif sourceType == "PLAYED":
            return game.currentTurn.playedCards
        return None
        
SourceFactory = SourceFactory()