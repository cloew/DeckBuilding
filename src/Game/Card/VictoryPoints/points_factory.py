from Game.Card.VictoryPoints.conditional_points import ConditionalPoints
from Game.Card.VictoryPoints.fixed_points import FixedPoints

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory

class PointsFactory:
    """ Factory to create VP Calculators """
        
    def loadPointsCalculator(self, pointsJson):
        """ Load the Points Calculator in the given JSON """
        pointsType = pointsJson['type']
        
        if pointsType == "CONDITIONAL":
            return ConditionalPoints(ConditionFactory.loadCondition(pointsJson["condition"]), 
                                     self.loadPointsCalculator(pointsJson["points"]),
                                     self.loadPointsCalculator(pointsJson["otherwise"]))
        elif pointsType == "FIXED":
            return FixedPoints(pointsJson["points"])
        return None
        
PointsFactory = PointsFactory()