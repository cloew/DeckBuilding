from Game.Effects.add_to_source import AddToSource
from Game.Effects.remove_played_card import RemovePlayedCard

class Play:
    """ Represents an effect to Play Cards """
    
    def __init__(self, sourceType, remove=None):
        """ Initialize the Effect with the source to play from """
        self.sourceType = sourceType
        if remove is None:
            remove = False
        self.remove = remove
        
    def perform(self, context):
        """ Perform the Game Effect """
        source = context.loadSource(self.sourceType)
        for card in source:
            if self.remove:
                source.remove(card)
            context.owner.cleanupEffects.append(RemovePlayedCard(card))
                
            coroutine = context.owner.playCard(card)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
            if self.remove:
                context.owner.cleanupEffects.append(AddToSource(card, source))