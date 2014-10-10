from Game.Effects.play_or_have_played import PlayOrHavePlayed
from Game.Effects.Conditions.and_condition import AndCondition

class PlayOrHavePlayedAnother(PlayOrHavePlayed):
    """ Represents an effect that conditionally applies """
        
    def getTriggerCondition(self, playedCondition, eventCondition):
        """ Get the Condition for the Trigger """
        return AndCondition([playedCondition, eventCondition])