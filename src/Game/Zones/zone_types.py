
nameToZoneType = {}

class ZoneType:
    """ Represents a type of Zone """
    
    def __init__(self, name):
        """ Initialize the Zone Type """
        global nameToZoneType
        self.name = name
        nameToZoneType[name] = self
        
    def __eq__(self, other):
        """ Return if this Zone Type is equal to other """
        if not hasattr(other, 'name'):
            return NotImplemented
        return self.name == other.name
        
    def __repr__(self):
        """ Return the string representation of the Zone Type """
        return "<{0} at {1:#x}>".format(self.name, id(self))

CHARACTER = ZoneType("CHARACTER")
DECK = ZoneType("DECK")
DESTROYED = ZoneType("DESTROYED")
DISCARD_PILE = ZoneType("DISCARD_PILE")
EVENT = ZoneType("EVENT")
GAINED = ZoneType("GAINED")
HAND = ZoneType("HAND")
KICK = ZoneType("KICK")
LINE_UP = ZoneType("LINE_UP")
MAIN_DECK = ZoneType("MAIN_DECK")
ONGOING = ZoneType("ONGOING")
PLAYED = ZoneType("PLAYED")
SUPERVILLAIN = ZoneType("SUPERVILLAIN")
UNDER_CHARACTER = ZoneType("UNDER_CHARACTER")
WEAKNESS = ZoneType("WEAKNESS")