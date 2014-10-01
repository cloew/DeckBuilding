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
        
    def addOngoingEffects(self, card):
        self.registerTriggers(card.triggerEffects)
        self.registerActivatable(card, card.activatableEffect)
        
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