from Game.Card.card import Card
from Game.Card.Cost.fixed_cost import FixedCost
from Game.Card.VictoryPoints.points_factory import PointsFactory

from Game.Effects.effect_factory import EffectFactory
from Game.Effects.Activatables.activatable_factory import ActivatableFactory
from Game.Effects.Triggers.trigger_factory import TriggerFactory

import resources.resource_manager as resource_manager

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

def loadCost(data):
    """ Load the Cost """
    return FixedCost(data["cost"])

CARD_FILENAME = resource_manager.GetResourcePath("cards.json")

parameters = [PrimitiveParameter("name"),
              PrimitiveParameter("type", optional=True),
              ComplexParameter("cost", loadCost),
              ComplexParameter("points", PointsFactory.load),
              ComplexParameter("playEffects", EffectFactory.loadAll, optional=True, default=[]),
              ComplexParameter("onGain", EffectFactory.loadAll, optional=True, default=[]),
              ComplexParameter("onDefense", EffectFactory.loadAll, optional=True, default=[]),
              ComplexParameter("triggers", TriggerFactory.loadAll, optional=True, default=[]),
              ComplexParameter("activatableEffect", ActivatableFactory.load, optional=True),
              PrimitiveParameter("image", optional=True)]
    
CardFactory = DataSourceFactory(Card, parameters, JsonSource(CARD_FILENAME), "name")