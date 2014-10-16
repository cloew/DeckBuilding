def GetPlayersStartingWith(player, players):
    """ Get the players in order starting with the given player """
    foes = [player]
    for i in range(len(players)-1):
        player = GetNextPlayer(player, players)
        foes.append(player)
    return foes

def GetNextPlayer(player, players):
    """ Get the player next to the given player """
    index = players.index(player)
    index = (index + 1) % len(players)
    return players[index]