from Game.Card.VictoryPoints.conditional_points import ConditionalPoints
from Game.Card.VictoryPoints.fixed_points import FixedPoints
from Game.Card.VictoryPoints.per_result_points import PerResultPoints

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory
from Game.Effects.Conditions.Filters.filter_factory import FilterFactory

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

PointsFactory = TypedFactory('type', {"FIXED":Factory(FixedPoints, [PrimitiveParameter("points")]),
                                      "PER_RESULT":Factory(PerResultPoints, [ComplexParameter("filter", FilterFactory.load), PrimitiveParameter("points", optional=True)])})
PointsFactory.addFactory("CONDITIONAL", Factory(ConditionalPoints, [ComplexParameter("condition", ConditionFactory.load),
                                                                    ComplexParameter("points", PointsFactory.load),
                                                                    ComplexParameter("otherwise", PointsFactory.load)]))