from character_source import CharacterSource
from deck_source import DeckSource
from deck_with_discard_pile_source import DeckWithDiscardPileSource
from event_source import EventSource
from gained_source import GainedSource
from list_source import ListSource
from source import Source
import source_types

class SourceFactory:
    """ Factory to construct card sources """
    
    def getSourceInContext(self, sourceType, context):
        """ Gat a Source based on the given context """
        return self.getSource(sourceType, context.game, event=context.event, player=context.player)
    
    def getSource(self, sourceType, game, event=None, player=None):
        """ Return the source for the given source type and game """
        if sourceType == source_types.CHARACTER:
            return CharacterSource(game.currentTurn.player.character)
        elif sourceType == source_types.DECK:
            return DeckWithDiscardPileSource(player.deck, sourceType=source_types.DECK)
        if sourceType == source_types.DESTROYED:
            return DeckSource(game.destroyedDeck, sourceType=source_types.DESTROYED)
        elif sourceType == source_types.DISCARD_PILE:
            return DeckSource(player.discardPile, sourceType=source_types.DISCARD_PILE)
        elif sourceType == source_types.EVENT:
            return EventSource(event)
        elif sourceType == source_types.GAINED:
            return GainedSource(game.currentTurn.gainedCards, self.getSource(source_types.DISCARD_PILE, game, event=event, player=player))
        elif sourceType == source_types.HAND:
            return ListSource(player.hand, sourceType=source_types.HAND)
        elif sourceType == source_types.KICK:
            return DeckSource(game.kickDeck, sourceType=source_types.KICK)
        elif sourceType == source_types.LINE_UP:
            return Source(game.lineUp)
        elif sourceType == source_types.MAIN_DECK:
            return DeckSource(game.mainDeck, sourceType=source_types.MAIN_DECK)
        elif sourceType == source_types.ONGOING:
            return ListSource(player.ongoing, sourceType=source_types.ONGOING)
        elif sourceType == source_types.PLAYED:
            return ListSource(game.currentTurn.playedCards, sourceType=source_types.PLAYED)
        elif sourceType == source_types.SUPERVILLAIN:
            return Source(game.superVillainStack, sourceType=source_types.SUPERVILLAIN)
        elif sourceType == source_types.UNDER_CHARACTER:
            return ListSource(player.underCharacter, sourceType=source_types.UNDER_CHARACTER)
        elif sourceType == source_types.WEAKNESS:
            return DeckSource(game.weaknessDeck, sourceType=source_types.WEAKNESS)
        return None
        
SourceFactory = SourceFactory()