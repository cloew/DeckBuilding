from character_source import CharacterSource
from deck_source import DeckSource
from deck_with_discard_pile_source import DeckWithDiscardPileSource
from gained_source import GainedSource
from list_source import ListSource
from source import Source

CHARACTER = "CHARACTER"
DECK = "DECK"
DESTROYED = "DESTROYED"
DISCARD_PILE = "DISCARD_PILE"
EVENT = "EVENT"
GAINED = "GAINED"
HAND = "HAND"
KICK = "KICK"
LINE_UP = "LINE_UP"
MAIN_DECK = "MAIN_DECK"
ONGOING = "ONGOING"
PLAYED = "PLAYED"

class SourceFactory:
    """ Factory to construct card sources """
    
    def getSourceForEffect(self, sourceType, args):
        """ Gat a Source based on Effect Arguments """
        return self.getSource(sourceType, args.game, event=args.event, player=args.player)
    
    def getSource(self, sourceType, game, event=None, player=None):
        """ Return the source for the given source type and game """
        if sourceType == CHARACTER:
            return CharacterSource(game.currentTurn.player.character)
        elif sourceType == DECK:
            return DeckWithDiscardPileSource(player.deck)
        if sourceType == DESTROYED:
            return DeckSource(game.destroyedDeck)
        elif sourceType == DISCARD_PILE:
            return DeckSource(player.discardPile)
        elif sourceType == EVENT:
            return Source(event)
        elif sourceType == GAINED:
            return GainedSource(game.currentTurn.gainedCards, self.getSource(DISCARD_PILE, game, event=event))
        elif sourceType == HAND:
            return ListSource(player.hand)
        elif sourceType == KICK:
            return DeckSource(game.kickDeck)
        elif sourceType == LINE_UP:
            return game.lineUp
        elif sourceType == MAIN_DECK:
            return DeckSource(game.mainDeck)
        elif sourceType == ONGOING:
            return ListSource(player.ongoing)
        elif sourceType == PLAYED:
            return ListSource(game.currentTurn.playedCards)
        return None
        
SourceFactory = SourceFactory()