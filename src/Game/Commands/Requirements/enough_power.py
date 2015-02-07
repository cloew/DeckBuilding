
class EnoughPower:
    """ Represents a command requirement that passes if their is enough power to buy the given card """
    
    def __init__(self, card):
        """ Initialize the Enough Power Requirement with the card to compare against """
        self.card = card
    
    def passed(self, player, game):
        """ Return if the requirement passes """
        return self.card.cost <= game.currentTurn.power