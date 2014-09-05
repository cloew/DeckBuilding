from Game.Card.card import Card
from Game.Card.Cost.fixed_cost import FixedCost

import resources.resource_manager as resource_manager

import json

class CardFactory:
    """ Factory to load Cards from the Card JSON file """
    CARD_FILENAME = resource_manager.GetResourcePath("cards.json")
    
    def __init__(self):
        """ Initialize the Card Factory """
        self.__cardsJson__ = None
        
    def loadCard(self, cardName):
        """ Load the card with the given name """
        cardJson = self.findCardJson(cardName)
        if cardJson is not None:
            name = cardJson["name"]
            cost = cardJson["cost"]["cost"]
            return Card(name, costCalculator=FixedCost(0))
        return None
        
    def findCardJson(self, cardName):
        """ Find the proper card JSON """
        matchingCardsJson = [cardJson for cardJson in self.cardsJson if cardJson["name"] == cardName]
        if len(matchingCardsJson) > 0:
            return matchingCardsJson[0]
        return None
            
    @property
    def cardsJson(self):
        """ Lazy-load the card Json """
        if self.__cardsJson__ is None:
            self.loadJson()
        return self.__cardsJson__
        
    def loadJson(self):
        """ Load the Card JSON """
        with open(self.CARD_FILENAME, 'r') as file:
            self.__cardsJson__ = json.load(file)
            
            
CardFactory = CardFactory()