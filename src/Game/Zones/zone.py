from kao_decorators import proxy_for

@proxy_for('zoneType', ['public'])
class Zone:
    """ Represents a potential zone """
    
    def __init__(self, zoneObject, zoneType=None):
        """ Initialize the zone """
        self.zone = zoneObject
        self.zoneType = zoneType
        
    def add(self, card):
        """ Add the given card to the zone """
        self.zone.add(card)
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.zone.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.zone[index]
        
    def __iter__(self):
        """ Return the Deck Iterator """
        return self.zone.__iter__()
        
    def availableLength(self):
        """ Return the number of available cards """
        return self.__len__()
        
    def __len__(self):
        """ Return the Length of the Deck """
        return len(self.zone)