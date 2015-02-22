from Game.coroutine_helper import RunCoroutineOrFunction
from Game.Commands.Requests.pick_card_request import PickCardRequest
from Game.Effects.effect_runner import PerformEffects
from Game.Events.cards_event import CardsEvent
from Game.Events.multi_zone_event import MultiZoneEvent
from Game.Zones.event_zone import EventZone
from Game.Zones.zone_types import DECK

PICK = "PICK"
TOP = "TOP"

class CollectCards:
    """ Represents an effect to Collect Cards from the top of your opponents decks """
    
    def __init__(self, thenEffects, zoneType=None, pickType=None, number=None, toDescription=None):
        """ Initialize the Effect with the effects to call with the collected cards """
        self.thenEffects = thenEffects
        
        if zoneType is None:
            zoneType = DECK
        self.zoneType = zoneType
        
        if pickType is None:
            pickType = TOP
        self.pickType = pickType
        
        if number is None:
            number = 1
        self.number = number
        
        if toDescription is None:
            toDescription = ""
        self.toDescription = toDescription
        
    def perform(self, context):
        """ Perform the Game Effect """
        typeToFunction = {TOP:self.getTopCards,
                          PICK:self.pickCards}
        function = typeToFunction[self.pickType]
        
        self.cardsForFoes = []
        zones = []
        for foe in context.foes:
            playerContext = context.getPlayerContext(foe)
            zone = playerContext.loadZone(self.zoneType)
            coroutine = RunCoroutineOrFunction(function, [playerContext, zone, self.number])
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass
            event = CardsEvent(self.cardsForFoes, zone, playerContext)
            zones.append(event.loadZone())
                
        event = MultiZoneEvent(zones, context)
        coroutine = PerformEffects(self.thenEffects, event.context)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)
            
    def getTopCards(self, context, zone, number):
        """ Get the Top Cards """
        self.cardsForFoes = zone[:number]
            
    def pickCards(self, context, zone, number):
        """ Get the Top Cards """
        self.cardsForFoes = yield PickCardRequest(zone, context.player, number, self.toDescription)
        