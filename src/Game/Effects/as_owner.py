from Game.Effects.effect_runner import PerformEffects

class AsOwner:
    """ Represents an effect to run as the Owner of the Current Turn """
    
    def __init__(self, thenEffects):
        """ Initialize the Effect with the children effects """
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        newContext = context.getPlayerContext(context.owner.player)
        
        coroutine = PerformEffects(self.thenEffects, newContext)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)