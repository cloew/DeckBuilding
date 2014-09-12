import inspect

def RunCoroutineOrFunction(function):
    """ Runs the given function as a coroutine or as a standard function """
    if inspect.isgeneratorfunction(function):
        coroutine = function()
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
    else:
        function()