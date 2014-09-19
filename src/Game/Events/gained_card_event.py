from game_events import CARD_GAINED

from Game.Events.card_event import CardEvent

class GainedCardEvent(CardEvent):
    """ Represents an Event for Gaining a Card """
    subject = CARD_GAINED