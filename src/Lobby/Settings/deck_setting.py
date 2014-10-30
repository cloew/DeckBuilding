from Game.Decks.deck_factory import DeckFactory

class DeckSetting:
    """ Represents a setting for choosing a deck for a specific role """
    
    def __init__(self, role):
        """ Initialize the Deck Setting with the role its filling """
        self.role = role
        self.potentialDeckIds = DeckFactory.findDeckIdsToFillRole(role)
        self.index = 0
        self.deckId = self.potentialDeckIds[0]
        
    def setDeck(self, index):
        """ Set the deck for this setting """
        self.index = (index + len(self.potentialDeckIds)) % len(self.potentialDeckIds)
        
    def loadDeck(self, **kwargs):
        """ Load the current deck """
        return DeckFactory.load(self.deckId).loadDeck(**kwargs)
        
    @property
    def deckId(self):
        """ Return the currently selected deck id """
        return self.potentialDeckIds[self.index]