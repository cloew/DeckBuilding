import inspect

def PerformEffects(effects, args):
    """ Perform the given effects """
    for effect in effects:
        coroutine = PerformEffect(effect, args)
        try:
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        except StopIteration:
            pass

def PerformEffect(effect, args):
    """ Perform the given effect """
    if inspect.isgeneratorfunction(effect.perform):
        coroutine = effect.perform(args)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
    else:
        effect.perform(args)