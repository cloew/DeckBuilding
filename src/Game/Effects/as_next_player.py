from Game.Effects.effect_runner import PerformEffects

class AsNextPlayer:
    """ Represents an effect to run as the Next Player """
    
    def __init__(self, thenEffects):
        """ Initialize the Effect with the children effects """
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        newContext = context.getPlayerContext(context.nextPlayer)
        
        coroutine = PerformEffects(self.thenEffects, newContext)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)