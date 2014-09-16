from card_wrapper import CardWrapper

def GetCardListJSON(cards, actions=[]):
    """ Return the Card JSON for the given list of cards """
    return [CardWrapper(card, actions=actions).toJSON() for card in cards]