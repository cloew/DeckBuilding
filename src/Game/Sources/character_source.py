from source import Source

class CharacterSource(Source):
    """ Represents a Character Source """
    
    def __init__(self, character):
        """ Initialize the source """
        self.character = character
        Source.__init__(self, character)
        
    def add(self, card):
        """ Add the given card to the source """
        raise NotImplemented
        
    def remove(self, card):
        """ Remove the card from the deck """
        raise NotImplemented
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return [self.character][index]
        
    def __iter__(self):
        """ Return the Deck Iterator """
        return [self.character].__iter__()
        
    def __len__(self):
        """ Return the Length of the Deck """
        return 1