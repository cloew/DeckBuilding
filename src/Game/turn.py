
class Turn:
    """ Represents a turn in the game """
    
    def __init__(self, player):
        """ Initialize the Turn """
        self.player = player
        self.power = 0
        self.playedCards = []
        self.cleanupEffects = []
        
    def playCard(self, card):
        """ Play the provided card """
        self.player.hand.remove(card)
        card.play(self)
        self.playedCards.append(card)
        
    def addOngoing(self, card):
        """ Add the given card as an ongoing effect """
        self.player.addOngoing(card)
        
    def draw(self, count=1):
        """ Draw the given number of cards """
        self.player.draw(count=count)
        
    def gainCard(self, card):
        """ Gain the provided card """
        self.player.gainCard(card)
        
    def gainPower(self, power):
        """ Gain the proper amount of power """
        self.power += power
        
    def spendPower(self, power):
        """ Spend the provided amount of power """
        self.power -= power
        
    def cleanup(self):
        """ Cleanup the turn """
        for effect in self.cleanupEffects:
            effect.perform(self)
        
        self.player.deck.discardAll(self.playedCards)
        self.player.deck.discardAll(self.player.hand)
        self.player.drawHand()
        
    def __repr__(self):
        """ Return the String Representation of the Turn """
        return "<Turn: Power:{0}|Played:{1}>".format(self.power, self.playedCards)