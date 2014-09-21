from Game.Effects.effect_runner import PerformEffect

import copy

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effect):
        """ Initialize the Effect with the effect to attack with """
        self.effect = effect
        
    def perform(self, args):
        """ Perform the Game Effect """
        foes = args.foes
        for foe in args.foes:
            args = copy.copy(args)
            args.player = foe
            
            coroutine = PerformEffect(self.effect, args)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass