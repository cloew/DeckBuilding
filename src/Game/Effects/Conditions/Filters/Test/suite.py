import unittest

from Game.Effects.Conditions.Filters.Operations.Test.suite import suite as operations_suite
from Game.Effects.Conditions.Filters.Criteria.Test.suite import suite as criteria_suite

suites = [criteria_suite,
          operations_suite]
suite = unittest.TestSuite(suites)