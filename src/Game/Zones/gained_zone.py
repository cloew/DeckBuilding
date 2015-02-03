from list_zone import ListZone
from zone_types import GAINED

class GainedZone(ListZone):
    """ Represents the List of Gained Cards as a zone """
    
    def __init__(self, cards, discardPileZone):
        """ Initialize the Zone so that you can only interact 
            with Gained Cards that are in your discard pile """
        self.discardPileZone = discardPileZone
        discardPileSet = set(discardPileZone)
        ListZone.__init__(self, [card for card in cards if card in discardPileSet], zoneType=GAINED)
        
    def remove(self, card):
        """ Remove the given card """
        self.discardPileZone.remove(card)
        ListZone.remove(self, card)