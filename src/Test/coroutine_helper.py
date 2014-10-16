
def RunCoroutine(coroutine):
    """ Run the given coroutine """
    try:
        coroutine.next()
    except StopIteration:
        pass