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
        cardsByType = {type:cardsForType for type, cardsForType in groupby(sorted(self.player.deck, key=lambda card: card.cardType))}
        for cardType in cardsByType:
            cardsForType = cardsByType[cardType]
            cards[cardType] = {points:list(cardsForPoints) for points, cardsForPoints in groupby(sorted(list(cardsForType), key=lambda card: card.calculatePoints(game)))}
        return {'points':self.player.calculatePoints(game), 'name':self.player.name, 'isYou':self.isYou, 'cards':cards}