from Game.Effects.effect_runner import PerformEffects

class AsOwner:
    """ Represents an effect to run as the Owner of the Current Turn """
    
    def __init__(self, thenEffects):
        """ Initialize the Effect with the children effects """
        self.thenEffects = thenEffects
        
    def perform(self, args):
        """ Perform the Game Effect """
        newArgs = args.copyForPlayer(args.owner.player)
        
        coroutine = PerformEffects(self.thenEffects, newArgs)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)