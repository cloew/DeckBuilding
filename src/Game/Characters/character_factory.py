from character import Character

from Game.Effects.Activatables.activatable_factory import ActivatableFactory
from Game.Effects.Triggers.trigger_factory import TriggerFactory

import resources.resource_manager as resource_manager

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

CHARACTER_FILENAME = resource_manager.GetResourcePath("characters.json")

parameters = [PrimitiveParameter("name"),
              ComplexParameter("triggers", TriggerFactory.loadTriggers, optional=True, default=[]),
              ComplexParameter("activatableEffect", ActivatableFactory.loadActivatable, optional=True),
              PrimitiveParameter("image", optional=True)]
    
CharacterFactory = DataSourceFactory(Character, parameters, JsonSource(CHARACTER_FILENAME), "name")