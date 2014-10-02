from Game.Effects.effect_runner import PerformEffects

class AsNextPlayer:
    """ Represents an effect to run as the Next Player """
    
    def __init__(self, thenEffects):
        """ Initialize the Effect with the children effects """
        self.thenEffects = thenEffects
        
    def perform(self, args):
        """ Perform the Game Effect """
        newArgs = args.copyForPlayer(args.nextPlayer)
        
        coroutine = PerformEffects(self.thenEffects, newArgs)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)