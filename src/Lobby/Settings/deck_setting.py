from Game.Decks.deck_factory import DeckFactory

class DeckSetting:
    """ Represents a setting for choosing a deck for a specific role """
    
    def __init__(self, role):
        """ Initialize the Deck Setting with the role its filling """
        self.role = role
        self.potentialDeckIds = DeckFactory.findDeckIdsToFillRole(role)
        self.index = 0
        
    def setDeck(self, index):
        """ Set the deck for this setting """
        self.index = (index + len(self.potentialDeckIds)) % len(self.potentialDeckIds)
        print "Deck Setting Index:", self.index
        print "Deck Setting Id:", self.deckId
        
    def loadDeck(self, **kwargs):
        """ Load the current deck """
        print "Loading Deck Setting:", self.deckId
        return DeckFactory.load(self.deckId).loadDeck(**kwargs)
        
    @property
    def deckId(self):
        """ Return the currently selected deck id """
        print "Potential Deck Ids:", self.potentialDeckIds
        return self.potentialDeckIds[self.index]