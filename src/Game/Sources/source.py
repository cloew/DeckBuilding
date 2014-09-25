
class Source:
    """ Represents a potential source """
    
    def __init__(self, sourceObject):
        """ Initialize the source """
        self.source = sourceObject
        
    def add(self, card):
        """ Add the given card to the source """
        self.source.add(card)
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.source.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.source[index]
        
    def __iter__(self):
        """ Return the Deck Iterator """
        return self.source.__iter__()
        
    def availableLength(self):
        """ Return the number of available cards """
        return self.__len__()
        
    def __len__(self):
        """ Return the Length of the Deck """
        return len(self.source)