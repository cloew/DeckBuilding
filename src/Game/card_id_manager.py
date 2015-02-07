
class CardIdManager:
    """ Represents a manager for tracking card ids and the cards they belong to """
    
    def __init__(self, game):
        """ Initialize the card id manager """
        self.nextId = 1
        self.idToCard = {}
        
        for player in game.players:
            self.assignId(player.character)
            for card in player.deck:
                self.assignId(card)
            for card in player.hand:
                self.assignId(card)
                
        for deck in [game.mainDeck, game.kickDeck, game.weaknessDeck, game.superVillainStack]:
            for card in deck:
                self.assignId(card)
                
    def getCardFromId(self, id):
        """ Return the card that matches the given id """
        return self.idToCard[id]
                
    def assignId(self, card):
        """ Assign an Id to the given card """
        card.gameId = self.nextId
        self.idToCard[card.gameId] = card
        
    @property
    def nextId(self):
        """ Return the next id """
        id = self.__nextId
        self.__nextId += 1
        return id