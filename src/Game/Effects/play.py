from Game.Effects.add_to_source import AddToSource
from Game.Effects.ongoing import Ongoing
from Game.Effects.remove_played_card import RemovePlayedCard

class Play:
    """ Represents an effect to Play Cards """
    EFFECT_TYPES_TO_IGNORE = [Ongoing]
    
    def __init__(self, sourceType, returnTo=None):
        """ Initialize the Effect with the source to play from """
        self.sourceType = sourceType
        self.returnTo = returnTo
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        for card in source:
            if self.returnTo:
                source.remove(card)
            context.owner.cleanupEffects.append(RemovePlayedCard(card))
                
            coroutine = context.owner.playCard(card, effectTypesToIgnore=self.EFFECT_TYPES_TO_IGNORE)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
            if self.returnTo:
                context.owner.cleanupEffects.append(AddToSource(card, context.loadSource(self.returnTo)))