from game_events import CARD_PLAYED

class PlayedCardEvent:
    """ Represents an Event for Playing a Card """
    subjecet = CARD_PLAYED
    
    def __init__(self, card):
        """ Initialize the Played Card Event with the card that got played """
        self.card = card