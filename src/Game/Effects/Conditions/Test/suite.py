import unittest

from Game.Effects.Conditions.Test.and_condition_test import suite as and_condition_suite
from Game.Effects.Conditions.Filters.Test.suite import suite as filters_suite

suites = [filters_suite,
          and_condition_suite]
suite = unittest.TestSuite(suites)