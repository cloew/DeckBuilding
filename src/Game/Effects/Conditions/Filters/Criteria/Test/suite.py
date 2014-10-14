import unittest

from Game.Effects.Conditions.Filters.Criteria.Test.source_criteria_test import suite as source_criteria_suite
from Game.Effects.Conditions.Filters.Criteria.Test.fixed_criteria_test import suite as fixed_criteria_suite

suites = [fixed_criteria_suite,
          source_criteria_suite]
suite = unittest.TestSuite(suites)