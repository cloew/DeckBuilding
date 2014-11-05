from Game.Events.game_event_listener import GameEventListener

class OngoingEffects:
    """ Represents the Triggers and Activatable Effects for the turn """
    
    def __init__(self):
        """ Initialize the Watching Effects """
        self.activatableEffects = {}
        self.eventListener = GameEventListener()
        self.send = self.eventListener.send
        
    def addStartingEffects(self, game):
        """ Add the Starting Effects for the Turn """
        game.currentTurn.player.addStartingEffects(self.addOngoingEffects)
        
    def addOutOfTurnEffects(self, game):
        """ Add the Starting Effects for the Turn """
        game.currentTurn.player.addOutOfTurnEffects(self.registerOutOfTurnEffects)
        
    def addOngoingEffects(self, card):
        self.registerTriggers(card.triggerEffects)
        self.registerActivatable(card, card.activatableEffect)
        
    def registerOutOfTurnEffects(self, card):
        self.registerTriggers(card.outOfTurnTriggerEffects)
        
    def registerTrigger(self, trigger):
        """ Register the given trigger """
        self.registerTriggers([trigger])
        
    def registerTriggers(self, triggers):
        """ Register the given triggers """
        self.eventListener.registerTriggers(triggers)
        
    def unregisterTrigger(self, trigger):
        """ Unregister the given trigger """
        self.eventListener.unregisterTriggers([trigger])
        
    def unregisterTriggers(self, triggers):
        """ Unregister the given trigger """
        self.eventListener.unregisterTriggers(triggers)
        
    def registerActivatable(self, card, activatable):
        """ Register the given activatable """
        if activatable is not None:
            if card not in self.activatableEffects:
                self.activatableEffects[card] = []
            self.activatableEffects[card].append(activatable)
        
    def unregisterActivatable(self, card, activatable):
        """ Unregister the given card's activatable effect """
        self.activatableEffects[card].remove(activatable)
        if len(self.activatableEffects[card]) == 0:
            del self.activatableEffects[card]