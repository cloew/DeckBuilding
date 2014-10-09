from Game.Sources.source_types import HAND
import random

class ShuffleAndDeal:
    """ Represents an effect to Shuffle Cards and Deal them to the foes """
    
    def __init__(self):
        """ Initialize the Effect """
        
    def perform(self, context):
        """ Perform the Game Effect """
        allCards = self.getCardsToDeal(context)
        for foe in context.foes:
            if len(allCards) > 0:
                source = context.getPlayerContext(foe).loadSource(HAND)
                source.add(allCards.pop())
        
    def getCardsToDeal(self, context):
        """ Get the Cards to Deal to the Character """
        allCards = []
        for card in list(context.event):
            context.event.remove(card)
            allCards.append(card)
        random.shuffle(allCards)
        return allCards