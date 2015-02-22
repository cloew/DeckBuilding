from zone import Zone
from zone_types import CHARACTER

class CharacterZone(Zone):
    """ Represents a Character Zone """
    
    def __init__(self, character, player):
        """ Initialize the zone """
        self.character = character
        Zone.__init__(self, character, player, zoneType=CHARACTER)
        
    def add(self, card):
        """ Add the given card to the zone """
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