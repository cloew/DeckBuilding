from Game.Effects.effect_arguments import EffectArguments
from Game.Events.gained_card_event import GainedCardEvent
from Game.Events.played_card_event import PlayedCardEvent
from Game.Events.start_of_turn_event import StartOfTurnEvent
from Game.Events.game_event_listener import GameEventListener

from coroutine_helper import RunCoroutineOrFunction

class Turn:
    """ Represents a turn in the game """
    
    def __init__(self, player, game):
        """ Initialize the Turn """
        self.player = player
        self.game = game
        self.power = 0
        
        self.playedCards = []
        self.gainedCards = []
        
        self.activatableEffects = {}
        self.cleanupEffects = []

        self.command = None
        self.request = None
        
        self.setupEventListener()
        
    def setupEventListener(self):
        """ Setup the Event Listener """
        self.eventListener = GameEventListener()
        self.addStartingEffects()
        
    def addStartingEffects(self):
        for card in self.player.ongoing + [self.player.character]:
            self.addOngoingEffects(card)
            
    def start(self):
        """ Start the Turn """
        coroutine = self.eventListener.send(StartOfTurnEvent(self.game))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def perform(self, command):
        """ Perform the given command """
        coroutine = RunCoroutineOrFunction(command.perform)
        try:
            request = coroutine.next()
            self.command = coroutine
            self.request = request
        except StopIteration:
            self.command = None
            self.request = None
            
    def continueCommand(self, response):
        """ Continue the Command """
        coroutine = self.command
        try:
            request = self.command.send(response)
            self.command = coroutine
            self.request = request
        except StopIteration:
            self.command = None
            self.request = None
        
    def playCard(self, card):
        """ Play the provided card """
        self.player.hand.remove(card)
        coroutine = card.play(self.game)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        coroutine = self.eventListener.send(PlayedCardEvent(card, self.game))
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        self.playedCards.append(card)
        
    def addOngoing(self, card):
        """ Add the given card as an ongoing effect """
        self.player.addOngoing(card)
        self.addOngoingEffects(card)
        
    def addOngoingEffects(self, card):
        self.registerTriggers(card.triggerEffects)
        self.registerActivatable(card, card.activatableEffect)
        
    def draw(self, count=1):
        """ Draw the given number of cards """
        self.player.draw(count=count)
        
    def gainCard(self, card, fromSource, toSource=None):
        """ Gain the provided card """
        self.player.gainCard(card, fromSource, toSource=toSource)
        coroutine = self.eventListener.send(GainedCardEvent(card, self.game))
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        self.gainedCards.append(card)
        
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
        
    def registerActivatable(self, card, activatable):
        """ Register the given activatable """
        if activatable is not None:
            self.activatableEffects[card] = activatable
        
    def unregisterActivatable(self, card):
        """ Unregister the given card's activatable effect """
        del self.activatableEffects[card]
        
    def cleanup(self):
        """ Cleanup the turn """
        args = EffectArguments(self.game, None)
        for effect in self.cleanupEffects:
            effect.perform(args)
        
        self.player.deck.discardAll(self.playedCards)
        self.player.deck.discardAll(self.player.hand)
        self.player.drawHand()
        
    def __repr__(self):
        """ Return the String Representation of the Turn """
        return "<Turn: Power:{0}|Played:{1}>".format(self.power, self.playedCards)