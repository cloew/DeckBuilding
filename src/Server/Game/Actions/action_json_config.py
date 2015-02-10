from kao_json import JsonAttr

def BuildActions(card, actionBuilders, gameId, playerId, includeActions):
    """ Build the actions """
    actions = []
    if includeActions:
        actions = [actionBuilder.buildFor(card, gameId, playerId) for actionBuilder in actionBuilders if actionBuilder.canBuildFor(card)]
    return actions
CardActionAttr = JsonAttr('actions', BuildActions, args=["actionBuilders", "gameId", "playerId", "includeActions"])