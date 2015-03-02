from Game.Context.system_context import SystemContext
from Game.Effects.effect_runner import PerformEffects

class SuperVillainStack:
    """ Represents the Super Villain Stack of available cards in the game """
    LINE_UP_SIZE = 5
    
    def __init__(self, superVillains):
        """ Initialize the Super Villain Stack """
        self.superVillains = superVillains
        self.getTopCard()
        
    def getTopCard(self):
        """ Get the top card of the super villain stack """
        self.topCard = self.superVillains.peek()
        self.hasAppeared = True
        
    def refill(self):
        """ Refill the supervillain stack if needed """
        if self.topCard is None:
            self.getTopCard()
            
    def performFirstAppearanceEffects(self, game):
        """ Perform the Super Villain's First Appearance Effects """
        if self.hasAppeared:
            self.hasAppeared = False
            coroutine = PerformEffects(self.topCard.appearanceEffects, SystemContext(game, self.topCard))
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)
        
    @property
    def cards(self):
        """ Return if the Super Villain can be bought """
        if self.available:
            return [self.topCard]
        else:
            return []
        
    @property
    def available(self):
        """ Return if the Super Villain is available """
        return self.topCard is not None
            
    def remove(self, card):
        """ Remove a card from the stack """
        self.topCard = None
        self.superVillains.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.superVillains[index]
        
    def __len__(self):
        """ Return the length of the Line Up """
        return len(self.superVillains)
        
    def __iter__(self):
        """ Return the Line-up Iterator """
        return self.superVillains.__iter__()