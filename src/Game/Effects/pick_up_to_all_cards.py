from Game.Effects.pick_up_to_n_cards import PickUpToNCards

class PickUpToAllCards(PickUpToNCards):
    """ Represents an effect to pick up to all the cards from a zone and an optional filter """
    
    def __init__(self, zoneType, toDescription, thenEffects, criteria=None, leftoverCardEffects=[]):
        """ Initialize the options """
        PickUpToNCards.__init__(self, zoneType, 0, toDescription, thenEffects, criteria=criteria, leftoverCardEffects=leftoverCardEffects)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        possibleCardsPerZone = PickUpToNCards.findPossibleCards(self, context)
        self.setNumberOfCards(len([card for cards in possibleCardsPerZone.values() for card in cards]))
        return possibleCardsPerZone