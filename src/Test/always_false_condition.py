
class AlwaysFalseCondition:
    """ Represents a Game Condition that always returns false """
    
    def evaluate(self, context):
        """ Return whether the condition is true for the given game context """
        return False