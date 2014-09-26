from Game.Effects.per_foe import PerFoe

class Attack(PerFoe):
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effect):
        """ Initialize with the effect to attack with """
        PerFoe.__init__(self, [effect])