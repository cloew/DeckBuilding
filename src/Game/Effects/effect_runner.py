import inspect

def PerformEffectsForEachPlayer(effects, players, context, failedEffects=[]):
    """ Perform the given effects """
    for player in players:
        context = context.getPlayerContext(player)
        
        coroutine = PerformEffects(effects, context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            failedEffects.append(context.failed)
            pass

def PerformEffects(effects, context, effectTypesToIgnore=[]):
    """ Perform the given effects """
    effectsToPerform = [effect for effect in effects if effect.__class__ not in effectTypesToIgnore]
    for effect in effectsToPerform:
        coroutine = PerformEffect(effect, context)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass

def PerformEffect(effect, context):
    """ Perform the given effect """
    if inspect.isgeneratorfunction(effect.perform):
        coroutine = effect.perform(context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
    else:
        effect.perform(context)