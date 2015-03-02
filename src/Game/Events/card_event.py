from Game.Effects.game_contexts import PlayerContext

class CardEvent:
    """ Represents an event wrapping a single card """
    subject = None # Should be sub-classed to specify what the actual subject is
    
    def __init__(self, card, context):
        """ Initialize the Played Card Event with the card that got played """
        self.card = card
        
        self.context = context.copy(event=self)
        
    def __len__(self):
        """ Return the iterator for the event when it is used as a source """
        return 1
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return [self.card].__iter__()