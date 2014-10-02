from Game.Effects.Conditions.Filters.Operations.operations import operations

class FixedCriteria:
    """ Represents a Criteria based on a fixed value """
    
    def __init__(self, field, value, operation):
        """ Initialize the Fixed Criteria """
        self.field = field
        self.value = value
        self.operation = operations[operation]
        
    def compare(self, card, context):
        """ Compare the card with the Matching Condition """
        value = getattr(card, self.field)
        return self.operation(value, self.value)