from card_wrapper import CardWrapper

def GetCardListJSON(cards, game, actions=[], source=None):
    """ Return the Card JSON for the given list of cards """
    wrappers = []
    for card in cards:
        actionsForCard = list(actions)
        activatableJSON = GetActivatableActionJSON(card, game, source=source)
        if activatableJSON is not None:
            actionsForCard.append(activatableJSON)
        wrappers.append(CardWrapper(card, actions=actionsForCard))
    return [wrapper.toJSON() for wrapper in wrappers]
    
def GetActivatableActionJSON(card, game, source=None):
    """ Get the Activatable Action JSON for a particular card """
    json = None
    if card in game.currentTurn.activatableEffects:
        json = {'type':'ACTIVATE', 'source':source}
    return json