from game_events import DEFEND

from Game.Events.card_event import CardEvent

class DefendEvent(CardEvent):
    """ Represents an Event for Defending an attack """
    subject = DEFEND