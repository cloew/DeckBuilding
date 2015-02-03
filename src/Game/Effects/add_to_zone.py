
class AddToZone:
    """ Represents an effect to Add a card to the zone """
    
    def __init__(self, card, zone):
        """ Initialize the Effect with the card and the zone to add it to """
        self.card = card
        self.zone = zone
        
    def perform(self, context):
        """ Perform the Game Effect """
        self.zone.add(self.card)