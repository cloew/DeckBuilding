from Game.Card.card_factory import CardFactory

from kao_deck.deck_initializer import DeckInitializer

import resources.resource_manager as resource_manager

import json

class DeckFactory:
    """ Factory to load Decks from JSON """
    DECK_FILENAME = resource_manager.GetResourcePath("decks.json")
    
    def __init__(self):
        """ Initialize the Card Factory """
        self.__decksJson__ = None
        
    def loadDeck(self, deckName):
        """ Load the Deck with the given name """
        deckJson = self.findDeckJson(deckName)
        if deckJson is not None:
            deckInitializer = DeckInitializer()
            for cardJson in deckJson["cards"]:
                cardName = cardJson["name"]
                count = cardJson["count"]
                card = CardFactory.loadCard(cardName)
                deckInitializer.addItem(card, count)
            return deckInitializer
        return None
        
    def findDeckJson(self, deckName):
        """ Find the proper deck JSON """
        matchingDecksJson = [deckJson for deckJson in self.decksJson if deckJson["name"] == deckName]
        if len(matchingDecksJson) > 0:
            return matchingDecksJson[0]
        return None
        
    @property
    def decksJson(self):
        """ Lazy-load the card Json """
        if self.__decksJson__ is None:
            self.loadJson()
        return self.__decksJson__
        
    def loadJson(self):
        """ Load the Deck JSON """
        with open(self.DECK_FILENAME, 'r') as file:
            self.__decksJson__ = json.load(file)
            
DeckFactory = DeckFactory()