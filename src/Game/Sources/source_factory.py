from deck_source import DeckSource
from list_source import ListSource

DISCARD_PILE = "DISCARD_PILE"
EVENT = "EVENT"
HAND = "HAND"
KICK = "KICK"
LINE_UP = "LINE_UP"
MAIN_DECK = "MAIN_DECK"
PLAYED = "PLAYED"

class SourceFactory:
    """ Factory to construct card sources """
    
    def getSource(self, sourceType, game, event=None):
        """ Return the source for the given source tyoe and game """
        if sourceType == DISCARD_PILE:
            return DeckSource(game.currentTurn.player.discardPile)
        elif sourceType == EVENT:
            return event
        elif sourceType == HAND:
            return ListSource(game.currentTurn.player.hand)
        elif sourceType == KICK:
            return DeckSource(game.kickDeck)
        elif sourceType == LINE_UP:
            return game.lineUp
        elif sourceType == MAIN_DECK:
            return DeckSource(game.mainDeck)
        elif sourceType == PLAYED:
            return ListSource(game.currentTurn.playedCards)
        return None
        
SourceFactory = SourceFactory()