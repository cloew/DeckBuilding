from game_events import CARD_PLAYED

from Game.Events.card_event import CardEvent

class PlayedCardEvent(CardEvent):
    """ Represents an Event for Playing a Card """
    subject = CARD_PLAYED