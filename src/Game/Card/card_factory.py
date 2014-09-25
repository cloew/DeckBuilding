from Game.Card.card import Card
from Game.Card.Cost.fixed_cost import FixedCost
from Game.Card.VictoryPoints.points_factory import PointsFactory

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Activatables.activatable_factory import ActivatableFactory
from Game.Effects.Triggers.trigger_factory import TriggerFactory

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
            cardType = cardJson["type"]
            cost = cardJson["cost"]["cost"]
            
            image = None
            if "image" in cardJson:
                image = cardJson["image"]
            return Card(name, cardType, costCalculator=FixedCost(cost), vpCalculator=PointsFactory.loadPointsCalculator(cardJson["points"]),
                        playEffects=self.loadPlayEffects(cardJson), triggers=self.loadTriggers(cardJson), activatable=self.loadActivatable(cardJson), image=image)
        else:
            print "Unable to load Card:", cardName
        return None
        
    def findCardJson(self, cardName):
        """ Find the proper card JSON """
        matchingCardsJson = [cardJson for cardJson in self.cardsJson if cardJson["name"] == cardName]
        if len(matchingCardsJson) > 0:
            return matchingCardsJson[0]
        return None
        
    def loadPlayEffects(self, cardJson):
        """ Load the Card's Play Effects """
        playEffects = []
        if "playEffects" in cardJson:
            playEffects = EffectFactory.loadEffects(cardJson["playEffects"])
        return playEffects
        
    def loadTriggers(self, cardJson):
        """ Load the Card's Trigger Effects """
        triggers = []
        if "triggers" in cardJson:
            triggers = TriggerFactory.loadTriggers(cardJson["triggers"])
        return triggers
        
    def loadActivatable(self, cardJson):
        """ Load the Card's Activatble Effect, if any """
        activatableEffect = None
        if "activatableEffect" in cardJson:
            activatableEffect = ActivatableFactory.loadActivatable(cardJson["activatableEffect"])
        return activatableEffect
            
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