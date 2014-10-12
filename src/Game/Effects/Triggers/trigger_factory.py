from Game.Effects.Triggers.trigger import Trigger

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Conditions.condition_factory import ConditionFactory

from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

TriggerFactory = Factory(Trigger, [PrimitiveParameter("type"),
                                   ComplexParameter("effect", EffectFactory.load),
                                   ComplexParameter("condition", ConditionFactory.load, optional=True),
                                   PrimitiveParameter("singleUse")])