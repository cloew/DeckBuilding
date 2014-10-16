import unittest

from Game.Effects.Activatables.Test.suite import suite as activatables_suite
from Game.Effects.Triggers.Test.suite import suite as triggers_suite
from Game.Effects.Conditions.Test.suite import suite as conditions_suite

suites = [conditions_suite,
          triggers_suite,
          activatables_suite]
suite = unittest.TestSuite(suites)