from Game.Effects.effect_arguments import EffectArguments
from Game.Effects.Conditions.has_cards import HasCards
from Game.Effects.Conditions.not_condition import NotCondition

from Game.Sources.source_factory import MAIN_DECK

class GameOver:
    """ Represents how to check if a game is over """
    
    def __init__(self, game):
        """ Initialize the Game """
        self.game = game
        self.condition = NotCondition(HasCards(MAIN_DECK))
    
    @property
    def isOver(self):
        """ Return if the game is over """
        return self.condition.evaluate(EffectArguments(self.game, None))