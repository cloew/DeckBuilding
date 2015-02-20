from character_zone import CharacterZone
from deck_zone import DeckZone
from deck_with_discard_pile_zone import DeckWithDiscardPileZone
from event_zone import EventZone
from gained_zone import GainedZone
from list_zone import ListZone
from zone import Zone
import zone_types

class ZoneFactory:
    """ Factory to construct card zones """
    
    def getZoneInContext(self, zoneType, context):
        """ Gat a Zone based on the given context """
        return self.getZone(zoneType, context.game, event=context.event, player=context.player)
    
    def getZone(self, zoneType, game, event=None, player=None):
        """ Return the zone for the given zone type and game """
        if zoneType == zone_types.CHARACTER:
            return CharacterZone(game.currentTurn.player.character)
        elif zoneType == zone_types.DECK:
            return DeckWithDiscardPileZone(player.deck, zoneType=zone_types.DECK)
        if zoneType == zone_types.DESTROYED:
            return DeckZone(game.destroyedDeck, zoneType=zone_types.DESTROYED)
        elif zoneType == zone_types.DISCARD_PILE:
            return DeckZone(player.discardPile, zoneType=zone_types.DISCARD_PILE)
        elif zoneType == zone_types.EVENT:
            return EventZone(event)
        elif zoneType == zone_types.GAINED:
            return GainedZone(game.currentTurn.gainedCards, self.getZone(zone_types.DISCARD_PILE, game, event=event, player=player))
        elif zoneType == zone_types.HAND:
            return ListZone(player.hand, zoneType=zone_types.HAND)
        elif zoneType == zone_types.KICK:
            return DeckZone(game.kickDeck, zoneType=zone_types.KICK)
        elif zoneType == zone_types.LINE_UP:
            return Zone(game.lineUp, zoneType=zone_types.LINE_UP)
        elif zoneType == zone_types.MAIN_DECK:
            return DeckZone(game.mainDeck, zoneType=zone_types.MAIN_DECK)
        elif zoneType == zone_types.ONGOING:
            return ListZone(player.ongoing, zoneType=zone_types.ONGOING)
        elif zoneType == zone_types.PLAYED:
            return ListZone(game.currentTurn.playedCards, zoneType=zone_types.PLAYED)
        elif zoneType == zone_types.SUPERVILLAIN:
            return Zone(game.superVillainStack, zoneType=zone_types.SUPERVILLAIN)
        elif zoneType == zone_types.UNDER_CHARACTER:
            return ListZone(player.underCharacter, zoneType=zone_types.UNDER_CHARACTER)
        elif zoneType == zone_types.WEAKNESS:
            return DeckZone(game.weaknessDeck, zoneType=zone_types.WEAKNESS)
        return None
        
ZoneFactory = ZoneFactory()