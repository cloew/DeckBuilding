
nameToZoneType = {}

class ZoneType:
    """ Represents a type of Zone """
    
    def __init__(self, name, public=False):
        """ Initialize the Zone Type """
        global nameToZoneType
        self.name = name
        self.public = public
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
DESTROYED = ZoneType("DESTROYED", public=True)
DISCARD_PILE = ZoneType("DISCARD_PILE", public=True)
EVENT = ZoneType("EVENT")
GAINED = ZoneType("GAINED", public=True)
HAND = ZoneType("HAND")
KICK = ZoneType("KICK", public=True)
LINE_UP = ZoneType("LINE_UP", public=True)
MAIN_DECK = ZoneType("MAIN_DECK")
ONGOING = ZoneType("ONGOING", public=True)
PLAYED = ZoneType("PLAYED", public=True)
SUPERVILLAIN = ZoneType("SUPERVILLAIN", public=True)
UNDER_CHARACTER = ZoneType("UNDER_CHARACTER", public=True)
WEAKNESS = ZoneType("WEAKNESS", public=True)