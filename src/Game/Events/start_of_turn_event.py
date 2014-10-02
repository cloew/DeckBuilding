from game_events import START_OF_TURN

from Game.Effects.game_contexts import PlayerContext

class StartOfTurnEvent:
    """ Represnts the event for the Start of a Turn """
    subject = START_OF_TURN
    
    def __init__(self, game):
        """ Initialize the Start of Turn Event """
        self.context = PlayerContext(game, None, event=self)
    
    def __len__(self):
        """ Return the iterator for the event when it is used as a source """
        return 0
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return [].__iter__()