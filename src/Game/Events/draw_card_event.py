from game_events import DRAW

from Game.Events.card_event import CardEvent

class DrawCardEvent(CardEvent):
    """ Represents an Event for Drawing a Card """
    subject = DRAW