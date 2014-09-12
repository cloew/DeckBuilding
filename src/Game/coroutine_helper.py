
def RunCoroutine(coroutine):
    """ Runs the given coroutine til it is complete """
    try:
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
    except StopIteration:
        pass