from Game.Sources.source_factory import SourceFactory

class IndicesInList:
    """ Represents a command requirement that can only be run if the indices exist in the list """
    
    def __init__(self, indices, possibilities):
        """ Initialize the requirement with the indices and list to check """
        self.indices = indices
        self.possibilities = possibilities
        
        self.chosen = None
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        cards = [game.currentTurn.request.cards[cardIndex] for cardIndex in self.indices if cardIndex < len(self.possibilities)]
        passed = len(self.indices) == len(cards)
        
        if passed:
            self.chosen = cards
        return passed