import unittest

from Game.Effects.Triggers.Test.suite import suite as triggers_suite
from Game.Effects.Conditions.Test.suite import suite as conditions_suite

suites = [conditions_suite,
          triggers_suite]
suite = unittest.TestSuite(suites)