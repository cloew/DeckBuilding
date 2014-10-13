
class AlwaysTrueCondition:
    """ Represents a Game Condition that always returns true """
    
    def evaluate(self, context):
        """ Return whether the condition is true for the given game context """
        return True