from Game.Effects.as_player_with_highest_cost import AsPlayerWithHighestCost
from Game.Effects.effect_runner import PerformEffects
from Game.Zones.zone_types import EVENT

class AsOnlyPlayerWithHighestCost(AsPlayerWithHighestCost):
    """ Represents an effect to run as the Player who has the greatest cost of cards """
    
    def __init__(self, thenEffects):
        """ Initialize the Effect with the children effects and the zone to check from """
        self.zoneType = EVENT
        self.thenEffects = thenEffects
        
    def perform(self, context):
        """ Perform the Game Effect """
        players = self.findHighestCostPlayers(context)
        
        if len(players) == 1:
            player = players[0]
            newContext = context.getPlayerContext(player)
            
            coroutine = PerformEffects(self.thenEffects, newContext)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        
    def findCardsforPlayer(self, context, player):
        """ Find cards for the given player """
        return context.loadZone(self.zoneType).event.cardsForPlayer(player)