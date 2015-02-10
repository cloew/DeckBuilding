from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from Game.Effects.game_contexts import PlayerContext
from Game.Results.game_results import GameResults
from Game.Results.player_results import PlayerResults

from itertools import groupby
    
def GetCards(playerResults, game):
    """ Return the cards """
    context = PlayerContext(game, None, player=playerResults.player)
    
    cards = {}
    cardsByType = {str(cardType):list(cardsForType) for cardType, cardsForType in groupby(sorted(playerResults.player.deck, key=lambda card: card.cardType), key=lambda card: card.cardType)}
    
    cardTypes = []
    for cardType in sorted(cardsByType.keys()):
        cardTypes.append(cardType)
        cardsForType = cardsByType[cardType]
        
        cardsSortedByCost = sorted(cardsForType, key=lambda card: card.calculatePoints(context))
        cards[cardType] = {str(points):list(cardsForPoints) for points, cardsForPoints in groupby(cardsSortedByCost, key=lambda card: card.calculatePoints(context))}
        cards[cardType]['total'] = sum([int(points)*len(cardsForPoints) for points, cardsForPoints in cards[cardType].items()])
        cards[cardType]['pointValues'] = sorted([points for points in cards[cardType].keys() if points != 'total'])
        
    cards['cardTypes'] = cardTypes
    return cards

resultsConfig = [(GameResults, [FieldAttr('players', field='playerResults')]),
                 (PlayerResults, [FieldAttr('points'),
                                  FieldAttr('name', field='player.name'),
                                  JsonAttr('isYou', lambda results, currentPlayer: results.player is currentPlayer, args=['currentPlayer']),
                                  JsonAttr('cards', GetCards, args=['game'])])]