
class PlayerResults:
    """ Represents player results """
    PRIORITY = 0
        
    def __cmp__(self, other):
        """ Compare this result to another result """
        priorityCmp = other.PRIORITY.__cmp__(self.PRIORITY)
        if priorityCmp == 0:
            return other.points.__cmp__(self.points)
        return priorityCmp