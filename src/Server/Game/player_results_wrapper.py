from json_helper import GetCardListJSON

from itertools import groupby

class PlayerResultsWrapper:
    """ A Wrapper for a Player's Game Results """
    
    def __init__(self, player, isYou):
        """ Initialize the Player Wrapper """
        self.player = player
        self.isYou = isYou
        
    def toJSON(self, game):
        """ Return the Player as a JSON Dictionary """
        cards = {}
        cardsByType = {str(cardType):list(cardsForType) for cardType, cardsForType in groupby(sorted(self.player.deck, key=lambda card: card.cardType), key=lambda card: card.cardType)}
        
        cardTypes = []
        for cardType in cardsByType:
            cardTypes.append(cardType)
            cardsForType = cardsByType[cardType]
            
            cardsSortedByCost = sorted(cardsForType, key=lambda card: card.calculatePoints(game))
            cards[cardType] = {str(points):GetCardListJSON(cardsForPoints, game) for points, cardsForPoints in groupby(cardsSortedByCost, key=lambda card: card.calculatePoints(game))}
            cards[cardType]['pointValues'] = list(cards[cardType].keys())
            
        cards['cardTypes'] = cardTypes
        return {'points':self.player.calculatePoints(game), 'name':self.player.name, 'isYou':self.isYou, 'cards':cards}