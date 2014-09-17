from Game.Effects.effect_arguments import EffectArguments

class ActivateCard:
    """ Represents a command to activate a card """
    
    def __init__(self, card, owner):
        """ Initialize the Activate Card Command """
        self.card = card
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        args = EffectArguments(self.owner.game, self.card)
        self.owner.activatableEffects[self.card].activate(args)