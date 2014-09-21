from Game.Effects.effect_arguments import EffectArguments
from Game.Sources.source_factory import SourceFactory, DISCARD_PILE

class BuyCard:
    """ Represents a command to buy a card """
    
    def __init__(self, card, owner, source):
        """ Initialize the Buy Card Command """
        self.card = card
        self.owner = owner
        self.source = source
        
    def perform(self):
        """ Perform the command """
        args = EffectArguments(self.owner.game, self.card)
        self.owner.spendPower(self.card.calculateCost())
        coroutine = self.owner.gainCard(self.card, self.source, toSource=SourceFactory.getSourceForEffect(DISCARD_PILE, args))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)