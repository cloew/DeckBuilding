from card_wrapper import GetCardListJSON

from Game.Effects.game_contexts import PlayerContext

from itertools import groupby

class PlayerResultsWrapper:
    """ A Wrapper for a Player's Game Results """
    
    def __init__(self, playerResults, isYou):
        """ Initialize the Player Wrapper """
        self.playerResults = playerResults
        self.player = playerResults.player
        self.isYou = isYou
        
    def toJSON(self, game):
        """ Return the Player as a JSON Dictionary """
        context = PlayerContext(game, None, player=self.player)
        
        cards = {}
        cardsByType = {str(cardType):list(cardsForType) for cardType, cardsForType in groupby(sorted(self.player.deck, key=lambda card: card.cardType), key=lambda card: card.cardType)}
        
        cardTypes = []
        for cardType in sorted(cardsByType.keys()):
            cardTypes.append(cardType)
            cardsForType = cardsByType[cardType]
            
            cardsSortedByCost = sorted(cardsForType, key=lambda card: card.calculatePoints(context))
            cards[cardType] = {str(points):GetCardListJSON(cardsForPoints) for points, cardsForPoints in groupby(cardsSortedByCost, key=lambda card: card.calculatePoints(context))}
            cards[cardType]['total'] = sum([int(points)*len(cardsForPoints) for points, cardsForPoints in cards[cardType].items()])
            cards[cardType]['pointValues'] = sorted([points for points in cards[cardType].keys() if points != 'total'])
            
        cards['cardTypes'] = cardTypes
        return {'points':self.playerResults.points, 'name':self.player.name, 'isYou':self.isYou, 'cards':cards}