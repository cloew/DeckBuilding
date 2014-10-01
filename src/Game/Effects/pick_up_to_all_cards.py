from Game.Effects.pick_up_to_n_cards import PickUpToNCards

class PickUpToAllCards(PickUpToNCards):
    """ Represents an effect to pick up to all the cards from a source and an optional filter """
    
    def __init__(self, sourceType, thenEffects, filter=None):
        """ Initialize the options """
        PickUpToNCards.__init__(self, sourceType, 0, thenEffects, filter=filter)
                
    def findPossibleCards(self, args):
        """ Return the possible cards """
        source, possibleCards = PickUpToNCards.findPossibleCards(self, args)
        self.setNumberOfCards(len(possibleCards))
        return source, possibleCards
        