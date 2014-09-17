from deck_source import DeckSource
from deck_with_discard_pile_source import DeckWithDiscardPileSource
from list_source import ListSource
from source import Source

DECK = "DECK"
DESTROYED = "DESTROYED"
DISCARD_PILE = "DISCARD_PILE"
EVENT = "EVENT"
HAND = "HAND"
KICK = "KICK"
LINE_UP = "LINE_UP"
MAIN_DECK = "MAIN_DECK"
ONGOING = "ONGOING"
PLAYED = "PLAYED"

class SourceFactory:
    """ Factory to construct card sources """
    
    def getSource(self, sourceType, game, event=None):
        """ Return the source for the given source tyoe and game """
        if sourceType == DECK:
            return DeckWithDiscardPileSource(game.currentTurn.player.deck)
        if sourceType == DESTROYED:
            return DeckSource(game.destroyedDeck)
        elif sourceType == DISCARD_PILE:
            return DeckSource(game.currentTurn.player.discardPile)
        elif sourceType == EVENT:
            return Source(event)
        elif sourceType == HAND:
            return ListSource(game.currentTurn.player.hand)
        elif sourceType == KICK:
            return DeckSource(game.kickDeck)
        elif sourceType == LINE_UP:
            return game.lineUp
        elif sourceType == MAIN_DECK:
            return DeckSource(game.mainDeck)
        elif sourceType == ONGOING:
            return ListSource(game.currentTurn.player.ongoing)
        elif sourceType == PLAYED:
            return ListSource(game.currentTurn.playedCards)
        return None
        
SourceFactory = SourceFactory()