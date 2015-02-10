
def Incrementer(startAt=0):
    """ Return the next value by incrementing from the start at value """
    value = startAt
    while True:
        yield value
        value += 1