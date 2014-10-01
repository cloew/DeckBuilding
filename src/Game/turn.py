from power_tracker import PowerTracker
from ongoing_effects import OngoingEffects

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
        self.powerTracker = PowerTracker()
        self.gainPower = self.powerTracker.gainPower
        self.spendPower = self.powerTracker.spendPower
        self.changeModifier = self.powerTracker.changeModifier
        
        self.ongoingEffects = OngoingEffects()
        self.registerTrigger = self.ongoingEffects.registerTrigger
        self.unregisterTrigger = self.ongoingEffects.unregisterTrigger
        self.registerActivatable = self.ongoingEffects.registerActivatable
        self.unregisterActivatable = self.ongoingEffects.unregisterActivatable
        self.addOngoingEffects = self.ongoingEffects.addOngoingEffects
        
        self.playedCards = []
        self.gainedCards = []
        self.cleanupEffects = []

        self.command = None
        self.request = None
            
    def start(self):
        """ Start the Turn """
        coroutine = self.game.superVillainStack.performFirstAppearanceEffects(self.game)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        self.ongoingEffects.addStartingEffects(self.game)
            
        coroutine = self.ongoingEffects.send(StartOfTurnEvent(self.game))
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
        
    def playCardFromHand(self, card):
        """ Play the provided card """
        self.player.hand.remove(card)
        coroutine = self.playCard(card)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
        
    def playCard(self, card):
        """ Play card """
        coroutine = card.play(self.game)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
        
        coroutine = self.ongoingEffects.send(PlayedCardEvent(card, self.game))
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
        
    def gainCard(self, card, fromSource, toSource=None):
        """ Gain the provided card """
        coroutine = self.player.gainCard(card, fromSource, toSource=toSource, game=self.game)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
            
        coroutine = self.ongoingEffects.send(GainedCardEvent(card, self.game))
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass
            
        self.gainedCards.append(card)
        
    def cleanup(self):
        """ Cleanup the turn """
        args = EffectArguments(self.game, None)
        for effect in self.cleanupEffects:
            effect.perform(args)
        
        self.player.deck.discardAll(self.playedCards)
        self.player.deck.discardAll(self.player.hand)
        self.player.drawHand()
       
    @property
    def power(self):
        """ Return the current power level for the turn """
        return self.powerTracker.power
       
    @property
    def modifier(self):
        """ Return the current power modifier for the turn """
        return self.powerTracker.modifier
        
    @property
    def activatableEffects(self):
        """ Return the current activatable effects for the turn """
        return self.ongoingEffects.activatableEffects
        
    def __repr__(self):
        """ Return the String Representation of the Turn """
        return "<Turn: Power:{0}|Played:{1}>".format(self.power, self.playedCards)