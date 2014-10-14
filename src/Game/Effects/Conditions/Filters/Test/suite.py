import unittest

from Game.Effects.Conditions.Filters.Test.intersection_filter_test import suite as intersection_filter_suite
from Game.Effects.Conditions.Filters.Test.comparison_filter_test import suite as comparison_filter_suite
from Game.Effects.Conditions.Filters.Operations.Test.suite import suite as operations_suite
from Game.Effects.Conditions.Filters.Criteria.Test.suite import suite as criteria_suite

suites = [criteria_suite,
          operations_suite,
          comparison_filter_suite,
          intersection_filter_suite]
suite = unittest.TestSuite(suites)