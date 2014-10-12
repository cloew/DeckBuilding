
class Character:
    """ Represents a Player Character """
    
    def __init__(self, name, triggers=[], activatable=None, image="batman.jpg"):
        """ Initialize the Character """
        self.name = name
        self.goesFirst = False
        self.activatableEffect = activatable
        self.triggerEffects = triggers
        self.image = image
        self.active = True
        
    def addOngoingEffects(self, addOngoingEffects):
        """ Add Starting Effects for the current player """            
        if self.active:
            addOngoingEffects(self)
            
    def activate(self, turn):
        """ Activate the character and add the ongoing effects if it is the player's turn """
        wasInactive = self.active == False
        self.active = True
        if wasInactive and turn.player.character is self:
            self.addOngoingEffects(turn.addOngoingEffects)
        
    def deactivate(self):
        """ Deactivate the character """
        self.active = False