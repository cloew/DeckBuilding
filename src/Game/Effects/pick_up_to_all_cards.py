from Game.Effects.pick_up_to_n_cards import PickUpToNCards

class PickUpToAllCards(PickUpToNCards):
    """ Represents an effect to pick up to all the cards from a source and an optional filter """
    
    def __init__(self, sourceType, toDescription, thenEffects, criteria=None, leftoverCardEffects=[]):
        """ Initialize the options """
        PickUpToNCards.__init__(self, sourceType, 0, toDescription, thenEffects, criteria=criteria, leftoverCardEffects=leftoverCardEffects)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        possibleCardsPerSource = PickUpToNCards.findPossibleCards(self, context)
        self.setNumberOfCards(len([card for cards in possibleCardsPerSource.values() for card in cards]))
        return possibleCardsPerSource