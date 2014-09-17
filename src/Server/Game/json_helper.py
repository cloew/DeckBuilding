from card_wrapper import CardWrapper

def GetCardListJSON(cards, game, actions=[], source=None):
    """ Return the Card JSON for the given list of cards """
    wrappers = []
    for card in cards:
        actionsForCard = list(actions)
        if card in game.currentTurn.activatableEffects:
            actionsForCard.append({'type':'ACTIVATE', 'source':source})
        wrappers.append(CardWrapper(card, actions=actionsForCard))
    return [wrapper.toJSON() for wrapper in wrappers]