from card_wrapper import CardWrapper

def GetCardListJSON(cards, game, includeActions=False, actions=[], zone=None, canBuyCallback=None):
    """ Return the Card JSON for the given list of cards """
    wrappers = []
    for card in cards:
        actionsForCard = []
        if canBuyCallback is None or canBuyCallback(card):
            actionsForCard = list(actions)
        
        activatableJSON = GetActivatableActionJSON(card, game, zone=zone)
        if activatableJSON is not None:
            actionsForCard.append(activatableJSON)
        wrappers.append(CardWrapper(card, actions=GetActions(actionsForCard, includeActions=includeActions)))
    return [wrapper.toJSON() for wrapper in wrappers]
    
def GetActivatableActionJSON(card, game, zone=None):
    """ Get the Activatable Action JSON for a particular card """
    json = None
    if card in game.currentTurn.activatableEffects:
        activatableEffect = game.currentTurn.activatableEffects[card][0]
        if activatableEffect.canActivate(game):
            json = {'type':'ACTIVATE', 'zone':zone}
    return json
    
def GetActions(actions, includeActions=False):
    """ Return the actions if possible """
    if not includeActions:
        return []
    else:
        return actions