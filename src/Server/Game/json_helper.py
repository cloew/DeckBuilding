from card_wrapper import CardWrapper

def GetCardListJSON(cards, canBuy=False, source=None):
    """ Return the Card JSON for the given list of cards """
    return [CardWrapper(card, canBuy=canBuy, source=source).toJSON() for card in cards]