from game_events import CARD_PLAYED

from Game.Effects.effect_arguments import EffectArguments

class PlayedCardEvent:
    """ Represents an Event for Playing a Card """
    subject = CARD_PLAYED
    
    def __init__(self, card, game):
        """ Initialize the Played Card Event with the card that got played """
        self.card = card
        self.game = game
        
        self.args = EffectArguments(game, card, event=self)
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return [self.card].__iter__()