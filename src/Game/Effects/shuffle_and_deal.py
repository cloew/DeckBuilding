from Game.Zones.zone_types import EVENT, HAND
import random

class ShuffleAndDeal:
    """ Represents an effect to Shuffle Cards and Deal them to the foes """
        
    def perform(self, context):
        """ Perform the Game Effect """
        allCards = self.getCardsToDeal(context)
        while (len(allCards) > 0):
            for foe in context.foes:
                if len(allCards) > 0:
                    zone = context.getPlayerContext(foe).loadZone(HAND)
                    zone.add(allCards.pop())
        
    def getCardsToDeal(self, context):
        """ Get the Cards to Deal to the Character """
        allCards = []
        eventZone = context.loadZone(EVENT)
        for card in list(eventZone):
            eventZone.remove(card)
            allCards.append(card)
        random.shuffle(allCards)
        return allCards