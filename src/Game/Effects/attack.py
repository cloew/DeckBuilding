from Game.Commands.Requests.defend_request import DefendRequest

class Attack:
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effect):
        """ Initialize with the effect to attack with """
        self.effects = [effect]
        
    def perform(self, args):
        """ Perform the Game Effect """
        targets = []
        for foe in foes:
            defended = yield DefendRequest(args.parent, args)
            if not defended:
                targets.append(foe)
            else:
                pass # Perform the Defend Effects
                
        coroutine = PerformEffectsForEachPlayer(self.effects, targets, args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)