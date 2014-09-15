from card_wrapper import CardWrapper

def GetCardListJSON(cards):
    """ Return the Card JSON for the given list of cards """
    return [CardWrapper(card).toJSON() for card in cards]