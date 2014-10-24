from Game.Effects.Conditions.Filters.Operations.operations import operations

class SourcesFilter:
    """ Represents a filter that returns all the cards from a source """
    
    def __init__(self, sourceTypes):
        """ Initialize the filter """
        self.sourceTypes = sourceTypes
        
    def evaluate(self, context):
        """ Evaluate the condition """
        return [card for sourceType in self.sourceTypes for card in context.loadSource(sourceType)]