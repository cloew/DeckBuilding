from Game.Events.played_card_event import PlayedCardEvent
from Game.Events.game_event_listener import GameEventListener

class Turn:
    """ Represents a turn in the game """
    
    def __init__(self, player, game):
        """ Initialize the Turn """
        self.player = player
        self.game = game
        self.power = 0
        self.playedCards = []
        self.cleanupEffects = []
        
        self.setupEventListener()
        
    def setupEventListener(self):
        """ Setup the Event Listener """
        self.eventListener = GameEventListener()
        for card in self.player.ongoing:
            self.registerTriggers(card.triggerEffects)
        
    def playCard(self, card):
        """ Play the provided card """
        self.player.hand.remove(card)
        card.play(self.game)
        self.eventListener.send(PlayedCardEvent(card, self.game))
        self.playedCards.append(card)
        
    def addOngoing(self, card):
        """ Add the given card as an ongoing effect """
        self.player.addOngoing(card)
        self.registerTriggers(card.triggerEffects)
        
    def draw(self, count=1):
        """ Draw the given number of cards """
        self.player.draw(count=count)
        
    def gainCard(self, card, fromSource, destinationSource=None):
        """ Gain the provided card """
        self.player.gainCard(card, fromSource, destinationSource=destinationSource)
        
    def gainPower(self, power):
        """ Gain the proper amount of power """
        self.power += power
        
    def spendPower(self, power):
        """ Spend the provided amount of power """
        self.power -= power
        
    def registerTrigger(self, trigger):
        """ Register the given trigger """
        self.registerTriggers([trigger])
        
    def registerTriggers(self, triggers):
        """ Register the given triggers """
        self.eventListener.registerTriggers(triggers)
        
    def unregisterTrigger(self, trigger):
        """ Unregister the given trigger """
        self.eventListener.unregisterTriggers([trigger])
        
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