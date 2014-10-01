
class Character:
    """ Represents a Player Character """
    
    def __init__(self, name, triggers=[], activatable=None, image="batman.jpg"):
        """ Initialize the Character """
        self.name = name
        self.activatableEffect = activatable
        self.triggerEffects = triggers
        self.image = image
        self.active = True
        
    def deactivate(self):
        """ Deactivate the character """
        self.active = False