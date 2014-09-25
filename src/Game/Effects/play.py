from Game.Effects.remove_played_card import RemovePlayedCard
from Game.Sources.source_factory import SourceFactory

class Play:
    """ Represents an effect to Play Cards """
    
    def __init__(self, sourceType, remove=None):
        """ Initialize the Effect with the source to play from """
        self.sourceType = sourceType
        if remove is None:
            remove = False
        self.remove = remove
        
    def perform(self, args):
        """ Perform the Game Effect """
        source = SourceFactory.getSourceForEffect(self.sourceType, args)
        for card in source:
            if self.remove:
                source.remove(card)
                
            coroutine = args.owner.playCard(card)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
                
            args.owner.cleanupEffects.append(RemovePlayedCard(card))