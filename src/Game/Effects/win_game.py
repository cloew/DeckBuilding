from Game.Results.effect_player_results import EffectPlayerResults

class WinGame:
    """ Represents an effect to Win the Game """
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.game.endAfterThisTurn({context.player:EffectPlayerResults})