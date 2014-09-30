from Game.Effects.effect_arguments import EffectArguments
from Game.Effects.Conditions.full_line_up import FullLineUp
from Game.Effects.Conditions.has_cards import HasCards
from Game.Effects.Conditions.not_condition import NotCondition
from Game.Effects.Conditions.or_condition import OrCondition

from Game.Sources.source_factory import SUPERVILLAIN

class GameOver:
    """ Represents how to check if a game is over """
    
    def __init__(self, game):
        """ Initialize the Game """
        self.game = game
        self.condition = OrCondition([NotCondition(FullLineUp()), NotCondition(HasCards(SUPERVILLAIN))])
    
    @property
    def isOver(self):
        """ Return if the game is over """
        return self.condition.evaluate(EffectArguments(self.game, None))