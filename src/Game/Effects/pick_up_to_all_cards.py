from Game.Effects.pick_up_to_n_cards import PickUpToNCards

class PickUpToAllCards(PickUpToNCards):
    """ Represents an effect to pick up to all the cards from a source and an optional filter """
    
    def __init__(self, sourceType, thenEffects, criteria=None):
        """ Initialize the options """
        PickUpToNCards.__init__(self, sourceType, 0, thenEffects, criteria=criteria)
                
    def findPossibleCards(self, context):
        """ Return the possible cards """
        possibleCards = PickUpToNCards.findPossibleCards(self, context)
        self.setNumberOfCards(len(possibleCards))
        return possibleCards
        