import unittest

from Game.Effects.Conditions.Filters.Criteria.Test.suite import suite as criteria_suite

suites = [criteria_suite]
suite = unittest.TestSuite(suites)