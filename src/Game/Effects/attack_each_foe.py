from Game.Effects.attack import Attack
from Game.Effects.per_foe import PerFoe

class AttackEachFoe(Attack):
    """ Represents an effect to Attack other Players """
    
    def __init__(self, effects):
        """ Initialize with the effects to attack each foe with """
        Attack.__init__(self, [PerFoe(effects)])